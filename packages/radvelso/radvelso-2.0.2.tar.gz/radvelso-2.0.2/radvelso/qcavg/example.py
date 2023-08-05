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

class Dealias(DealiasBase):
    """
    Dealiasing class.
    """

    def __init__(
        self, ppi_ranges, ppi_azimuths, ppi_elevation, ppi_velocity, nyquist, alpha=0.6
    ):
        """
        Constructor.

        Parameters
        ----------
        ppi_ranges: array[bins]
            PPI's bins range in meters.
        ppi_azimuths: array[rays]
            PPI's rays angle in degrees.
        ppi_elevation: float
            PPI elevation angle in degrees.
        ppi_velocity: array[rays, bins]
            Dopple velocity.
        nyquist: float
            PPI nyquist velocity.
        alpha: float
            Coefficient for which the nyquist velocity periodicity range is
            considered valid.
        """

  #      self.ppi_ranges    = ppi_ranges
  #      self.ppi_azimuths  = ppi_azimuths 
  #      self.ppi_elevation = ppi_elevation
  #      self.ppi_velocity  = ppi_velocity
  #      self.nyquist       = nyquist
  #      self.alpha         = alpha
        super().__init__(
            ppi_ranges,
            ppi_azimuths,
            ppi_elevation,
            ppi_velocity.copy(),
            nyquist,
            alpha=alpha,
        )
        self._initialized = False

    def initialize(
        self, model_dop_velocity, beta=0.25, missing=-9999.0, undetect=-3333.0
    ):
        """
        Initialize the dealiasing finding the radials of reference.

        1. Consider as "reference velocities" dealiased velocities close to the model's doppler velocity.
           This step is an initial dealiasing that helps the sbsequent dealiasing steps.
        2. Find reference radials (section 3.a.2, Leuf et al, 2020).

        Notes
        -----
        Louf, V., Protat, A., Jackson, R. C., Collis, S. M., & Helmus, J. (2020).
        UNRAVEL: A Robust Modular Velocity Dealiasing Technique for Doppler Radar,
        Journal of Atmospheric and Oceanic Technology, 37(5), 741-758. Retrieved Mar 2, 2022.
        https://journals.ametsoc.org/view/journals/atot/37/5/jtech-d-19-0020.1.xml
        """

        model_dop_velocity = model_dop_velocity.copy()

        # Prepare the data
        invalid = (self.velocity == missing) | (self.velocity == undetect)
        valid = ~invalid
        self.velocity[invalid] = np.nan
        self.dealias_vel = self.velocity.copy()

        #####################################
        # Initial dealiasing using model data
        #print (invalid)
        model_dop_velocity[invalid] = missing
        self.velocity[invalid] = missing

        # Find reference velocities close to the model_velocity (reference)
        # 1. Generate velocity candidates at +/- 2*Ny*i intervals.
        vel_candidates = []
        for i in range(-3, 4):
            vel_candidates.append(self.velocity + 2 * i * self.nyquist)
        vel_candidates = np.stack(vel_candidates, axis=-1)

        # 2. Keep the closest one to the model_velocity (reference)
        sorting_idx = np.argsort(
            np.abs(vel_candidates - model_dop_velocity[:, :, None]), axis=2
        )[:, :, 0].squeeze()
        xi, yi = np.meshgrid(
            range(sorting_idx.shape[0]), range(sorting_idx.shape[1]), indexing="ij"
        )
        vel_candidate = vel_candidates[xi, yi, sorting_idx]

        # 3. Check if the candidate is |Vcand-Vobs|< beta*Vny
        #    If True, accept that that candidate.

        # Check is the candidate is equal to the original velocity.
        # not_modified = np.abs(vel_candidate - self.velocity) < 0.0001
        vel_diff = np.abs(vel_candidate - model_dop_velocity)
        accepted_candidates = vel_diff < beta * self.nyquist  # & (~not_modified)

        # not_modified = not_modified & valid
        model_valid = (model_dop_velocity != missing) & (model_dop_velocity != undetect)
        accepted_candidates = accepted_candidates & valid & model_valid

        if np.count_nonzero(accepted_candidates.size > 0):
            self.dealias_vel[accepted_candidates] = vel_candidate[accepted_candidates]
            self.flag[accepted_candidates] = 2  # Dealiased
            # self.flag[not_modified] = 0  # Consider as unprocessed.

            # NOTE: Once a velocity has been flagged 1 or 2, it is not modified anymore by
            # subsequent steps.

        self.dealias_vel[invalid] = np.nan
        self.flag[invalid] = -1

        ########################
        # Find reference radials
        start_beam, end_beam = find_reference.find_reference_radials(
            self.azimuth, self.dealias_vel
        )

        azi_start_pos = np.argmin(np.abs(self.azimuth - start_beam))
        azi_end_pos = np.argmin(np.abs(self.azimuth - end_beam))

        self.azi_start_pos = azi_start_pos
        self.azi_end_pos = azi_end_pos

        self._initialized = True

    def dealiase(self):
        """
        Dealise the doppler velocity.

        Dealiasing flags:
        -3: Missing values
        0: Unprocessed. This velocity could not be dealiased.
        1: Processed and unchanged value
        2: Processed and dealiased value.
        """
        if not self._initialized:
            raise RuntimeError(
                "The dealiasing object was not initialized.\n"
                "Run the initialize(*args,**kwargs) method first."
            )

        for window in [6, 12, 24]:
            self.correct_range(window)
            self.correct_clock(window)
            if self.check_completed():
                break

        if not self.check_completed():
            for window in [(5, 5), (10, 10), (20, 20), (40, 40)]:
                self.correct_box(window)
                if self.check_completed():
                    break

        self.correct_closest()
        self.flag[self.flag > 2] = 2

        # self.check_box(window_size=(15, 10))
        # self.flag[self.flag > 2] = 0



