%define lib32dir %{_prefix}/lib

Name:		bocca
Version:	0.5.7
Release:	1%{?dist}
Summary:	
Group:		Applications/Engineering
License:	Other
URL:		http://www.cca-forum.org
Source0:	http://www.cca-forum.org/download/cca-tools/cca-tools-latest/bocca-0.5.7.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description

%prep
%setup -q

# Following babel, allow bocca to install in %{lib32dir}.
# The install location should be /usr/local/csdms.
%build
%configure --disable-doc \
	   --libdir=%{lib32dir} \
	   --with-cca-babel=%{_prefix} \
	   --with-babel-libtool=%{_prefix}/bin/babel-libtool \
	   --without-mpi \
	   --with-boost=/usr/include
make # deparallelize

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# %{_bindir}/
# %{_includedir}/
# %{_datadir}/
# %{lib32dir}/

%changelog
* Fri Oct 3 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
