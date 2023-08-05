#!/usr/bin/python3

import os
import tempfile
import argparse 
import numpy as np
import sqlite3
import time 
import glob
import dask
import dask.distributed
from dask.delayed import delayed
import copy
import sys
import datetime
import radvelso

def find_schema(schema):
  """find schema file contained in the Python package

   args: 
     schema: the schema we are looking for

   output:
     full path of schema file that was found
  """

  #full path of radvelso module
  radvelso_dir = os.path.dirname(radvelso.__file__)
  #root path of radvelso package (one dir up from radvelso module)
  package_dir = os.path.dirname(radvelso_dir)
  #full path of schema we are looking for
  schema_file = f'{package_dir}/radvelso/schema/{schema}'

  if not os.path.isfile(schema_file):
    raise ValueError(f'schema_file: {schema_file} does not exist')

  return schema_file


def make_input_db(filein, this_time):

  """make a separate db for one PPI

   This db is saved in memory and allows quich search of averaging boxes

   args: 
     filein                 : input sqlite file containing many radars and times
     stn                    : radar for this one volume scan
     this_time              : end time of this one volume san
     nominal_ppi_elevation  : nominal elevation
     min_range_in_ppi       : min range in PPI
     max_range_in_ppi       : max range in PPI
     obs_nyquist            : Nyquist for QC
   output: 
     sqlite connection to the created db

  """

  
  # https://tools.ietf.org/html/rfc3986  Uniform Resource Identifier (URI)
  # The advantage of using a URI filename is that query parameters on the
  # URI can be used to control details of the newly created database connection in parallel
  conn_ppi_db = sqlite3.connect("file::memory:?cache=shared",uri=True)
  # off the journal
  conn_ppi_db.execute("""PRAGMA journal_mode=OFF;""")
  # SQLite continues without syncing as soon as it has handed data off to the operating system
  conn_ppi_db.execute("""PRAGMA synchronous=OFF;""")

  schema = find_schema('schema')
  with open(schema) as f:
    schema = f.read()
  conn_ppi_db.executescript(schema)
  # improve searches with index tables
  create_index_tables_elevation_azimuth(conn_ppi_db)
  create_index_tables_idobs_iddata(conn_ppi_db)
  # attach database
  conn_ppi_db.execute("ATTACH DATABASE ? AS db_all", (filein,)) 
  #select headers in desirec PPI
  order_sql = """ INSERT into header 
                  SELECT 
                    * 
                  FROM
                    db_all.header 
                  WHERE
                    time = ? 
                    ;"""
  conn_ppi_db.execute(order_sql, ( this_time,))
  #select associated data entries
  order_sql = """ INSERT into data 
                  SELECT
                    * 
                  FROM
                    db_all.data 
                  WHERE
                    id_obs in (SELECT
                                 id_obs 
                               FROM
                                 header  );"""
  conn_ppi_db.execute(order_sql)

  conn_ppi_db.commit()

  return conn_ppi_db

def create_index_tables_elevation_azimuth(conn):
  """ Create index tables
  For elevation and azimuth  
  args:
    conn          : connextion to sqlite file
  output:
    Nothing
    index tables i sqlite file
 
  """

  order_sql ="""CREATE INDEX 
                  NOMINAL_PPI_ELEVATIONS 
                ON header (NOMINAL_PPI_ELEVATION);"""
  conn.execute(order_sql)

  order_sql ="""CREATE INDEX
                  CENTER_AZIMUTHS 
                ON header (CENTER_AZIMUTH);"""
  conn.execute(order_sql)

def create_index_tables_idobs_iddata(conn):
  """ Create index tables
  For id_obs and id_data
  args:
    conn          : connextion to sqlite file
  output:
    Nothing
    index tables i sqlite file

  """
  
  order_sql = """ CREATE INDEX
                    idx1
                  ON header(id_obs);"""
  conn.execute(order_sql)
  
  order_sql = """CREATE INDEX
                   idx2 
                 ON data(id_obs);"""
  conn.execute(order_sql)

  order_sql = """CREATE INDEX
                   idx3 
                 ON data(id_data);"""
  conn.execute(order_sql)