def round_date2hour(reference_date, which="closest"):
    """
    Round the date to the nearest hour (which="closest")
    the begining of the hour (which="floor"),
    or the immediately next hour (which="ceil") .
    """
    # round_off: 0 closest to beggining of the hour. 1 Closest to the end.
    round_off = timedelta(hours=reference_date.minute // 30)
    model_init_floor = reference_date.replace(minute=0, second=0, microsecond=0)

    which = which.lower()
    if which not in ("floor", "closest", "ceil"):
        raise ValueError(f"which={which} unsupported.")

    if which == "floor":
        return model_init_floor
    elif which == "ceil":
        model_init_ceil = model_init_floor + timedelta(hours=1)
        return model_init_ceil
    else:  # closest
        model_init_closest = model_init_floor + round_off
        return model_init_closest

def find_model_init(reference_date, init_interval=6, which="closest", ext=""):
    """
    Find the closest model initialization time to a given date.
    The corresponding forecast hour is also returned.

    Parameters
    ----------
    reference_date: datetime
        Input date.
    init_interval: int
        Model initialization interval in hours.
    which: str
        Which date to find. "closest", "floor", "ceil"

    Returns
    -------
    model_init: datetime
        Model initialization time
    fcst_hours: int
        Forecast hour
    filename: str
        File name of the model output file (standard file format).

    Notes
    -----
    The actual forecast time can be computed as:
    model_init + timedelta(hours=fcst_hours)
    """
    model_time = round_date2hour(reference_date, which=which)
    fcst_hours = model_time.hour % init_interval
    model_init = model_time - timedelta(hours=model_time.hour % init_interval)

    model_init_timestamp = model_init.strftime("%Y%m%d%H")
    file_name = f"{model_init_timestamp}_{fcst_hours:03d}{ext}"

    return model_init, fcst_hours, file_name

def find_fcst_file(
    reference_time, model_data_dir, subdir_fmt="", ext="", which="closest"
):
    """
    Find the module output in the archive that is the closest to given date.

    Returns
    -------

    model_filename: str
        The path to the model output file closest to the desired date.
    """
    model_init, _, model_filename = find_model_init(
        reference_time, which=which, ext=ext
    )

    model_filename_candidates = [
        os.path.join(model_data_dir, model_filename),
        os.path.join(model_data_dir, model_init.strftime(subdir_fmt), model_filename),
    ]
    model_filename = [f for f in model_filename_candidates if os.path.isfile(f)]

    if len(model_filename) == 0:
        print("No model data found at:")
        print(model_filename_candidates[0])
        print(model_filename_candidates[1])
        return

    return model_filename[0]



def model_data_over_radar(
    scan, model_data_dir, max_range=250, interp="linear", min_delta=10
):
    """
    Return a DataFrame with the model data closest to the scan time.
    The data is clipped to the radar domain.

    Parameters
    ----------
    scan: PolarScan
        Input polar scan.
    model_data_dir: str
        Directory where the model data is stored in Netcdf format.
    max_range: float
        Maximum radar range used to trim the model output the
        radar domain.
    interp: str
        Time interpolation method: "linear" or "nearest".
        If `method="linear"` the model data is interpolated in time at the scan time.
    min_delta: float
        Minimum time delta in minutes to consider a model time "close enough" to the
        scan time. If the time difference is less than min_delta, the time interpolation
        is ignored and the closet model time is used.

    Returns
    -------
    model_ds: DataFrame
        Dataframe with the model data.
    """
    # 1.1 Get the closest model date
   # scan_datetime = datetime.strptime(scan.startdate + scan.starttime, "%Y%m%d%H%M%S")
    scan_datetime = scan
    if interp == "linear":
        closest_model_time_floor = round_date2hour(scan_datetime, which="floor")
        closest_model_time_ceil = round_date2hour(scan_datetime, which="ceil")
         
        dt_floor = np.abs(
            (scan_datetime - closest_model_time_floor).total_seconds() / 60
        )
        dt_ceil = np.abs((scan_datetime - closest_model_time_ceil).total_seconds() / 60)
        if dt_floor < min_delta:
            model_times = [closest_model_time_floor]
            dt = [dt_floor]
        elif dt_ceil < min_delta:
            model_times = [closest_model_time_ceil]
            dt = [ dt_ceil]
        else:
            model_times = [closest_model_time_floor, closest_model_time_ceil]
            dt = [dt_floor, dt_ceil]

    else:
        model_times = [scan_datetime]
        dt =[]

 #   sys.exit(0)
 #   radar_lat = round(scan.latitude, 4)
 #   radar_lon = round(scan.longitude, 4)
 #   radar_height = round(scan.height)

    # We use the netcdf files (.nc) with the rotated winds extracted from the Stantard files.
    # Note that they should be available on the archive and generated with the
    # `extract_winds_from_fst` program.
    model_filenames = []
    for model_time in sorted(model_times):

        model_filename = find_fcst_file(model_time, model_data_dir)
        if model_filename is None:
            print(f"Model outputs not found for {str(model_time)}.")
            continue
        model_filenames.append(model_filename)

    if len(model_filenames) == 0:
        print(f"Model outputs not found for {str(model_times)}.")
        return

    def expand_time_dim(ds):
        """Expand the time dimension for the variables."""
        for varname, da in ds.data_vars.items():
            ds[varname] = da.expand_dims(dim="time")
        return ds
 # Lazy loading of netcdf files.
    return model_filenames, dt


def extract_winds_from_fst(fst_file, radar_lat, radar_lon, V, output_dir=None):
    """
    Extract the rotated winds from an standard file. If an output directory is
    specified, it saves the winds data in a netcdf file.

    (Adapted from Dominik Jacques get_profiles.py functions)

    Parameter
    ---------
    fst_file: str
        Path to the standard file containing a model output for a single time.
    output_dir: str, optional
        Output directory where to store the wind fields as a netcdf file.
        None by default (no files are saved).

    Returns
    -------
    xarray dataset with the winds and the coordinates information.
    """

    filename = os.path.basename(fst_file)
    init_day = filename.split("_")[0]
    fcst_hour = filename.split("_")[1]

    fcst_init = datetime.strptime(init_day, "%Y%m%d%H")
    timestamp_dt = fcst_init + timedelta(hours=int(fcst_hour))

    # read std file
    wind_dict = fst_tools.get_data(
        file_name=fst_file, var_name="wind_vectors", datev=timestamp_dt, latlon=True
    )

    # wind
    model_latitudes = wind_dict["lat"]
    model_longitudes = wind_dict["lon"]
    model_uuwe = wind_dict["uuwe"]  # west-east   component of wind
    


    model_vvsn = wind_dict["vvsn"]  # south-north component of wind
    ip1_momentum = wind_dict["ip1_list"]  # list of momentum vertical levels

    # Get rid of diagnostic surface level
    # (this step should not be necessary for newer GEM outputs without diagnostic wind)
    model_uuwe = model_uuwe[:, :, 1:]
    model_vvsn = model_vvsn[:, :, 1:]
    ip1_momentum = ip1_momentum[1:]

    # altitude of gridpoints
    gz_dict = fst_tools.get_data(
        file_name=fst_file, var_name="GZ", ip1=ip1_momentum, datev=timestamp_dt
    )
    model_heights = gz_dict["values"] * 10  # decameter to meters
   # print ( model_heights.shape)
    model_heights_average = model_heights.mean(axis=(0,1))
   # print (model_heights_average.shape)
    max_z_index = np.where (model_heights_average > 20000)[0][0]



  #  print ("max_z_index", max_z_index)
    #sys.exit(0)
    ## We cap the model top at ~20km height to avoid saving unnecessary data.
    #max_z_index = 63
  #  model_heights = model_heights[:, :, 0:max_z_index]
  #  model_uuwe = model_uuwe[:, :, 0:max_z_index]
  #  model_vvsn = model_vvsn[:, :, 0:max_z_index]

    model_longitudes = ((model_longitudes + 180) % 360) - 180
    print ('--->',len(model_latitudes))
    print ('--->',len(model_latitudes[0]))  
    print ('--->',len(model_longitudes))
    print ('--->',len(model_longitudes[0]))

    print ('qqqqqq',model_latitudes[100,100])
    print ('qqqqqq',model_longitudes[100,100])

    print (float(radar_lat), float(radar_lon))
    #print (model_latitudes)
   # print (model_longitudes)
    i, j = index_from_latlon(model_latitudes, model_longitudes, float(radar_lat), float(radar_lon))

 #   sys.exit(0)
    if V:
      model_heights = model_heights[i-30:i+30,j-30:j+30 , 0:max_z_index]
      model_uuwe = model_uuwe[i-30:i+30,j-30:j+30, 0:max_z_index]
      model_vvsn = model_vvsn[i-30:i+30,j-30:j+30 , 0:max_z_index]
      model_latitudes = model_latitudes  [i-30:i+30,j-30:j+30]
      model_longitudes = model_longitudes [i-30:i+30,j-30:j+30]
    return  model_latitudes , model_longitudes, model_uuwe, model_vvsn, model_heights


def model2ppi_linear(
    model_latitudes,
    model_longitudes,
    model_heights,
    ppi_latitudes,
    ppi_longitudes,
    ppi_heights,
    model_vars=None,
    invalid_mask=None,
):
    """
    Interpolate the model output into the PPI scan using bilinear interpolation.

    (Based on Dominik Jacques interpolation routine)

    Parameters
    ----------
    model_latitudes: array[lon,lat]
        Model latitudes in degrees.
    model_longitudes: array[lon,lat]
        Model longitudes in degrees.
    model_heights: array[lon,lat, level]
        Model height in meters ASL.
    ppi_latitudes: array[rays,bins]
        Radar bin latitudes in degrees.
    ppi_longitudes: array[rays,bins]
        Radar bin longitude in degrees.
    ppi_heights: array[rays,bins]
        Radar bin heights in meters ASL.
    model_vars: array[lon, lat, level] or list of arrays
        List of model data to interpolate. 
        Each element of the list corresponds to a different variable.
    invalid_mask: array[rays,bins]
        Mask indicating the invalid values in the PPI.
    """

    if model_vars is None:
        raise ValueError("The list of model variables to interpolate cannot be emtpy.")

    if not isinstance(model_vars, (tuple, list)):
        model_vars = [model_vars]
    # IMPORTANT! Only locations with valid values are interpolated
    nrays, nbins = ppi_latitudes.shape
    nz = model_heights.shape[2]
    if invalid_mask is None:
        valid = np.ones_like(ppi_latitudes, dtype=bool)
    else:
        valid = ~invalid_mask

    # Define grids
    ppi_grid = np.stack((ppi_longitudes[valid], ppi_latitudes[valid]), axis=1)
    n_valid_ppi_points = ppi_grid.shape[0]
    model_grid = np.stack((model_longitudes.ravel(), model_latitudes.ravel()), axis=1)

    # 1. The model-> PPI interpolation is done by first interpolating each model level at the radar bins lats/lons (the PPI grid).
    # Then, we interpolate along the vertical at the bins hights.
    # This approach is faster than a 3D interpolation.

    def interpolate2D(data_values, input_grid):
        """Interpolate model data into the ppi grid."""
        interpolator = LinearNDInterpolator(input_grid, data_values.ravel())
        res = interpolator(ppi_grid)
        return res, interpolator.tri

    # [n_valid_ppi_points, nz]
    model_height_at_ppi = np.zeros((n_valid_ppi_points, nz)).copy()
    model_vars_at_ppi3D = [model_height_at_ppi.copy() for _ in model_vars]

    # Iterate over vertical levels and interpolate along the horizontal
    tri = model_grid
    for z in range(model_vars[0].shape[2]):
        model_height_at_ppi[:, z], tri = interpolate2D(model_heights[:, :, z], tri)
        for var_idx, var in enumerate(model_vars):
            model_vars_at_ppi3D[var_idx][:, z], tri = interpolate2D(
                var[:, :, z].ravel(), tri
            )

    # 2. Interpolate the data in the vertical
    z_diff = model_height_at_ppi - ppi_heights[valid][:, None]

    # Variables dimensions:
    # z_diff: [n_valid_ppi_points, nz]
    # model_height_at_ppi: [n_valid_ppi_points, nz]
    nan_diff = np.where(z_diff < 0.0, np.nan, z_diff)
    within_bounds = np.isfinite(nan_diff).any(axis=1)
    outside_bounds = ~within_bounds

    outside_bounds_2d_mask = np.zeros_like(valid)

    idx = np.arange(valid.size)
    idx = idx[valid.ravel()][outside_bounds]
    if len(idx) > 0:
        outside_bounds_2d_mask_flat = outside_bounds_2d_mask.reshape(-1)
        outside_bounds_2d_mask_flat[idx] = True

    nan_diff[outside_bounds] = 0

    k_just_above = np.nanargmin(nan_diff, axis=1)

    k_just_below = k_just_above - 1
    k_just_above[outside_bounds] = nz - 1
    k_just_below[outside_bounds] = nz - 2

    # points below model level
    too_low_inds = np.asarray(k_just_below < 0).nonzero()
    if len(too_low_inds[0]) >= 0:
        k_just_above[too_low_inds] = 1
        k_just_below[too_low_inds] = 0

    # k_just_below: [n_valid_ppi_points,]
    ii = np.arange(n_valid_ppi_points)

    vert_interp_weights = z_diff[ii, k_just_above] / (
        model_height_at_ppi[ii, k_just_above] - model_height_at_ppi[ii, k_just_below]
    )

    def interp_vertically(data_in_3d):
        data_1d_interpolated = (
            vert_interp_weights * data_in_3d[ii, k_just_below]
            + (1.0 - vert_interp_weights) * data_in_3d[ii, k_just_above]
        )

        data2d = np.zeros((nrays, nbins))
        data2d[valid] = data_1d_interpolated
        data2d[outside_bounds_2d_mask] = np.nan
        return data2d

    # Interpolate variables
    model_vars_at_ppi = tuple(interp_vertically(var) for var in model_vars_at_ppi3D)

    if len(model_vars_at_ppi) == 1:
        return model_vars_at_ppi[0]

    return model_vars_at_ppi


def index_from_latlon(grid_lats, grid_lons, lats , lons):
   import scipy.spatial
   import cartopy.crs as ccrs

   radar_lats = np.array([lats])

   radar_lons = np.array([lons])
   grid_shape = grid_lats.shape
   #from latlon to xyz coords 
   proj_ll = ccrs.Geodetic()
   geo_cent = proj_ll.as_geocentric()

   grid_xyz = geo_cent.transform_points(proj_ll,
                                     grid_lons.flatten(),
                                     grid_lats.flatten())

   radar_xyz = geo_cent.transform_points(proj_ll,
                                      radar_lons.flatten(),
                                      radar_lats.flatten())

   #build kdtree from model grid
   kdtree = scipy.spatial.cKDTree(grid_xyz, balanced_tree=False)

   #search nearest neighbor using the tree
   _, indices = kdtree.query(radar_xyz, k=1)
   print ('sss',indices)
   for ii, index in enumerate(indices):
    (nearest_i, nearest_j) = np.unravel_index(index, grid_shape)
    print(f'radar lat/,on: {radar_lats[ii]:.3f},{radar_lons[ii]:.3f} --  nearest i,j: {nearest_i},{nearest_j}')

    return  nearest_i, nearest_j
    
def model_velocity_from_ppi(model_filename, ppi_latitudes, ppi_longitudes, ppi_heights, ppi_azimuths, radar_lat, radar_lon,V):
      
    t1 = time.time()
    model_latitudes , model_longitudes, model_uuwe, model_vvsn, model_heights = extract_winds_from_fst(model_filename, radar_lat, radar_lon, V )
    #  index_latitudes =  model_latitudes

   # model_longitude =  np.where(np.logical_and(model_longitudes>=2, model_longitudes<=10)) 
   # model_latitudes =  np.where(np.logical_and(model_latitudes>=2 , model_latitudes<=10))
    
    t2 = time.time() 
    print (t2-t1, "eta 1 ")
    t1 = time.time()

    model_ = model2ppi_linear(model_latitudes,
                              model_longitudes,
                              model_heights,
                              ppi_latitudes,
                              ppi_longitudes,
                              ppi_heights,
                              model_vars= [model_uuwe, model_vvsn],
                              invalid_mask=None,
                                                )

    model_uuInterpolate = model_[0]
    model_vvInterpolate = model_[1]
    dim1 = len(ppi_heights)
    dim2 = len(ppi_heights[0])
    ppi_azimuths = np.broadcast_to(ppi_azimuths[:,np.newaxis], (dim1,dim2))  
    # Doppler velocity is the projection of wind along direction of radar beam
    # Positive values indicates velocities "away" from the radar
    model_velocity = model_uuInterpolate*np.sin(np.radians(ppi_azimuths)) + model_vvInterpolate*np.cos(np.radians(ppi_azimuths))
    t2 = time.time() 
    print (t2-t1, "eta 2 ")
    return  model_velocity 

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


def plotss(A,nameA,B,nameB,C,nameC,D,nameD):
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
  lat_0 = 45.7063
  delta_lat = 2.18
  lon_0 = -73.85
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
  closeup_lons, closeup_lats = geo_tools.lat_lon_range_az(lon_0, lat_0, radius, azimuths)
  #a line 5km long for showing scale in closeup insert
  azimuth = 90 #meteorological angle
  distance = np.linspace(0,5.,50)#360 degree will be included for full circles
  scale_lons, scale_lats = geo_tools.lat_lon_range_az(lon_0-0.07, lat_0-0.04, distance, azimuth)
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
  proj_inds = geo_tools.ProjInds(src_lon=ppi_longitudes, src_lat=ppi_latitudes,
                                   extent=map_extent,  dest_crs=proj_rp,
                                   extend_x=False, extend_y=True,
                                   image_res=img_res,  missing=missing)

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
  radar_ax_circ(ax, radar_lat, radar_lon)
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
  radar_ax_circ(ax, radar_lat, radar_lon)

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
  radar_ax_circ(ax, radar_lat, radar_lon)

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
  radar_ax_circ(ax, radar_lat, radar_lon)

  #circle indicating closeup area
  # ax.plot(closeup_lons, closeup_lats, transform=proj_pc, c=(0.,0.,0.), zorder=300, linewidth=.8)

  #arrow pointing to closeup
  # ax.annotate("", xy=(0.33, 0.67), xytext=(.55, .74),  xycoords='axes fraction',
  #            arrowprops=dict(arrowstyle="<-"))
  plt.savefig(f'radar_ppi_.png')
#  print ('savefig_end')

# python example.py 2019062100_ra 'casbv' 0.4 '20190620210600' 47.8709983825684
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


def make_input_db(filein, this_time, radar, elevation):

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
                    and id_stn = ?
                    and round(nominal_ppi_elevation, 1) =?
                    ;"""
  conn_ppi_db.execute(order_sql, ( this_time, radar, elevation,))
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
 
  #

  conn_ppi_db.commit()

  return conn_ppi_db

def finder(a, b):
    dup = np.searchsorted(a, b)
    uni = np.unique(dup)
    uni = uni[uni < a.shape[0]]
    ret_b = np.zeros(uni.shape[0])
    for idx, val in enumerate(uni):
        bw = np.argmin(np.abs(a[val]-b[dup == val]))
        tt = dup == val
        ret_b[idx] = np.where(tt == True)[0][bw]
    return np.column_stack((uni, ret_b))

def find_nearest(array, value):
    ''' Find nearest value is an array '''
    idx = (np.abs(array-value)).argmin()
    return idx

def model_velocity_ (dattime, model_data_dir,ppi_latitudes, ppi_longitudes, ppi_heights, ppi_azimuths,radar_lat, radar_lon, V):
   
    
    model_filenames, dt_model_time = model_data_over_radar(dattime, 
                                                    model_data_dir,
                                                    max_range=250,
                                                    interp="linear", 
                                                    min_delta=10)
    if len(model_filenames)==1:

      model_velocity = model_velocity_from_ppi(model_filenames[0], ppi_latitudes, ppi_longitudes, ppi_heights, ppi_azimuths, radar_lat, radar_lon, V)

    else:

      model_velocity_floor = model_velocity_from_ppi(model_filenames[0], ppi_latitudes, ppi_longitudes, ppi_heights, ppi_azimuths,radar_lat, radar_lon, V)
      model_velocity_ceil  = model_velocity_from_ppi(model_filenames[1], ppi_latitudes, ppi_longitudes, ppi_heights, ppi_azimuths,radar_lat, radar_lon, V)
      t_floor = 0.
      t_ceil = 60
      Diff = model_velocity_ceil - model_velocity_floor
      dt =  dt_model_time[0]
      model_velocity = a0 + aDiff * ((dt - t_floor) / (t_ceil -  t_floor))
    
    return model_velocity 



import radvelso
import time
import sqlite3
import domutils.radar_tools as radar_tools
import domutils.geo_tools as geo_tools


sqlite_file = sys.argv[1]
radar     = sys.argv[2]
elevation = float(sys.argv[3])
YmdHMS    = sys.argv[4]
nyquist   = sys.argv[5]
hrad      = sys.argv[6]
radar_lon = sys.argv[7]
radar_lat = sys.argv[8]
radar_lon = -73.8589172363281
radar_lat = 45.7063484191895
hrad = 105.0

print (nyquist)
print ('sqlite_file',sqlite_file)
print ('radar'      ,radar)
print ('elevation',elevation)
print ('YmdHMS'     ,YmdHMS)
dattime = datetime.strptime(YmdHMS, '%Y%m%d%H%M%S') 
model_data_dir ='/home/dlo001/data_maestro/ppp5/operation.forecasts.reghyb/'
np.set_printoptions(threshold=sys.maxsize)

t1 = time.time()  
print (dattime)
hhmiss_pad =  dattime.strftime('%H%M%S') 
#no zeros on left but still 0 if 000000
hhmiss_nopad = str(int(hhmiss_pad))

#Prepare file in memory
filememory=f'file:{sqlite_file}_{YmdHMS}?mode=memory&cache=shared'
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

conn_ppi_db = make_input_db(sqlite_file, hhmiss_nopad, radar, elevation)
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
c = conn_filememory.cursor()
c.row_factory = sqlite3.Row
query = (  f'select range from data;') #ORDER BY RANDOM()  ;')
avg1  = c.execute(query)
ranges = np.array([row[0] for row in avg1])

query = (  f'select obsvalue from data;') #ORDER BY RANDOM()  ;')
avg1  = c.execute(query)
obsvalues = np.array([row[0] for row in avg1])

query = (  f'select CENTER_AZIMUTH, range from data natural join header;') #ORDER BY RANDOM()  ;')
avg1  = c.execute(query)
_azimuths =np.array([row[0] for row in avg1])

no_data = -9999.

delta_azimuth = .5
azimuth_arr = np.arange(0., 360., delta_azimuth)+delta_azimuth/2.
n_azimuths = azimuth_arr.size

min_range = 0.    #m
max_range = 240000.
delta_r   = 500
#ranges used in oputput PPI
range_bounds_arr = np.arange(min_range, max_range+delta_r, delta_r)
range_bin_arr = range_bounds_arr[0:-1] + (range_bounds_arr[1:] - range_bounds_arr[0:-1])/2
n_range_bins = range_bin_arr.size

print ("==========:n_azimuths", n_azimuths, "n_range_bins", n_range_bins)
out_velocity   = np.full((n_azimuths, n_range_bins),no_data)
out_heights    = np.full((n_azimuths, n_range_bins),no_data)
out_latitudes  = np.full((n_azimuths, n_range_bins),no_data)
out_longitudes = np.full((n_azimuths, n_range_bins),no_data)
out_azimuths   = np.full((n_azimuths),no_data)


dist_earth = radar_tools.model_43(elev=elevation, dist_beam=ranges/1e3, hrad=hrad/1e3, want='dist_earth')
_longitudes, _latitudes  = geo_tools.lat_lon_range_az(radar_lon ,radar_lat, dist_earth, _azimuths)

_heights = radar_tools.model_43(elev=elevation, dist_beam=ranges/1e3, hrad=hrad/1e3, want='height')

for Range, Azimuth, obsvalue, heights, lon, lat, azimuth in zip(ranges,_azimuths, obsvalues, _heights, _longitudes, _latitudes, _azimuths):

    ind_range   = find_nearest(range_bounds_arr, Range)
    ind_azimuth = find_nearest(azimuth_arr, Azimuth)
    out_azimuths[ind_azimuth] = azimuth  
    out_velocity[ind_azimuth, ind_range]   = obsvalue
    out_heights[ind_azimuth, ind_range]    =  heights 
    out_longitudes[ind_azimuth, ind_range] = lon
    out_latitudes[ind_azimuth, ind_range]  = lat

# create info and resume_tables in fileout
create_info_midas_tables(sqlite_file, conn_filememory)  



t2 = time.time()  
print (t2-t1, "read_sqlite_vol_0")
#sys.exit(0)

# read sqlite file
t1 = time.time()  
out_dict = radar_tools.read_sqlite_vol(sqlite_file = sqlite_file,
                                         vol_scans = [dattime],
                                            radars = [radar],
                                        elevations = [elevation],
                                            latlon = True,
                                       )

                                       
t2 = time.time()  
print (t2-t1, "read_sqlite_vol")

# definition ppi information 
t1 = time.time()  
radar_lat = out_dict[radar]['radar_lat']
radar_lon = out_dict[radar]['radar_lon']
ppi_latitudes  = out_dict[radar][dattime][f"{elevation}"]['latitudes']
ppi_longitudes = out_dict[radar][dattime][f"{elevation}"]['longitudes']
ppi_heights    = out_dict[radar][dattime][f"{elevation}"]['m43_heights']
ppi_id_obs     = out_dict[radar][dattime][f"{elevation}"]['id_obs']
ppi_azimuths   = out_dict[radar][dattime][f"{elevation}"]['azimuths']
ppi_velocity   = out_dict[radar][dattime][f"{elevation}"]['obsvalue']
ppi_ranges     = out_dict[radar][dattime][f"{elevation}"]['ranges']
ppi_elevations = out_dict[radar][dattime][f"{elevation}"]['elevations']


index = np.where(ppi_velocity!=out_velocity)

if np.size(index[0])==0:
   print("List is empty ppi_velocity")

index = np.where( out_velocity!=-9999.0)




A = ppi_velocity[index]
B = out_velocity[index]
#print (ppi_heights[index[0]],out_heights[index[0]])

if (A==B).all():
   print("List is empty ppi_wwwwwwwwwwwwwwwww")

print (t2-t1, "out_dict")




t1 = time.time()  
print ("enter")
model_velocity2 = model_velocity_(dattime, 
                                  model_data_dir, 
                                  ppi_latitudes,
                                  ppi_longitudes, 
                                  ppi_heights,
                                  ppi_azimuths, 
                                  radar_lat, 
                                  radar_lon, True)
t2 = time.time()  
print (t2-t1, "model_velocity2")

t1 = time.time()  
print ("enter")
model_velocity3 = model_velocity_(dattime, 
                                  model_data_dir, 
                                  ppi_latitudes,
                                  ppi_longitudes, 
                                  ppi_heights,
                                  ppi_azimuths, 
                                  radar_lat, 
                                  radar_lon, False)

                                  
t2 = time.time()  
print (t2-t1, "model_velocity3")
A=model_velocity2
B=model_velocity3
print (A[0,0],B[0,0])
index = np.where(A!=B)
AA = A[index]
BB = B[index]
print (AA[0],BB[0])

print (len(index[0]))
print (np.allclose(A,B),'aaaaaaaaaaa')
if (A==B).all():
   print("List is empty ppi_wwwwwwwwwwwwwwwww")


t1 = time.time()  
model_velocity = model_velocity_(dattime, model_data_dir, out_latitudes, out_longitudes, out_heights, out_azimuths, radar_lat, radar_lon, True)
t2 = time.time()  
print (t2-t1, "model_velocity2")

#A = model_velocity2
#B = model_velocity 
#print (ppi_heights[index[0]],out_heights[index[0]])
#if (A==B).all():
#   print("List is empty ppi_heightsssssssssssssss")

#print (t2-t1, "out_dict")

# Dealias
t1 = time.time()  


print ('len azimuths', len(ppi_azimuths))

print ('ppi_ranges'  , len(ppi_ranges))
print ('ppi_velocity', len(ppi_velocity))
print ('ppi_velocity', len(ppi_velocity[0]))
print ('ele'         , elevation )

undetect_mask = np.where( ppi_velocity == -3333.)
nodata_mask   = np.where( ppi_velocity == -9999.)

_dealias = Dealias(ppi_ranges, ppi_azimuths, elevation, ppi_velocity.copy(), float(nyquist))
_dealias.initialize(model_velocity, beta=0.5)
_dealias.dealiase()
dealiasv= _dealias.velocity

#dealiasv[nodata_mask]=-9999.
#dealiasv[undetect_mask]=-3333.

t2 = time.time() 

index=np.where(ppi_velocity != dealiasv)

print (t2-t1, len(index),index, "+++++++++++++++++++++++Dealias radar velocities")




# Identify the noisy regions
t1 = time.time()  

kernel_az=5
kernel_r=3
filter_threshold = 10
OmP = ppi_velocity - model_velocity



#OmP[qc_data < qi_min] = np.nan
OmP[undetect_mask] = np.nan
OmP[nodata_mask] = np.nan
da = xr.DataArray(data=OmP, dims=("rays", "bins"))
min_valid_bins = int(round(0.65 * kernel_az * (kernel_r + 2)))
OmP_std = (
            da.rolling(
                         rays=kernel_az,
                         bins=kernel_r + 2,
                         center=True,
                         min_periods=min_valid_bins,
                        )
                        .std(skipna=True)
                        .values
                       )

OmP_std[np.isnan(OmP_std)] = 0
OmP_std[np.isnan(OmP)] = 0

#print (OmP_std)
filter_threshold_mask = np.where(OmP_std > filter_threshold)
print ('----->',len(filter_threshold_mask[0]))

ppi_velocity_threshold = np.copy(ppi_velocity)
ppi_velocity_threshold[filter_threshold_mask] = -9999.


index= np.where(ppi_velocity!=ppi_velocity_threshold)
t2 = time.time() 
print (t2-t1, len(index[0]),  "+++++++++++++++++++++++velocity_threshold")
sys.exit(0)
model_velocity[np.isnan(model_velocity)] = -9999.

plotss(ppi_velocity, 'ppi_velocity',
       out_velocity, 'out_velocity',
       model_velocity2, 'model_velocity2',
       model_velocity3, 'model_velocity3')
#ppi_velocity_dealias, 'ppi_velocity_dealias'  )

