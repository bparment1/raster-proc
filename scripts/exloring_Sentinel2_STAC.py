import raster_proc.processing *

raster_proc.processing.process.

## Functions

def create_dir_and_check_existence(path: str) -> str:
  '''
  Create a new directory

  :param path: path to the directory
  :return: path to the directory
  '''

  try:
    os.makedirs(path)
  except:
    print ("directory already exists")
  return path


############################################################################
#####  Parameters and argument set up ###########

#ARG 1
in_dir = '../data/'
#ARG 2
out_dir = "."
#ARGS 3:
create_out_dir=True #create a new ouput dir if TRUE
#ARG 4
out_suffix = "covid_shutdown_stac_processing_sentinel5p_20231217" #output suffix for the files and ouptut folder
#ARG 5

in_filename_roi = None

period_freq = 'D' #use 5D for days means that we using both Sentinel 2A and 2B
#bbox=[-72.8, 43.5, -72.7, 43.6] #xmin,ymin,xmax,ymax
bbox = None
convert_to_dms = True
#centroid_val = [ 43.750,-73.132]
centroid_val= ['''44°20'11.5"N''', '''72°45'21.2"W''']
#infilename_= 'Sentinel2_level2A_band_description.csv'
processing_files=False
#processing_files=True #if True then crop, reproject and download
mask_values = [0,1,8,9]

#Args for STAC
start_date = '2019-01-01'
end_date = '2023-10-10'
image_collections = "sentinel-5p-l2-netcdf"
#image_collections = "sentinel-2-l2a"#can be landsat or anything of interest
URL = 'https://planetarycomputer.microsoft.com/api/stac/v1' #STAC API URL
#'https://earth-search.aws.element84.com/v0'

#band selected for processing
bands_selected = ['no2']
platform='Sentinel-2A'
platform= None

event_date = '2020-3-10'
add_description = False

