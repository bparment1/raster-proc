# raster-proc
Raster processing and modeling python package for Earth Observation data.

This package contains general functions to download, process and model Earth Observation/Remote Sensing data. The goal is
It contains the following functionalities:

- processing
- plotting
- modeling
- timeseries

# INSTALL

Create a virtual environment

```
python -m venv venv
source venv/bin/activate
```

To use this package you will need to use GDAL:

if on ubuntu 22.04
```
sudo apt-get install libgdal-dev gdal-config
export CPLUS_INCLUDE_PATH=$(gdal-config --cflags | sed 's/-I//')
export C_INCLUDE_PATH=$(gdal-config --cflags | sed 's/-I//')
pip install GDAL==$(gdal-config --version)
```

Then you can install the packages:

```
pip install -r requirements.txt
```

#Upate/Contribute to package

- To install locally do:
```
pip install -e .
```