def create_info_midas_tables(filein,
                              conn_pathfileout):
  """ Create header entry

  A header is created matching a bunch of entries in data table

  args:
    filein        : input sqlite file with raw data
    conn_pathfileout  : connextion to output file
    n_rays        : number of rays 
    delta_range   : delta range of the boxes
   ops_run_name  : name of operational run
    obs_percentage:
    obs_nyquist   :
  output:
    Nothing
    info table entry is written in output sqlite file

  """
  
  conn_pathfileout.execute("""ATTACH DATABASE ? AS db_all""", (filein,) ) 

  # Info table
  order_sql ="""CREATE TABLE info( NAME, DESCRIPTION, UNIT );"""
  conn_pathfileout.execute( order_sql)
  order_sql =""" INSERT  into  info (
                   NAME, DESCRIPTION, UNIT) 
                 SELECT * 
                   from  db_all.info """
  conn_pathfileout.execute( order_sql)


  # Resume table 
  order_sql ="""CREATE TABLE resume(date integer , time integer , run varchar(9));"""
  conn_pathfileout.execute( order_sql)

  order_sql = """INSERT into resume (
                    date, time, run) 
                  SELECT * 
                   from  db_all.resume """
  conn_pathfileout.execute( order_sql)
  
  # rdb4_schema table
  order_sql ="""CREATE TABLE rdb4_schema( schema  varchar(9) );"""
  conn_pathfileout.execute( order_sql)
  order_sql ="""INSERT into rdb4_schema (
                 schema)
                SELECT * 
                   from  db_all.rdb4_schema  """
  conn_pathfileout.execute( order_sql)

  # commint and detach database
  conn_pathfileout.commit()
  conn_pathfileout.execute("DETACH DATABASE db_all")

def getHfromRange(beamRange, radarAltitude, beamElevation):
    import math
    #!
    #! :Purpose: Computation of height of the radar beam
    #!           from range of the radar beam
    #!
    #! Radius of sphere of equal area from earthconstants_mod.f90
    ec_wgs_R2 = 6371007.1809
    #! effective radius of the earth
    Re = ec_wgs_R2*(4./3.)
    #! height of radar beam  from range at beamElevation and radarAltitude 
    beamHeight = math.sqrt(beamRange**2.+(Re+radarAltitude)**2.+2.*beamRange*(Re+radarAltitude)*math.sin(math.radians(beamElevation)))-(Re)

    return  beamHeight 

def distance_between_two_points(lat1, lon1, lat2, lon2):
  import math
  # approximate radius of earth in km
  R =  6371007.1809

  lat1 = np.radians(lat1)
  lon1 = np.radians(lon1)
  lat2 = np.radians(lat2)
  lon2 = np.radians(lon2)

  dlon = lon2 - lon1
  dlat = lat2 - lat1

  a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
  c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

  distance = R * c

  return R * c

def couple_height(Height_interval, Height_test1, Height_test2, indsort):

  id_height_top1    = np.where(Height_interval>Height_test1[indsort])[0]
  id_height_bottom1 = np.where(Height_interval<Height_test1[indsort])[0][::-1]
  id_height_top2    = np.where(Height_interval>Height_test2[indsort])[0]
  id_height_bottom2 = np.where(Height_interval<Height_test2[indsort])[0][::-1]
  values = [Height_interval[id_height_top1[0]], Height_interval[id_height_top2[0]] ,Height_interval[id_height_bottom1[0]], Height_interval[id_height_bottom2[0]]]

  return max(values), min(values)


def obs_height(Height_interval, Height_obs):

  id_height_top    = np.where(Height_interval>Height_obs)[0]
  id_height_bottom = np.where(Height_interval<Height_obs)[0][::-1]
  values = [Height_interval[id_height_top[0]], Height_interval[id_height_bottom[0]]]

  return max(values), min(values)

  return max(values), min(values)


