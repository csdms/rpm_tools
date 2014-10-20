# Notes

The `--with-hdf5=` parameter to `configure` is not the correct way to tell
netCDF where the HDF5 library is.

Instead, set the environment variables `CPPFLAGS` and `LDFLAGS`:

    export CPPFLAGS=-I$CSDMS_DIR/include
    export LDFLAGS=-L$CSDMS_DIR/lib
    export LD_LIBRARY_PATH=$CSDMS_DIR/lib

Then run `configure`. Don't forget to do a `make distclean` first.

From [http://www.unidata.ucar.edu/mailing_lists/archives/netcdfgroup/2011/msg00342.html](http://www.unidata.ucar.edu/mailing_lists/archives/netcdfgroup/2011/msg00342.html).

The `configure` call:

   ./configure --prefix=$CSDMS_DIR --libdir=$CSDMS_DIR/lib --enable-netcdf4 --with-libcf
