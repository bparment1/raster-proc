# raster-proc
Raster processing and modeling python package for Earth Observation data

Create a virtual environment

```
python -m venv venv
pip install -r requirements.txt
```

if on ubuntu 22.04
```
sudo apt-get install libgdal-dev gdal-config
export CPLUS_INCLUDE_PATH=$(gdal-config --cflags | sed 's/-I//')
export C_INCLUDE_PATH=$(gdal-config --cflags | sed 's/-I//')
pip install GDAL==$(gdal-config --version)
```
