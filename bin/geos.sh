curl -O http://download.osgeo.org/geos/geos-3.4.2.tar.bz2
tar -xjvf geos-3.4.2.tar.bz2
./configure --prefix=/app/.heroku/vendor
make
make install
