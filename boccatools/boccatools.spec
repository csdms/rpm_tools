%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		boccatools
Version:	%{_version}
Release:	1%{?dist}
Summary:	Python utilities for bocca
Group:		Applications/Engineering
License:	MIT
URL:		http://csdms.colorado.edu
# The BoccaTools source can be checked out from the CSDMS Trac site:
# $ svn co https://csdms.colorado.edu/svn/bocca_tools/trunk
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
The Python utilities `bocca-build`, `bocca-clone`, `bocca-ignore`, and 
`bocca-save`.

%prep
%setup -q

%build

# Following babel, allow boccatools to install libraries in %{lib32dir}.
# The package install location should be /usr/local/csdms.
# Get Python from babel.
%install
rm -rf %{buildroot}
$(%{_prefix}/bin/babel-config --which-var=PYTHON) setup.py install \
	 --prefix=%{buildroot}%{_prefix} \
	 --single-version-externally-managed \
	 --record="installed.txt"
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 installed.txt %{buildroot}%{docdir}/%{name}-%{version}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/
%{_datadir}/

%changelog
* Tue Oct 7 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
