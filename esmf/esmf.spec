%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define esmfmkfile %{_builddir}/%{name}/lib/libO/Linux.gfortran.64.mpiuni.default/esmf.mk

Name:		esmf
Version:	6.3.0
Release:	1%{?dist}
Summary:	Software for building and coupling weather, climate, and related models
Group:		Applications/Engineering
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
patch recovery and first-order conservative regridding.  There is also
an option to ignore unmapped destination points and mask out points on
either the source or destination.

%prep
%setup -q -n %{name}

# ESMF requires environment variables.
%build
export ESMF_DIR=%{_builddir}/%{name}
export ESMF_INSTALL_PREFIX=%{buildroot}%{_prefix}
make info > build-info.txt
make lib
cd %{_builddir}/%{name}/src/addon/ESMPy
/usr/local/bin/python2.7 setup.py build --ESMFMKFILE=%{esmfmkfile}

# Following babel, allow esmf to install libraries in %{lib32dir}.
# The package install location should be /usr/local/csdms.
# Note that, unless set externally, environment variables don't transfer 
# between the sections of a spec file.
%install
export ESMF_DIR=%{_builddir}/%{name}
export ESMF_INSTALL_PREFIX=%{buildroot}%{_prefix}
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m755 build-info.txt LICENSE README \
	%{buildroot}%{docdir}/%{name}-%{version}/
cd %{_builddir}/%{name}/src/addon/ESMPy
/usr/local/bin/python2.7 setup.py install --prefix=%{buildroot}%{_prefix}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}/ESMPy
install -m755 LICENSE README \
	%{buildroot}%{docdir}/%{name}-%{version}/ESMPy/

%check
export ESMF_DIR=%{_builddir}/%{name}
export ESMF_INSTALL_PREFIX=%{buildroot}%{_prefix}
make check

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
* Tue Oct 7 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