def thinning(pathfileout,
             filein, 
             date0,
             date1,
             delta_distance_neighbours_m,
             delta_height_vertical_m,
             delta_distance_couple_m,
             model_lats,
             model_lons,
             timer=False):

  """ Average  a volume scan
  
  This function takes in raw measurements in an sqlite file and 
  creates an average volume scan based on the content of the 
  provided averaging structure. 

  args:
    filein        : input sqlite file with raw data
    this_datetime : vdistance_between_two_points(alid date time of radar observation 
    pathfileout   : output averaging  sqlite file 
    ray_list      : averaging template containing info for how to average PPIs
    ops_run_name  : name of operational run 
    timer         : activation of time analysis, only the first PPI in a volume scan will be averaged
    obs_percentage:

  output:
    This function outputs nothing
    However, the averaged data is put in a sqlite file with the same name
    as the original but with the suffix "_superobs" 

  """ 

  import scipy.spatial
  import domutils.radar_tools as radar_tools
  import domutils.geo_tools as geo_tools
  from collections import Counter
  import math
  import random
  import itertools


  #Prepare file in memory
  filememory=f'file:{os.path.basename(filein)}_{date0}_{date1}?mode=memory&cache=shared'
  print (f'file:{os.path.basename(filein)}_{date0}_{date1}?mode=memory&cache=shared')

  #print(f'Averaging volume scan for radar {stn} at time {hhmiss_pad} into {os.path.basename(filememory)}')
  conn_filememory = sqlite3.connect(filememory, uri=True, check_same_thread=False)
  # off the journal
  conn_filememory.execute("""PRAGMA journal_mode=OFF;""")
  # SQLite continues without syncing as soon as it has handed data off to the operating system
  conn_filememory.execute("""PRAGMA synchronous=OFF;""")

  schema = find_schema('schema')
  with open(schema) as f:
    schema = f.read( )
  conn_filememory.executescript(schema)
  conn_filein = sqlite3.connect(filein)
  result = conn_filein.execute(f"select distinct DATE, printf('%06d', TIME) from header;").fetchall()
  datetime_list  = [datetime.datetime.strptime(f'{date_time[0]}{date_time[1]}', '%Y%m%d%H%M%S') for date_time in result]
  datetime_list.sort()
  conn_filein.close()
  for this_datetime in datetime_list:
    if (this_datetime > date0) and (this_datetime <= date1):
      #zero padded string 020100
      hhmiss_pad =  this_datetime.strftime('%H%M%S') 
      #no zeros on left but still 0 if 000000
      hhmiss_nopad = str(int(hhmiss_pad))

      conn_ppi_db = make_input_db(filein,
                                      hhmiss_nopad)

      #temporarily attach ppi db to output file
      conn_filememory.execute('ATTACH DATABASE "file::memory:?cache=shared" AS conn_ppi_db') 
      order_sql = """ INSERT into header
                    SELECT
                     *
                    FROM conn_ppi_db.header;"""
      conn_filememory.execute(order_sql) 
      order_sql = """ INSERT into data
                    SELECT
                      *
                    FROM conn_ppi_db.data;"""
      conn_filememory.execute(order_sql)

      conn_filememory.commit()
      conn_filememory.execute(""" DETACH DATABASE conn_ppi_db """)

      conn_ppi_db.close()

  #kdtree for finding nearest pt
  source_xy = np.transpose(np.vstack((model_lons.ravel(),model_lats.ravel())))
  kdtree = scipy.spatial.cKDTree(source_xy, balanced_tree=False)
  c = conn_filememory.cursor()
  c.row_factory = sqlite3.Row
  query = (  f'select ID_OBS, LAT, LON, ANTENNA_ALTITUDE, CENTER_ELEVATION, CENTER_AZIMUTH, DATE, TIME, ID_STN from header ORDER BY RANDOM()  ;')
  c.execute(query)
  header_entries = c.fetchall()
  list_indices = np.array((),int)
  list_id_data = np.array((),int)
  list_id_stn  = np.array((),int)
  list_obs_lats = np.array(())
  list_obs_lons = np.array(())
  list_beamHeight = np.array(())

  list_id_data_save = np.array((),int)
  list_id_data_save_thinning = np.array((),int)
  list_id_data_remove_thinning = np.array((),int)

  
  for header_entry in header_entries:
      query = (  f'select RANGE, OMP, OMA, ID_DATA, VCOORD  from data where ( id_obs = ? ) ORDER BY RANDOM() ;')
      c.execute(query, (header_entry['ID_OBS'],))
      data_entries = c.fetchall()
      ranges = np.zeros(len(data_entries))
      id_datas = np.zeros(len(data_entries),int)
      beamHeight  = np.zeros(len(data_entries))

      id_stns  =  []
      this_elevation = header_entry['CENTER_ELEVATION']
      this_azimuth   = header_entry['CENTER_AZIMUTH']
      hrad = header_entry['ANTENNA_ALTITUDE']
      radar_lon = header_entry['LON']
      radar_lat = header_entry['LAT']
       
      for nn, data_entry in enumerate(data_entries):
         ranges[nn] = data_entry['RANGE']
         id_datas[nn] = data_entry['ID_DATA']
         beamHeight[nn] = getHfromRange(data_entry['RANGE'], hrad, this_elevation)
         id_stns = np.append( id_stns,header_entry['id_stn'])
                
      dist_earth = radar_tools.model_43(elev=this_elevation, dist_beam=ranges/1e3, hrad=hrad/1e3, want='dist_earth')
      lons, lats = geo_tools.lat_lon_range_az(radar_lon ,radar_lat, dist_earth, this_azimuth)
      #lons int the interval 0 - 360)
      lons = np.where(lons < 0., lons + 360., lons)

      #index kdtree
      dest_xy = np.transpose(np.vstack((lons, lats)))
      _, indices = kdtree.query(dest_xy, k=1)
      list_indices =  np.append(list_indices, indices)
      list_id_data  =  np.append(list_id_data, id_datas)
      list_id_stn  =  np.append(list_id_stn, id_stns)
      list_obs_lats = np.append(list_obs_lats, lats)
      list_obs_lons = np.append(list_obs_lons, lons)
      list_beamHeight = np.append(list_beamHeight, beamHeight)
  ################### share pixels ###################
  if len(list_beamHeight)>0:
   Height_interval = list(np.arange(0, int(1.3*max(list_beamHeight)), delta_height_vertical_m))
   ################################
   counts = Counter(list_indices)
   list_unique_indices =  [id for id in list_indices if counts[id] > 1]
   # It will remove the duplicates.
   list_unique_indices = np.unique(list_unique_indices) 
   id_save1  = np.array(())
   id_save2  = np.array(())
   distance = np.array(())

  # pixel share radars
   for unique_indices in list_unique_indices:
    inds = np.where(list_indices==unique_indices)
    obs1  = np.array((),int)
    obs2  = np.array((),int)
    distance_test = np.array(())
    Height_test1 = np.array(()) 
    Height_test2 = np.array(())
    if (len(Counter(list_id_stn[inds]))) > 1:
      list_beamHeight_only_one = list_beamHeight[inds[0]]
      list_id_stn_only_one = list_id_stn[inds[0]]
      list_id_data_only_one = list_id_data[inds[0]]
      for ind1 in inds[0]:
         for ind2 in inds[0]:
             if (list_id_stn[ind1] != list_id_stn[ind2]):
               lat1 = list_obs_lats[ind1]
               lon1 = list_obs_lons[ind1]
               lat2 = list_obs_lats[ind2]
               lon2 = list_obs_lons[ind2]
               dista = distance_between_two_points(lat1, lon1, lat2, lon2)
               if dista < delta_distance_couple_m:
                 distance_test = np.append(distance_test, dista)
                 obs1 = np.append( obs1,  list_id_data[ind1])   
                 obs2 = np.append( obs2,  list_id_data[ind2]) 
                 Height_test1 = np.append( Height_test1, list_beamHeight[ind1]) 
                 Height_test2 = np.append( Height_test2, list_beamHeight[ind2]) 
    indssort = np.argsort( distance_test)    
    # best couple in pixel
    for indsort in  indssort:
       
       if (obs1[indsort] in list_id_data_save) or (obs2[indsort] in list_id_data_save):
         continue
       if (obs1[indsort] in list_id_data_remove_thinning) or (obs2[indsort] in list_id_data_remove_thinning):
         continue
       if (obs1[indsort]  in list_id_data_save_thinning) or (obs2[indsort] in list_id_data_save_thinning):
         continue

       list_id_data_save = np.append(list_id_data_save,obs1[indsort])
       list_id_data_save = np.append(list_id_data_save,obs2[indsort])
       
       max_height, min_height =couple_height(Height_interval, Height_test1, Height_test2, indsort)
       indx = np.where(np.logical_and(list_beamHeight>=min_height, list_beamHeight<max_height)) 
       index = np.where(list_id_data == obs1[indsort])
       

       lat =  list_obs_lats[index[0][0]]
       lon =  list_obs_lons[index[0][0]] 
       
       # Loop  index in Height interval
       for id1  in range(0,len(indx[0])):
         ind1= indx[0][id1]
         if list_id_data[ind1] in list_id_data_remove_thinning:
           continue
         if list_id_data[ind1] in list_id_data_save:  
           continue
         if list_id_data[ind1] in list_id_data_save_thinning:
           continue
         lat_neighbor = list_obs_lats[ind1]
         lon_neighbor = list_obs_lons[ind1]   
         distance = distance_between_two_points(lat, lon, lat_neighbor, lon_neighbor)
         if distance > delta_distance_neighbours_m:
            continue
         list_id_data_remove_thinning = np.append(list_id_data_remove_thinning, list_id_data[ind1])
       



   source_xy = np.transpose(np.vstack((list_obs_lons.ravel(), list_obs_lats.ravel())))
   kdtree = scipy.spatial.cKDTree(source_xy, balanced_tree=False)
   for h in range(0,len(Height_interval)-1):
    min_height = Height_interval[h]
    max_height = Height_interval[h+1]
    indx = np.where(np.logical_and(list_beamHeight>=min_height, list_beamHeight<max_height)) 
    list_id_data_height = list_id_data[indx]
    for id_data  in list_id_data_height:
         if id_data in list_id_data_remove_thinning:
                continue
         if id_data in list_id_data_save:  
                continue
         if id_data in list_id_data_remove_thinning:
                continue
         list_id_data_save_thinning = np.append(list_id_data_save_thinning, id_data)
         index = np.where(list_id_data == id_data)[0][0]
         lats = list_obs_lats[index]
         lons = list_obs_lons[index]
         Height_obs = list_beamHeight[index]

         max_height, min_height = obs_height(Height_interval, Height_obs)
          
         dest_xy = np.transpose(np.vstack((lons, lats)))
         _ , indicess = kdtree.query(dest_xy,k=100)
        
         indicess = np.unique(indicess)
         lonlat = kdtree.data[indicess[:-1]]
         for index, lonlat in enumerate(lonlat):
             lat_neighbor = lonlat[1]
             lon_neighbor = lonlat[0]
            # distance_mx = distance_between_two_points(lats, lons, lat_neighbor, lon_neighbor) 
             distance_mx = distance_between_two_points(lats, lons, lat_neighbor, lon_neighbor)

             indx = np.where(np.logical_and( list_obs_lats == lat_neighbor,  list_obs_lons == lon_neighbor))[0][0]
             id_data_neighbor = list_id_data[indx]
             height_neighbor = list_beamHeight[indx]
             h_ref = list_beamHeight[indx]
             distance_m=math.sqrt(distance_mx**2+h_ref**2)  
             if list_id_data_height is not list_id_data:
                continue
             if id_data_neighbor  in list_id_data_remove_thinning:
                continue
             if id_data_neighbor  in list_id_data_save: 
                continue
             if distance_m > delta_distance_neighbours_m: 
                continue
             if id_data_neighbor in list_id_data_save_thinning:
                continue
             list_id_data_remove_thinning = np.append(list_id_data_remove_thinning, id_data_neighbor)
  for i in list_id_data_save:
              if not  np.where( list_id_data_remove_thinning ==i) and  np.where( list_id_data_save_thinning ==i):
                 raise ValueError('id_data_save in two list')
            #  order_sql = """UPDATE data set flag=replace(flag,0,1) where ID_DATA = ?;"""
            #  conn_filememory.execute(order_sql,(int(i),)) 
  for i in list_id_data_save_thinning:
              if not  np.where( list_id_data_remove_thinning ==i) and  np.where( list_id_data_save ==i):  
                  raise ValueError('id_data_save_thinning in two list')
            #  order_sql = """UPDATE data set flag=replace(flag,0,2) where ID_DATA = ?;"""
            #  conn_filememory.execute(order_sql,(int(i),)) 
  for i in list_id_data_remove_thinning:
               if not  np.where( list_id_data_save_thinning ==i) and  np.where( list_id_data_save ==i):  
                  raise ValueError('id_data_remove_thinning in two list')
               order_sql = """UPDATE data set flag=replace(flag,0,2048) where ID_DATA = ?;"""
               conn_filememory.execute(order_sql,(int(i),)) 

  if (list_id_data_save.size+list_id_data_remove_thinning.size+list_id_data_save_thinning.size)!=list_id_data.size:
    print (list_id_data_save.size+list_id_data_remove_thinning.size+list_id_data_save_thinning.size)
    print (list_id_data.size)
    raise ValueError('id_data save in at least two list')

  conn_filememory.commit()
  try:
      combine(pathfileout, filememory)
  except sqlite3.Error as error:
    print("Error while creating a single sqlite file:  {os.path.basename(filememory)}", error)
  # close connection 
  conn_filememory.close()

