rpm-tools
=========

Recipes for building binary and source RPMs for CSDMS tools.

**Requirements**

These recipes are designed for Linux distros 
that are compatible with
Red Hat Enterprise Linux (e.g., CentOS, Fedora). 
To install CSDMS tools on Mac OS X, 
please see the [csdms/homebrew-tools](https://github.com/csdms/homebrew-tools) 
project.

To build and install the tools in this project,
the mandatory and default packages in the 
"Development Tools" group (such as `make`, `gcc`, and `rpm-build`) 
are required,
as well as the optional `cmake`, `git` and `rpmdevtools` packages.
Install them with:
```bash
$ sudo yum groupinstall "development tools"
$ sudo yum install cmake git rpmdevtools
```

**Preparation**

Download and install the `packagebuilder` Python package from the
[csdms/packagebuilder](https://github.com/csdms/packagebuilder)
repository:
```bash
$ git clone https://github.com/csdms/packagebuilder.git
$ cd packagebuilder
$ sudo python setup.py install
```
This installs the script `build_rpm`,
which is used to build the RPMs for a tool.
The standard `rpmbuild` tool can also be used,
but `build_rpm` takes care of a lot of the busy work
to make the build process easier.

To separate the CSDMS software stack from other programs,
it's designed to be installed 
in the directory **/usr/local/csdms**,
although this is optional.
Set the environment variable `CSDMS_DIR`:
```bash
$ export CSDMS_DIR=/usr/local/csdms
```
to the installation path on your machine.
`CSDMS_DIR` is used by several recipes in this project.

The `QA_RPATHS` environment variable may also need to be set:
```bash
$ export QA_RPATHS=19
```
for building RPMs.

**Building and installing the CSDMS tools**

The tools in this project form a cascading set of dependencies.
Build and install in this order:

1. `csdms-python`
1. `csdms-hdf5`
1. `csdms-netcdf` (requires csdms-hdf5)
1. `csdms-python-tools` (requires csdms-python, csdms-netcdf)
1. `babel` (requires csdms-python, csdms-python-tools)
1. `cca-spec-babel` (requires babel)
1. `ccaffeine` (requires babel, cca-spec-babel)
1. `bocca` (requires babel, cca-spec-babel, ccaffeine)
1. `boccatools` (requires babel, bocca, csdms-python)
1. `esmf` (requires csdms-netcdf, csdmd-python, csdms-python-tools)
1. `cmi` (csdms-python, babel, cca-spec-babel, ccaffeine, bocca, boccatools, as well as child, sedflux, hydrotrend, and cem from [csdms/rpm_models](https://github.com/csdms/rpm_models))
1. `coupling` (csdms-python, csdms-python-tools, esmf)

Build RPMs by
calling `build_rpm` with the package name as a parameter.
For example, to build `csdms-python`:
```bash
$ build_rpm csdms-python --tag=2.7.6 --prefix=$CSDMS_DIR
```
Many of the packages are built against a set version of a tool;
e.g., Python 2.7.6.
Check the package's **.spec** file to get the version
used for input to `build_rpm`'s `tag` argument.

On success,
the RPMs will be located in the directories:

* **~/rpmbuild/RPMS** (binary)
* **~/rpmbuild/SRPMS** (source)

on your machine.

Install the package from the binary RPM with `rpm`.
For example:
```bash
$ sudo rpm -ivh csdms-python-2.7.6-2.el6.x86_64.rpm
```

Check that the package was installed successfully:
```bash
$ $CSDMS_DIR/bin/python --version
Python 2.7.6
```

**The CSDMS repository**

Built versions of all of the tools in this project are available 
from the CSDMS repository, 
[http://csdms.colorado.edu/repo/](http://csdms.colorado.edu/repo/).
See the [README.md](http://csdms.colorado.edu/repo/README.md) file
for instructions on how to install these packages 
on your machine.
