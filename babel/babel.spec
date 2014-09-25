%define _lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define url http://computation.llnl.gov/casc/components

Name:		babel
Version:	1.4.0
Release:	1%{?dist}
Summary:	Babel is a high-performance language interoperability tool
Group:		Applications/Engineering
License:	LGPLv2+
URL:		%{url}
Source0:	%{url}/docs/%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         /usr

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Babel is a tool that enables software written in different languages
to communicate. It accomplishes this task by using an Interface
Definition Language (IDL) similar to COM and CORBA. Babel relies on
the Scientific Interface Definition Language (SIDL) that is
specifically tuned for scientific applications. By expressing software
interfaces, or APIs1, in SIDL the appropriate glue code stubs and
skeletons can be generated to facilitate language interoperability.

%prep
%setup -q

# Assuming use of Oracle JDK, installed in default location, and gfortran.
# Python 2.7 is required for CSDMS software stack.
%build
%configure --disable-documentation \
	   --with-F90-vendor=GNU \
	   --with-libparsifal=local \
	   --enable-java=/usr/java/default \
	   --enable-python=/usr/local/bin/python2.7
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 ANNOUNCE %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 BUGS %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 CHANGES %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 COPYRIGHT %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 INSTALL %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 LICENSE %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 README %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 THANKS %{buildroot}%{docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
#make check # loooong

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{docdir}/%{name}-%{version}/ANNOUNCE
%{docdir}/%{name}-%{version}/BUGS
%{docdir}/%{name}-%{version}/CHANGES
%{docdir}/%{name}-%{version}/COPYRIGHT
%{docdir}/%{name}-%{version}/INSTALL
%{docdir}/%{name}-%{version}/LICENSE
%{docdir}/%{name}-%{version}/README
%{docdir}/%{name}-%{version}/THANKS
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_includedir}/%{name}_config.h
%{_includedir}/c
%{_includedir}/cxx/
%{_includedir}/f77/
%{_includedir}/f90/
%{_includedir}/java/
%{_includedir}/libparsifal/
%{_includedir}/python2.7/
%{_includedir}/sidl*
%{_datadir}/%{name}-%{version}/
%{_datadir}/%{name}-runtime-%{version}/patches/*.txt
%{_datadir}/sgml/%{name}-%{version}/config/*
%{_datadir}/aclocal/*.m4
%{_datadir}/*.sidl
%{_libdir}/libchasmlite*
%{_libdir}/libparsifal*
%{_libdir}/libsidl*
%{_lib32dir}/

%changelog
* Wed Sep 24 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
