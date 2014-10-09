%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define bigname Python

Name:		csdms-python
Version:	2.7.6
Release:	1%{?dist}
Summary:	A Python distibution built for use by CSDMS software
Group:		Applications/Engineering
License:	Python
URL:		http://www.python.org
#Source0:	https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
Source0:	%{name}-%version.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%name-%version-%release
Prefix:         %{_prefix}
Autoreq:	0

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
A Python 2.7 distribution that serves as the base for building CSDMS
software tools. This distribution is installed alongside the CSDMS
software stack so it won't interfere with the native Python
distribution on a user's machine. Includes `pip`, `numpy`, `scipy`,
`nose`, `Shapely`, `pyyaml` and `netcdf4`.

%prep
%setup -q -n %bigname-%version

%build
%configure --libdir=%{lib32dir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 LICENSE README %{buildroot}%{docdir}/%{name}-%{version}/
rm -rf %{buildroot}/usr/share/man/

# Install pip, then use it to install other needed packages.
wget https://bootstrap.pypa.io/get-pip.py
%{buildroot}%{_bindir}/python get-pip.py
%{buildroot}%{_bindir}/pip install numpy
%{buildroot}%{_bindir}/pip install nose
%{buildroot}%{_bindir}/pip install scipy
%{buildroot}%{_bindir}/pip install netcdf4
%{buildroot}%{_bindir}/pip install Shapely
%{buildroot}%{_bindir}/pip install pyyaml
rm -rf %{buildroot}%{_prefix}/man
mv %{buildroot}%{_prefix}/shapely/* \
   %{buildroot}%{lib32dir}/python2.7/site-packages/shapely/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/
%{_includedir}/
%{_datadir}

%changelog
* Thu Oct  9 2014 Mark Piper <mpiper@siwenna.colorado.edu> - 2.7.6-1
- Initial build

