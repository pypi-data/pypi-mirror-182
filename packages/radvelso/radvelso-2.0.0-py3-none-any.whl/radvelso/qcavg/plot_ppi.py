import numpy as np
import os, inspect
import domutils.radar_tools as radar_tools
import sys
import datetime
from datetime import datetime, timedelta
import domutils.legs as legs
import domutils.geo_tools   as geo_tools
import domutils.radar_tools as radar_tools
import sys
import copy
import numpy as np
import domcmc.fst_tools as fst_tools
import xarray as xr
from scipy.interpolate import LinearNDInterpolator
from unravel import find_reference
from unravel.core import Dealias as DealiasBase


def radar_ax_circ(ax, radar_lat, radar_lon):
    '''plot azimuth lines and range circles around a given radar
    '''
    import numpy as np
    import cartopy.crs as ccrs
    import domutils.geo_tools as geo_tools

    #cartopy transform for latlons
    proj_pc = ccrs.PlateCarree()

    color=(100./256.,100./256.,100./256.)

    #add a few azimuths lines
    az_lines = np.arange(0,360.,90.)
    ranges   = np.arange(250.)
    for this_azimuth in az_lines:
        lons, lats = geo_tools.lat_lon_range_az(radar_lon, radar_lat, ranges, this_azimuth)
        ax.plot(lons, lats, transform=proj_pc, c=color, zorder=300, linewidth=.3)

    #add a few range circles
    ranges   = np.arange(0,250.,100.)
    azimuths = np.arange(0,361.)#360 degree will be included for full circles
    for this_range in ranges:
        lons, lats = geo_tools.lat_lon_range_az(radar_lon, radar_lat, this_range, azimuths)
        ax.plot(lons, lats, transform=proj_pc, c=color, zorder=300, linewidth=.3)


def plotss(A,nameA,B,nameB,C,nameC,D,nameD,lat_0, lon_0,ppi_latitudes,ppi_longitudes):
  import os, inspect
  import copy
  import numpy as np
  import matplotlib as mpl
  import matplotlib.pyplot as plt
  import cartopy.crs as ccrs

    # imports from domutils
  import domutils.legs as legs
  import domutils.geo_tools   as geo_tools
  import domutils.radar_tools as radar_tools
  import sys
    #missing values ane the associated color
  missing  = -9999.
  missing_color = 'grey_160'
  undetect = -3333.
  undetect_color = 'grey_160'

#  A=[]
#  B=[]
#  C=[]
#  D=[]
  #pixel density of panels in figure
  ratio = 1.
  hpix = 800.       #number of horizontal pixels E-W
  vpix = ratio*hpix #number of vertical pixels   S-N
  img_res = (int(hpix),int(vpix))
 
  #cartopy Rotated Pole projection
  pole_latitude=90.
  pole_longitude=0.
  proj_rp = ccrs.RotatedPole(pole_latitude=pole_latitude, pole_longitude=pole_longitude)
  #plate carree
  proj_pc = ccrs.PlateCarree()
  #a smaller domain for a closeup that will be inlaid in figure
#  lat_0 = 45.7063
  delta_lat = 2.18
#  lon_0 = -73.85
  delta_lon = 3.12
  map_extent=[lon_0-delta_lon, lon_0+delta_lon, lat_0-delta_lat, lat_0+delta_lat]
  #a circular clipping mask for the closeup axes
  x = np.linspace(-1., 1, int(hpix))
  y = np.linspace(-1., 1, int(vpix))
  xx, yy = np.meshgrid(x, y, indexing='ij')
  clip_alpha = np.where( np.sqrt(xx**2.+yy**2.) < 1., 1., 0. )
  #a circular line around the center of the closeup window
  radius=8. #km
  azimuths = np.arange(0,361.)#360 degree will be included for full circles
  print (lon_0, lat_0)
  print ("22222")

  closeup_lons, closeup_lats = geo_tools.lat_lon_range_az(lon_0, lat_0, radius, azimuths)
  #a line 5km long for showing scale in closeup insert
  azimuth = 90 #meteorological angle
  print ("33333")

  distance = np.linspace(0,5.,50)#360 degree will be included for full circles
  scale_lons, scale_lats = geo_tools.lat_lon_range_az(lon_0, lat_0, distance, azimuth)
  print ("11111")
  #point density for figure
  mpl.rcParams['figure.dpi'] = 100.   #crank this up for high def images
  # Use this for editable text in svg (eg with Inkscape)
  mpl.rcParams['text.usetex']  = False
  mpl.rcParams['svg.fonttype'] = 'none'
  #larger characters
  mpl.rcParams.update({'font.size': 25})
  # dimensions for figure panels and spaces
  # all sizes are inches for consistency with matplotlib
  fig_w = 13.5           # Width of figure
  fig_h = 12.5           # Height of figure
  rec_w = 5.             # Horizontal size of a panel
  rec_h = ratio * rec_w  # Vertical size of a panel
  sp_w = .5              # horizontal space between panels
  sp_h = .8              # vertical space between panels
  fig = plt.figure(figsize=(fig_w,fig_h))
  xp = .0               #coords of title (axes normalized coordinates)
  yp = 1.0
  #coords for the closeup  that is overlayed
  x0 = .55               #x-coord of bottom left position of closeup (axes coords)
  y0 = .55               #y-coord of bottom left position of closeup (axes coords)
  dx = .4                #x-size of closeup axes (fraction of a "regular" panel)
  dy = .4                #y-size of closeup axes (fraction of a "regular" panel)
  #normalize sizes to obtain figure coordinates (0-1 both horizontally and vertically)
  rec_w = rec_w / fig_w
  rec_h = rec_h / fig_h
  sp_w  = sp_w  / fig_w
  sp_h  = sp_h  / fig_h
  #instantiate objects to handle geographical projection of data
  print ('7777777777')
  proj_inds = geo_tools.ProjInds(src_lon=ppi_longitudes, src_lat=ppi_latitudes,
                                   extent=map_extent,  dest_crs=proj_rp,
                                   extend_x=False, extend_y=True,
                                   image_res=img_res,  missing=missing)
  print ('111117777777777')

  #Reflectivity
  #
  #axes for this plot
  print ("A")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  pos = [sp_w, sp_h+(sp_h+rec_h), rec_w, rec_h]
  ax = fig.add_axes(pos, projection=proj_rp)
  ax.set_extent(map_extent)
  ax.set_aspect('auto')

  ax.annotate(f'{nameA}', size=30,
                xy=(xp, yp), xycoords='axes fraction')


