%define lib32dir %{_prefix}/lib
%define pip_name pip
%define pip_version 1.5.6

Name:		csdms-python-tools
Version:	0.1
Release:	2%{?dist}
Summary:	Python packages used by CSDMS software
Group:		Development/Libraries
License:	MIT
URL:		https://pip.pypa.io/en/latest/
#Source0:	https://pypi.python.org/packages/source/p/%{pip_name}/%{pip_name}-%{pip_version}.tar.gz
Source0:	%{name}-%version.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%name-%version-%release
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
A set of Python packages that are installed with the CSDMS Python
distribution (csdms-python). Includes pip, NumPy, SciPy, nose,
Shapely, PyYAML and netCDF4.

%prep
%setup -q -n %{pip_name}-%{pip_version}

# Build pip.
%build
$CSDMS_PYTHON setup.py build

# Install pip, then use it to install the other packages.
%install
rm -rf %{buildroot}
$CSDMS_PYTHON setup.py install -O1 --skip-build --root %{buildroot}
export HDF5_DIR=%{_prefix}
export NETCDF4_DIR=%{_prefix}
export PYTHONPATH=%{buildroot}%{lib32dir}/python2.7/site-packages
%{buildroot}%{_prefix}/bin/pip install numpy --root %{buildroot}
%{buildroot}%{_prefix}/bin/pip install nose --root %{buildroot}
%{buildroot}%{_prefix}/bin/pip install scipy --root %{buildroot}
%{buildroot}%{_prefix}/bin/pip install netcdf4 --root %{buildroot}
%{buildroot}%{_prefix}/bin/pip install shapely --root %{buildroot}
%{buildroot}%{_prefix}/bin/pip install pyyaml --root %{buildroot}
rm -rf %{buildroot}%{_prefix}/man
mv %{buildroot}%{_prefix}/shapely/* $PYTHONPATH/shapely/
rm -rf %{buildroot}%{_prefix}/shapely

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/

%changelog
* Mon Oct 20 2014 Mark Piper <mark.piper@colorado.edu> - 0.1-2
- Use csdms-netcdf for the Python netCDF4 package

* Thu Oct 16 2014 Mark Piper <mark.piper@colorado.edu> - 0.1-1
- Initial build
