%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		cca-spec-babel
Version:	0.8.6
Release:	1%{?dist}
Summary:	CCA Specification Babel bindings
Group:		Applications/Engineering
License:	Other
URL:		http://www.cca-forum.org
Source0:	http://www.cca-forum.org/download/cca-tools/cca-tools-latest/cca-spec-babel-0.8.6.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
CCA Specification Babel bindings.

%prep
%setup -q

%build
%configure --disable-contrib \
	   --with-F90-vendor=GNU
make %{?_smp_mflags} all

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# %{_bindir}/%{name}-config
# %{_includedir}/
# %{_datadir}/
# %{lib32dir}/

%changelog
* Tue Sep 30 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