#  fig.suptitle(f'{A}')
 # colormapping object for reflectivity
  brown_purple=[[ 45,  0, 75],
                  [ 84, 39,136],
                  [128,115,172],
                  [178,171,210],
                  [216,218,235],
                  [247,247,247],
                  [254,224,182],
                  [253,184, 99],
                  [224,130, 20],
                  [179, 88,  6],
                  [127, 59,  8]]
  range_arr = [-48.,-40.,-30.,-20,-10.,-1.,1.,10.,20.,30.,40.,48.]
 
  map_dvel = legs.PalObj(range_arr=range_arr,
                                   color_arr=brown_purple,
                                   solid='supplied',
                                   excep_val=[missing,       undetect],
                                   excep_col=[missing_color, undetect_color])

  ##geographical projection of data into axes space
  #  #  #  #
  #  #  #  #
  proj_data = proj_inds.project_data(A)
  #plot data & palette
  map_dvel.plot_data(ax=ax, data=proj_data, zorder=0,
                            palette='right',
                            pal_units='[dBZ]', pal_format='{:3.0f}')

  #add political boundaries
  add_feature(ax)
 
  #radar circles and azimuths
  radar_ax_circ(ax, lat_0,lon_0)
  closeup_rgb = map_dvel.to_rgb(proj_data)
  rgba = np.concatenate([closeup_rgb/255.,clip_alpha[...,np.newaxis]], axis=2)
  ##uncomment to save figure


  #Quality Controlled Doppler velocity
  #
  #axes for this plot
  print ("B")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  pos = [sp_w+(sp_w+rec_w+1./fig_w), sp_h+(sp_h+rec_h), rec_w, rec_h]
  ax = fig.add_axes(pos, projection=proj_rp)
  ax.set_extent(map_extent)
  ax.set_aspect('auto')

  ax.annotate(f'{nameB}', size=30,
                xy=(xp, yp), xycoords='axes fraction')

  #from https://colorbrewer2.org
  brown_purple=[[ 45,  0, 75],
               [ 84, 39,136],
               [128,115,172],
               [178,171,210],
               [216,218,235],
               [247,247,247],
               [254,224,182],
               [253,184, 99],
               [224,130, 20],
               [179, 88,  6],
               [127, 59,  8]]
  range_arr = [-48.,-40.,-30.,-20,-10.,-1.,1.,10.,20.,30.,40.,48.]
  map_dvel = legs.PalObj(range_arr=range_arr,
                           color_arr = brown_purple,
                           solid='supplied',
                           excep_val=[missing, undetect],
                           excep_col=[missing_color, undetect_color])

  #geographical projection of data into axes space
  #  #  #  #
  #  #  #  #
  proj_data = proj_inds.project_data(B)
  #plot data & palette
  map_dvel.plot_data(ax=ax,data=proj_data, zorder=0,
                   palette='right', pal_units='[m/s]', pal_format='{:3.0f}')   #palette options

  #add political boundaries
  add_feature(ax)

  #radar circles and azimuths
  radar_ax_circ(ax, lat_0, lon_0)

  #circle indicating closeup area
  # ax.plot(closeup_lons, closeup_lats, transform=proj_pc, c=(0.,0.,0.), zorder=300, linewidth=.8)

  #arrow pointing to closeup
  # ax.annotate("", xy=(0.33, 0.67), xytext=(.55, .74),  xycoords='axes fraction',
  #            arrowprops=dict(arrowstyle="<-"))
  print ("C")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  pos = [sp_w, sp_h, rec_w, rec_h]
  ax = fig.add_axes(pos, projection=proj_rp)
  ax.set_extent(map_extent)
  ax.set_aspect('auto')

  ax.annotate(f'{nameC}', size=30,
                xy=(xp, yp), xycoords='axes fraction')

  #from https://colorbrewer2.org
  brown_purple=[[ 45,  0, 75],
                [ 84, 39,136],
                [128,115,172],
                [178,171,210],
                [216,218,235],
                [247,247,247],
                [254,224,182],
                [253,184, 99],
                [224,130, 20],
                [179, 88,  6],
                [127, 59,  8]]
  range_arr = [-48.,-40.,-30.,-20,-10.,-1.,1.,10.,20.,30.,40.,48.]
  map_dvel  = legs.PalObj(range_arr=range_arr,
                           color_arr = brown_purple,
                           solid='supplied',
                           excep_val=[missing, undetect],
                           excep_col=[missing_color, undetect_color])


  #geographical projection of data into axes space
  #  #  #  #
  #  #  #  #

  proj_data = proj_inds.project_data(C)
 #plot data & palette
  map_dvel.plot_data(ax=ax,data=proj_data, zorder=0,
                    palette='right', pal_units='[m/s]', pal_format='{:3.0f}')   #palette options

  #add political boundaries
  add_feature(ax)

  #radar circles and azimuths
  radar_ax_circ(ax, lat_0, lon_0)

    #circle indicating closeup area
   # ax.plot(closeup_lons, closeup_lats, transform=proj_pc, c=(0.,0.,0.), zorder=300, linewidth=.8)

    #arrow pointing to closeup
    # ax.annotate("", xy=(0.33, 0.67), xytext=(.55, .74),  xycoords='axes fraction',
    #            arrowprops=dict(arrowstyle="<-"))
  print ("D")
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  pos = [sp_w+(sp_w+rec_w+1./fig_w), sp_h, rec_w, rec_h]
  ax = fig.add_axes(pos, projection=proj_rp)
  ax.set_extent(map_extent)
  ax.set_aspect('auto')
  ax.annotate(f'{nameD}', size=30,
                xy=(xp, yp), xycoords='axes fraction')

  #from https://colorbrewer2.org
  brown_purple=[[ 45,  0, 75],
                [ 84, 39,136],
                [128,115,172],
                [178,171,210],
                [216,218,235],
                [247,247,247],
                [254,224,182],
                [253,184, 99],
                [224,130, 20],
                [179, 88,  6],
                [127, 59,  8]]
  range_arr = [-48.,-40.,-30.,-20,-10.,-1.,1.,10.,20.,30.,40.,48.]
  map_dvel  = legs.PalObj(range_arr=range_arr,
                           color_arr = brown_purple,
                           solid='supplied',
                           excep_val=[missing, undetect],
                           excep_col=[missing_color, undetect_color])


  #geographical projection of data into axes space
  #  #  #  #
  #  #  #  #

  proj_data = proj_inds.project_data(D)
  #plot data & palette
  map_dvel.plot_data(ax=ax,data=proj_data, zorder=0,
                   palette='right', pal_units='[m/s]', pal_format='{:3.0f}')   #palette options

  #add political boundaries
  add_feature(ax)

  #radar circles and azimuths
  radar_ax_circ(ax, lat_0, lon_0)

  #circle indicating closeup area
  # ax.plot(closeup_lons, closeup_lats, transform=proj_pc, c=(0.,0.,0.), zorder=300, linewidth=.8)

  #arrow pointing to closeup
  # ax.annotate("", xy=(0.33, 0.67), xytext=(.55, .74),  xycoords='axes fraction',
  #            arrowprops=dict(arrowstyle="<-"))
  plt.savefig(f'radar_ppi_.png')
