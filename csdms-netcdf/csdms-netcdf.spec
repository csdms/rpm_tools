%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define ur_name netcdf

Name:		csdms-netcdf
Version:	4.1.3
Release:	1%{?dist}
Summary:	A NetCDF distribution built for use by CSDMS software
Group:		Development/Libraries
License:	BSD-like
URL:		http://www.unidata.ucar.edu/software/netcdf/
#Source0:	ftp://ftp.unidata.ucar.edu/pub/%{ur_name}/%{ur_name}-%{version}.tar.gz
Source0:	%name-%version.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%name-%version-%release
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
This package contains a NetCDF distribution, including the library and
development tools, on which the CSDMS software stack can be
built. This distribution is installed alongside the CSDMS software
stack so it won't interfere with another NetCDF distribution on a
user's machine.

%prep
%setup -q -n %ur_name-%version

# Use environment variables to locate the HDF5 install (csdms-hdf5).
%build
export CPPFLAGS=-I%{_includedir}
export LDFLAGS=-L%{lib32dir}
export LD_LIBRARY_PATH=%{lib32dir}
%configure --libdir=%{lib32dir} --enable-netcdf4 --with-libcf --with-udunits
make %{?_smp_mflags}

%check
make check

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%ur_name-%version
install -m664 COPYRIGHT INSTALL README RELEASE_NOTES VERSION \
	 %{buildroot}%{docdir}/%ur_name-%version/
rm -rf %{buildroot}/usr/share

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/
%{_includedir}/
%{_datadir}/

%changelog
* Mon Oct 20 2014 Mark Piper <mark.piper@colorado.edu> - 4.1.3-1
- Initial build