def find_sample_entry(src_dir, file_type, variable=None, prefix=None):
    """find first entry of a given variable in a given directory
    """

    from pathlib import Path
    import domcmc.fst_tools as fst_tools

    if prefix is None:
        prefix = '2*'

    found = False
    if file_type == 'fst':
        file_list = sorted(Path(src_dir).glob(prefix))
        file_list = sorted(Path(src_dir).glob(prefix))
        file_list = sorted(Path(src_dir).glob(prefix))
        for this_file in file_list:
            if this_file.is_file():
                out_dict = fst_tools.get_data(str(this_file), var_name=variable, latlon=True )
                if out_dict is not None:
                    found = True
                    break

    else:
        raise ValueError('filetype not supported')

    if not found:
        raise ValueError(f'sample file not found in {src_dir}')

    return out_dict

def combine(pathfileout, filememory):
 
   
  """ Creating a single sqlite file from multiple sqlite files
 
  args:
    pathfileout   : output averaging  sqlite file 
    filememory    : name of the sqlite file in memory to copy
  output:
    Nothing
    A sqlite file is made with all averaged volume scans
  """

  # write in output averaging  sqlite file 
  conn_pathfileout = sqlite3.connect(pathfileout, uri=True, isolation_level=None, timeout=999)
  # off the journal
  conn_pathfileout.execute("""PRAGMA journal_mode=OFF;""")
  # SQLite continues without syncing as soon as it has handed data off to the operating system
  conn_pathfileout.execute("""PRAGMA synchronous=OFF;""")
  # Wait to read and write until the next process finishes
  # attach the sqlite file in memory for one PPI
  conn_pathfileout.execute("ATTACH DATABASE ? AS this_avg_db;", (filememory,))
  order_sql = """ INSERT into header
                    SELECT
                     *
                    FROM  this_avg_db.header;"""
  conn_pathfileout.execute(order_sql) 
  order_sql = """ INSERT into data
                    SELECT
                      *
                    FROM  this_avg_db.data;"""
  conn_pathfileout.execute(order_sql)

  conn_pathfileout.commit()
  conn_pathfileout.execute(""" DETACH DATABASE this_avg_db """)


