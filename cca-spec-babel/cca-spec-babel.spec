%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		cca-spec-babel
Version:	0.8.6
Release:	2%{?dist}
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

# Following babel, allow cca-spec-babel to install in %{lib32dir} for 
# dependent packages. Python 2.7, required for building the CSDMS software 
# stack, is inherited from babel.
%build
%configure --disable-contrib \
	   --with-babel-config=%{_prefix}/bin/babel-config \
	   --libdir=%{lib32dir}
make %{?_smp_mflags} all

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 CHANGELOG TODO \
	%{buildroot}%{docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{_includedir}/
%{_datadir}/
%{lib32dir}/

%changelog
* Wed Oct  8 2014 Mark Piper <mpiper@siwenna.colorado.edu> - 0.8.6-2
- Remove Python flags from configure; get them from babel.

* Wed Oct 1 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
