# raster-proc
Raster processing and modeling python package for Earth Observation data.

This package contains general functions to download, process and model Earth Observation/Remote Sensing data. 
It contains the following functionalities:

- processing: download from STAC and processing function for COGS and more
- plotting: plotting categorical raster, time series and more
- modeling: applying sklearn and tensorflow model to raster with ease
- timeseries: creating stack of raster for timeseries analyses



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


## Contributing

- To install locally do:
```
pip install -e .
```

```angular2html
python -m pip install --user --upgrade setuptools
python setup.py sdist
```
python setup.py sdist bdist_wheel

```angular2html
pip install twine

twine upload --repository testpypi dist/*

```

useful links:
- https://kynan.github.io/blog/2020/05/23/how-to-upload-your-package-to-the-python-package-index-pypi-test-server

## Versioning

For the versions available, see the [tags on this repository](https://github.com/bparment1/raster-proc/tags).

## Authors

* [Benoit Parmentier](https://github.com/bparment1)

See also the list of [contributors](https://github.com/bparment1/raster-proc/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Inspiration from working with rasterio and wanting to extend functionalities
* etc



