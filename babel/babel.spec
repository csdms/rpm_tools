%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define url http://computation.llnl.gov/casc/components

Name:		babel
Version:	1.4.0
Release:	3%{?dist}
Summary:	Babel is a high-performance language interoperability tool
Group:		Applications/Engineering
License:	LGPLv2+
URL:		%{url}
Source0:	%{url}/docs/%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Babel is a tool that enables software written in different languages
to communicate. It accomplishes this task by using an interface
definition language, the Scientific Interface Definition Language
(SIDL), that is specifically tuned for scientific applications. By
expressing software interfaces in SIDL, the appropriate glue code
stubs and skeletons can be generated to facilitate language
interoperability.

%prep
%setup -q

# Disable Java support, although babel still needs Java to build.
# Use gfortran for F77, F90, F03.
# Python 2.7 (provided by csdms-python) is required for CSDMS software stack.
# Allow babel to install in %{lib32dir} for dependent packages.
%build
%configure --disable-documentation \
	   --with-F90-vendor=GNU \
	   --with-libparsifal=local \
	   --disable-java \
	   --enable-python=$CSDMS_PYTHON \
	   --libdir=%{lib32dir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 ANNOUNCE BUGS CHANGES COPYRIGHT INSTALL LICENSE README THANKS \
	%{buildroot}%{docdir}/%{name}-%{version}/
rm %{buildroot}%{_includedir}/c # remove sketchy symlink

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%check
#make check # loooong

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{_includedir}/
%{_datadir}/
%{lib32dir}/

%changelog
* Thu Oct  9 2014 Mark Piper <mark.piper@colorado.edu> - 1.4.0-3
- Use csdms-python package and $CSDMS_PYTHON

* Wed Oct 1 2014 Mark Piper <mark.piper@colorado.edu>
- Allow babel to install in lib/ instead of lib64/ 

* Wed Sep 24 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
