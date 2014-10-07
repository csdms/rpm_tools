%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

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
The Earth System Modeling Framework (ESMF) collaboration is building
high-performance, flexible software infrastructure to increase ease of
use, performance portability, interoperability, and reuse in climate,
numerical weather prediction, data assimilation, and other Earth
science applications. The ESMF defines an architecture for composing
complex, coupled modeling systems and includes data structures and
utilities for developing individual models.

%prep
%setup -q -n %{name}

# Following babel, allow bocca to install libraries in %{lib32dir}.
# The package install location should be /usr/local/csdms.
# Python 2.7 is required for the CSDMS software stack.
# ESMF requires several environment variables...
%build
export ESMF_DIR=%{_builddir}
#export ESMF_COMM="mpiuni"
#export ESMF_COMPILER=gfortran
export ESMF_INSTALL_PREFIX=%{buildroot}%{_prefix}
make info > build-info.txt
make lib

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m755 build-info.txt %{buildroot}%{docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%{_bindir}/
#%{lib32dir}/
#%{docdir}/

%changelog
* Tue Oct 7 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