#  print ('savefig_end')

# python example.py 2019062100_ra 'casbv' 0.4 '20190620210600' 47.8709983825684

def add_feature(ax):
    """plot geographical and political boundaries in matplotlib axes
    """
    import cartopy.feature as cfeature
    ax.add_feature(cfeature.STATES.with_scale('10m'), linewidth=0.1, edgecolor='0.1',zorder=1)

def radar_ax_circ(ax, radar_lat, radar_lon):
    '''plot azimuth lines and range circles around a given radar
    '''
    import numpy as np
    import cartopy.crs as ccrs
    import domutils.geo_tools as geo_tools

    #cartopy transform for latlons
    proj_pc = ccrs.PlateCarree()

    color=(100./256.,100./256.,100./256.)

    #add a few azimuths lines
    az_lines = np.arange(0,360.,90.)
    ranges   = np.arange(250.)
    for this_azimuth in az_lines:
        lons, lats = geo_tools.lat_lon_range_az(radar_lon, radar_lat, ranges, this_azimuth)
        ax.plot(lons, lats, transform=proj_pc, c=color, zorder=300, linewidth=.3)

    #add a few range circles
    ranges   = np.arange(0,250.,100.)
    azimuths = np.arange(0,361.)#360 degree will be included for full circles
    for this_range in ranges:
        lons, lats = geo_tools.lat_lon_range_az(radar_lon, radar_lat, this_range, azimuths)
        ax.plot(lons, lats, transform=proj_pc, c=color, zorder=300, linewidth=.3)




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
  filein =filein
  print ('filess',filein)
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