def collision_test(conn_pathfileout):
   
   """Check the collisiona and that the id_obs from the header have an associated properly to id_data.
 
   args:
    conn_pathfileout   : connection of  output averaging  sqlite file 
   output:
    Nothing

   """
   # distinct id_obs from header
   # count id_obs from header
   order_sql = """select 
                    count(distinct id_obs)
                  from header;"""
   cursor   = conn_pathfileout.cursor()

   cursor.execute(order_sql)
   result   = cursor.fetchone()
   distinct_id_obs_from_header = result[0]
   order_sql = """select 
                    count(id_obs)
                  from header;"""
   cursor   = conn_pathfileout.cursor()
   cursor.execute(order_sql)
   result   = cursor.fetchone()
   count_id_obs_from_header = result[0]
   
   # distinct id_obs from data
   # distinct id_data from data
   # count id_data from data
   order_sql = """select 
                    count(distinct id_obs)
                  from data;"""
   cursor   = conn_pathfileout.cursor()
   cursor.execute(order_sql)
   result   = cursor.fetchone()
   distinct_id_obs_from_data = result[0]
   order_sql = """select 
                    count(distinct id_data)
                  from data;"""
   cursor   = conn_pathfileout.cursor()
   cursor.execute(order_sql)
   result   = cursor.fetchone()

   distinct_id_data_from_data = result[0]
   order_sql = """select 
                    count(id_data)
                  from data;"""
   cursor   = conn_pathfileout.cursor()
   cursor.execute(order_sql)
   result   = cursor.fetchone()
   count_id_data_from_data = result[0]


   if (distinct_id_obs_from_header !=  distinct_id_obs_from_data): 
      raise RuntimeError("""Error: id_obs is not associated properly""")
   if (distinct_id_obs_from_header !=  count_id_obs_from_header): 
      raise RuntimeError("""Error: id_obs is in collision""")
   if (distinct_id_data_from_data  !=  count_id_data_from_data): 
      raise RuntimeError("""Error: id_data is in collision""")

