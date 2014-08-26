Name:		babel
Version:	1.4.0
Release:	1%{?dist}
Summary:	Babel is a high-performance language interoperability tool
Group:		Applications/Engineering
License:	LGPLv2+
URL:		http://computation.llnl.gov/casc/components
# The HydroTrend source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/hydrotrend/trunk
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
%configure --disable-documentation
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ANNOUNCE BUGS CHANGES COPYRIGHT INSTALL LICENSE README THANKS
#%{_bindir}/%{name}
#%{_includedir}/%{name}_cli.h
#%{_includedir}/bmi_%{name}.h
#%{_libdir}/lib%{name}.so
#%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Aug 25 2014 Mark Piper <mark.piper@colorado.edu>
- Set up spec file for building package
