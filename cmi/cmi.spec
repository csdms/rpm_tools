%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		cmi
Version:	head
Release:	1%{?dist}
Summary:	Component wrappers for the Component Modeling Interface
Group:		Applications/Engineering
License:	MIT
URL:		http://csdms.colorado.edu
# The CMI source can be obtained with `git` from:
# $ git clone git://github.com/csdms/cmi.git
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Component wrappers for the CSDMS Component Modeling Interface.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

%check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
#%{_bindir}/
#%{lib32dir}/
#%{_includedir}/
#%{_datadir}

%changelog
* Wed Oct 8 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