def compute_thinning(center_time,
         window_width,
         infile_list, 
         pathout, 
         outfile_struc, 
         timing, 
         n_cpus,
         delta_time_thinning_min,
         delta_distance_neighbours_m,
         delta_height_vertical_m,
         delta_distance_couple_m,
         pathin_model):

  """launch computation of average volums scans, possibly in parallel

  args:
    center_time  : datetime object,  center time of the assimilation window
    window_width : [hours] Width of the assimilation window
    desired_radar_list : list of radars to process
    infile_list  : list of input files to be superobbed
    pathout      : output average sqlite file(s) 
    outfile_struc: structure of output file name ; will be passed to strftime
    timing       : activation of time analysis, only the first PPI in a volume scan will be averaged
    ops_run_name : name of operational run 
    n_rays       : number of rays
    delta_range  : delta range of the boxes
    n_cpus       : number of cpus for parallel execution, with n_cpus=1 joba are launched sequentially and dask is not invoked 
    obs_percentage : percentage of observation in the box to average
    obs_nyquist : Nyquist for QC
  output:
    Nothing
    Average sqlite file(s) are created with the '_thin' suffix

  """
  #start and stop time of assimilation window

  
  infile_combine =  f'combine_{center_time.strftime(outfile_struc)}'
  if os.path.isfile(infile_combine):
    os.remove(infile_combine)

  con_infile_combine = sqlite3.connect(infile_combine)
  con_infile_combine.execute("pragma temp_store = 2;")
  schema = find_schema('schema')
  with open(schema) as f:
    schema = f.read()
  con_infile_combine.executescript(schema)
  print (infile_list)
  for infile in infile_list:
    combine(infile_combine, infile)
    print (infile)
 # create info and resume_tables in fileout
  create_info_midas_tables(infile, con_infile_combine)  
  con_infile_combine.close()
   
  window_t0 = center_time - datetime.timedelta(seconds=3600*window_width/2.)
  window_tf = center_time + datetime.timedelta(seconds=3600*window_width/2.)
  vol_scan_list = []
  while window_t0 < window_tf :
     window_t1 = window_t0 + datetime.timedelta(minutes=delta_time_thinning_min)
     vol_scan_list.append( {'file':infile_combine, 'date0':window_t0, 'date1':window_t1 } )
     window_t0 = window_t1 
  ################
  #flush fileout if it already exists
  pathfileout=f"{pathout}/{center_time.strftime(outfile_struc)}"
  
  if os.path.isfile(pathfileout):
    os.remove(pathfileout)

  #init large output file
  conn_pathfileout = sqlite3.connect(pathfileout)
  conn_pathfileout.execute("pragma temp_store = 2;")
  schema = find_schema('schema')
  with open(schema) as f:
    schema = f.read()
  conn_pathfileout.executescript(schema)
  # using maestro_archives/
  # setup projection object
  model_dat  = find_sample_entry(pathin_model, 'fst', variable='UU', prefix=None) 
  model_lats = model_dat['lat']
  model_lons = model_dat['lon']
  if len(vol_scan_list) == 0:
    raise RuntimeError('List of volume scan to process is empty. Check that files are available and search criteria are correct.')
  tc_0 = time.time()
  if timing :
    print ("Compute only one PPI ")
    thinning(pathfileout, vol_scan_list[0]['file'], vol_scan_list[0]['date0'], vol_scan_list[0]['date1'], delta_distance_neighbours_m, delta_height_vertical_m, delta_distance_couple_m, model_lats, model_lons, timer=True)
    tc_1 = time.time()
  else:
    if n_cpus == 1:
      #serial execution, usefull for debugging
      print('Serial execution')
      for vscan in vol_scan_list:
        thinning(pathfileout, vscan['file'] , vscan['date0'], vscan['date1'], delta_distance_neighbours_m, delta_height_vertical_m, delta_distance_couple_m, model_lats, model_lons)
    else:
      print(f'Compute {len(vol_scan_list)} volume scans in parallel')
      with tempfile.TemporaryDirectory() as tmpdir:
        #the directory dask-worker-space/ will be in tmpdir
        with dask.distributed.Client(processes=True, threads_per_worker=1, 
                                     n_workers=n_cpus, 
                                     local_directory=tmpdir, 
                                     silence_logs=40) as client:

          #delay data 
          model_lons = client.scatter(model_lons)
          model_lats = client.scatter(model_lats)
          joblist = [delayed(thinning)( pathfileout, vscan['file'], vscan['date0'], vscan['date1'], delta_distance_neighbours_m, delta_height_vertical_m, delta_distance_couple_m, model_lats, model_lons) for vscan in vol_scan_list]
          dask.compute(joblist)
   
    sample_file  = vol_scan_list[0]['file']
    # create info and resume_tables in fileout
    create_info_midas_tables(sample_file, conn_pathfileout)   
    # improve searches with index tables
    create_index_tables_idobs_iddata(conn_pathfileout)
    # collision_test
    collision_test(conn_pathfileout)
    # close connection
    conn_pathfileout.close()
    tc_1 = time.time()
   
  print(f"Runtime total: {round(tc_1-tc_0,4)} s")

