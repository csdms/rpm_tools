%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define ur_name hdf5

Name:		csdms-hdf5
Version:	1.8.9
Release:	1%{?dist}
Summary:	An HDF5 distribution built for use by CSDMS software
Group:		Development/Libraries
License:	HDF5
URL:		http://hdfgroup.org/HDF5/
#Source0:	ftp://ftp.hdfgroup.org/HDF5/releases/%{ur_name}-%{version}/src/%{ur_name}-%{version}.tar.gz
Source0:	%{name}-%version.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%name-%version-%release
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
This package contains an HDF5 distribution, including the library and
development tools, on which the CSDMS software stack can be
built. This distribution is installed alongside the CSDMS software
stack so it won't interfere with another HDF5 distribution on a user's
machine.

%prep
%setup -q -n %ur_name-%version

%build
%configure --libdir=%{lib32dir}
make %{?_smp_mflags}

%check
make check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%ur_name-%version
install -m664 ACKNOWLEDGMENTS COPYING MANIFEST README.txt \
	 %{buildroot}%{docdir}/%ur_name-%version/

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
* Sat Oct 18 2014 Mark Piper <mark.piper@colorado.edu> - 1.8.9-1
- Initial build

