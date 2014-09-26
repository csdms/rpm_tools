%define docdir %{_datadir}/doc

Name:		chasm
Version:	1.4.RC3
Release:	1%{?dist}
Summary:	A language transformation system created to improve Fortran and C/C++ language interoperability.
Group:		Applications/Engineering
License:	LANL
URL:		http://chasm-interop.sourceforge.net
Source0:	http://sourceforge.net/projects/chasm-interop/files/chasm_1.4.RC3.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Chasm is a language transformation system created to improve Fortran
and C/C++ language interoperability. Chasm (with the aid of associated
tools) parses Fortran and C/C++ source code and automatically
generates bridging code that can be used to make calls to routines in
the foreign language. Chasm also supplies an array-descriptor library
that provides an interface between C and F90 assumed-shape
arrays. This allows arrays to be created in one language and then
passed to and used by the other (foreign) language.

%prep
%setup -q

%build
%configure --with-F90=$FC \
	   --with-F90-vendor=GNU \
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 INSTALL %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 LICENSE %{buildroot}%{docdir}/%{name}-%{version}/
install -m664 README %{buildroot}%{docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
# %{docdir}/%{name}-%{version}/
# %{_bindir}/%{name}

%changelog
* Fri Sep 26 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
