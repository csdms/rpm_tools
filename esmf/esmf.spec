%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		esmf
Version:	6.3.0
Release:	4%{?dist}
Summary:	Software for building and coupling weather, climate, and related models
Group:		Development/Libraries
License:	NCSA
URL:		http://www.earthsystemmodeling.org
# The ESMF source can be obtained with `git` from:
# $ git clone git://git.code.sf.net/p/esmf/esmf --branch ESMF_6_3_0rp1
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
The Earth System Modeling Framework (ESMF) defines an architecture for
composing complex, coupled modeling systems and includes data
structures and utilities for developing individual models. It has a
robust, parallel and scalable remapping package, used to generate
remapping weights. It can handle a wide variety of grids and options:
logically rectangular grids and unstructured meshes; regional or
global grids; 2D or 3D; and pole and masking options. ESMPy supports a
single-tile logically rectangular discretization type called Grid and
an unstructured discretization type called Mesh (ESMF also supports
observational data streams). ESMPy supports bilinear, finite element
patch recovery and first-order conservative regridding. There is also
an option to ignore unmapped destination points and mask out points on
either the source or destination.

%prep
%setup -q

# ESMF uses environment variables instead of a configure script. 
# Note that, unless set externally, environment variables don't transfer
# between the sections of a spec file.
%build
export ESMF_DIR=%{_builddir}/%{name}-%{version}
export ESMF_INSTALL_PREFIX=%{_prefix}
export ESMF_INSTALL_HEADERDIR=include/%name
export ESMF_NETCDF="split"
export ESMF_NETCDF_INCLUDE=%{_includedir}
export ESMF_NETCDF_LIBPATH=%{lib32dir}
make info > build-info.txt
make %{?_smp_mflags} lib

# %check
# export ESMF_DIR=%{_builddir}/%{name}-%{version}
# export ESMF_INSTALL_PREFIX=%{_prefix}
# export ESMF_INSTALL_HEADERDIR=include/%name
# export ESMF_NETCDF="split"
# export ESMF_NETCDF_INCLUDE=%{_includedir}
# export ESMF_NETCDF_LIBPATH=%{lib32dir}
# make check

# Following babel, allow esmf to install libraries in %{lib32dir}.
# The package install location should be /usr/local/csdms.
%install
rm -rf %{buildroot}
export ESMF_DIR=%{_builddir}/%{name}-%{version}
export ESMF_INSTALL_PREFIX=%{_prefix}
export ESMF_INSTALL_HEADERDIR=include/%name
export ESMF_NETCDF="split"
export ESMF_NETCDF_INCLUDE=%{_includedir}
export ESMF_NETCDF_LIBPATH=%{lib32dir}

# A horrible, awful fix, but due entirely to the design of ESMF. 
# Starting with an empty $CSDMS_DIR, install required packages
# for ESMF. Install ESMF and ESMPy directly into $CSDMS_DIR! Erase the
# required packages; the remainder is ESMF. Copy the contents of
# $CSDMS_DIR to %{buildroot} and finish.
# sudo yum install -y csdms-python csdms-hdf5 csdms-netcdf csdms-python-tools
sudo -E make install
cd $ESMF_DIR/src/addon/ESMPy
sudo -E $CSDMS_PYTHON setup.py build --ESMFMKFILE=%{lib32dir}/libO/Linux.gfortran.64.mpiuni.default/esmf.mk install
# sudo -E $CSDMS_PYTHON setup.py test_all
sudo yum erase -y csdms-python csdms-hdf5
mkdir -p %{buildroot}%{_prefix}
cp -R %{_prefix}/* %{buildroot}%{_prefix}
sudo rm -rf %{_prefix}

# Install build docs for ESMF and ESMPy. 
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
cd $ESMF_DIR
install -m755 build-info.txt LICENSE README \
	%{buildroot}%{docdir}/%{name}-%{version}/
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}/ESMPy
cd $ESMF_DIR/src/addon/ESMPy
install -m755 LICENSE README \
	%{buildroot}%{docdir}/%{name}-%{version}/ESMPy/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/
%{_includedir}/
%{_prefix}/mod/
%{_datadir}

%changelog
* Tue Oct 28 2014 Mark Piper <mpiper@siwenna.colorado.edu> - 6.3.0-4
- Unpack tarball to %name-%version and set ESMF_DIR

* Tue Oct 21 2014 Mark Piper <mpiper@siwenna.colorado.edu> - 6.3.0-3
- Implement ugly fix to get correct paths
- Include NetCDF support

* Fri Oct 10 2014 Mark Piper <mpiper@siwenna.colorado.edu> - 6.3.0-2
- Use $CSDMS_PYTHON to build ESMPy

* Tue Oct 7 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