def arg_call():
    import argparse 

    parser = argparse.ArgumentParser()
    parser.add_argument('--center_time',  default='undefined', type=str,   help="YYYYMMDDHH center time of assimilation window")
    parser.add_argument('--window_width', default=0.,          type=float, help="[hours] width of assimilation window")
    parser.add_argument('--inputfiles', nargs="+", default='undefined',    help="input sqlite file to average")
    parser.add_argument('--pathin',       default='undefined', type=str,   help="directory where are input sqlite files")
    parser.add_argument('--infile_struc', default='/%Y%m%d%H_ra',type=str,help="structure of input file name")
    parser.add_argument('--pathout',      default=os.getcwd(), type=str,   help="where averaged sqlite files will be put")
    parser.add_argument('--outfile_struc',default='%Y%m%d%H_superobbed_dvel_ground_radars.sqlite', type=str,   help="structure of output file name")
    parser.add_argument('--timing',       action="store_true",             help="Average only one PPI for time analysis" ) 
    parser.add_argument('--n_cpus',       default=1,           type=int,   help="Number of rays for averaging" )
    parser.add_argument('--delta_time_thinning_min',   default=10,         type=float, help="window_width to average (min)" )
    parser.add_argument('--delta_distance_neighbours_m', default=30000,        type=float, help="min distance neighbours (m)" )
    parser.add_argument('--pathin_model',       default='undefined', type=str,   help="directory where are input model file")
    parser.add_argument('--delta_height_vertical_m', default=1000,         type=int, help="window_width to average (min)" )
    parser.add_argument('--delta_distance_couple_m',   default=1000,         type=int, help="window_width to average (min)" )



    args = parser.parse_args()

    if args.inputfiles == 'undefined' and args.pathin == 'undefined':

      args.center_time = '2019062706'
      args.window_width = 6.
      #option1: explicitely specify inputfiles
      #args.inputfiles = ['/space/hall4/sitestore/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.3/sqlite_v1.0.0_qc/split_6h/USVNX/2019073100_ra',
      #                   '/space/hall4/sitestore/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.3/sqlite_v1.0.0_qc/split_6h/CASRA/2019073100_ra']
      #option2: specify pathin + infile_struc and let Python search for files
      args.pathin = '/fs/site6/eccc/cmd/a/dlo001/data/doppler_qc/doppler_qc_v0.4/sqlite_v1.0.0_qc/split_6h/'
      args.pathout = './work'
      args.timing = False
      args.plot   = False
      args.n_cpus = 80

      print(f'superobs called with no input filename(s)')
      print(f'We are running demo with:')
    for arg in vars(args):
      print(f'--{arg}  {getattr(args, arg)}')
    if args.center_time == 'undefined':
        raise ValueError('Center time of assimilation window must be provided')
    else:
       args.center_time = datetime.datetime.strptime(args.center_time, '%Y%m%d%H')

    if np.isclose(args.window_width, 0.) :
        raise ValueError('Window width must be provided')
    if args.pathin_model != 'undefined':
      #if inputfiles argument is provided, we use that
      infile_list = args.inputfiles 

    if args.inputfiles != 'undefined':
      #if inputfiles argument is provided, we use that
      infile_list = args.inputfiles 

    elif args.pathin != 'undefined': 
      #alternatively, search for files with pathin+infile_struc 
      if not os.path.isdir(args.pathin):
        raise ValueError(f'pathin: {args.pathin} does not exist.')
      search_str = args.center_time.strftime(args.infile_struc)
      infile_list = glob.glob(f'{args.pathin}/{search_str}*')
    else:
      raise ValueError('At least one of inputfiles ot pathin must be provided')

    #check infile_list
    if len(infile_list) == 0:
      raise ValueError('infile_list is empty, we stop here')
      sys.exit(1)

    else:
      for this_file in infile_list:
        if not os.path.isfile(this_file):
          raise ValueError(f'inputfiles: {this_file} does not exist.')

    if not os.path.isdir(args.pathout):
      os.mkdir(args.pathout)
    #sys.exit is used to the return status of main is catched and passed to caller
    sys.exit(compute_thinning(args.center_time,
                  args.window_width,
                  infile_list, 
                  args.pathout, 
                  args.outfile_struc, 
                  args.timing, 
                  args.n_cpus,
                  args.delta_time_thinning_min,
                  args.delta_distance_neighbours_m,
                  args.delta_height_vertical_m,
                  args.delta_distance_couple_m,
                  args.pathin_model))

if __name__ == '__main__':
    arg_call()
