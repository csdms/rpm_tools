%global _lib32dir /usr/lib

Name:		babel
Version:	1.4.0
Release:	1%{?dist}
Summary:	Babel is a high-performance language interoperability tool
Group:		Applications/Engineering
License:	LGPLv2+
URL:		http://computation.llnl.gov/casc/components
Source0:	http://computation.llnl.gov/casc/components/docs/%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}

#%if 0%{?_buildrequires:1}
#BuildRequires:	%{_buildrequires}
#%endif
#Requires:

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

%build
%configure \
	--enable-java=/usr/lib/jvm/java-1.7.0-openjdk.x86_64 \
	--disable-documentation
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ANNOUNCE BUGS CHANGES COPYRIGHT INSTALL LICENSE README THANKS
%{_bindir}/%{name}
%{_bindir}/%{name}-*
%{_includedir}/%{name}_config.h
%{_includedir}/c
%{_includedir}/cxx/
%{_includedir}/java/
%{_includedir}/libparsifal/
%{_includedir}/python2.7/
%{_includedir}/sidl*
%{_datadir}/%{name}-%{version}/
%{_datadir}/%{name}-runtime-%{version}/patches/*.txt
%{_datadir}/sgml/%{name}-%{version}/config/*
%{_datadir}/aclocal/*.m4
%{_datadir}/*.sidl
%{_libdir}/libparsifal*
%{_libdir}/libsidl*
%{_lib32dir}/

%changelog
* Mon Aug 25 2014 Mark Piper <mark.piper@colorado.edu>
- Set up spec file for building package
