%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define ur_name boost

Name:		csdms-boost-headers
Version:	1.34.0
Release:	1%{?dist}
Summary:	Headers for the free peer-reviewed portable C++ source libraries
Group:		Development/Libraries
License:	Boost
URL:		http://www.cca-forum.org
#Source0:	http://www.cca-forum.org/download/cca-tools/dependencies/boost_1_34_0.tar.gz
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
This package contains only the C++ header files for the Boost
libraries. This particular version of Boost is required to build the CCA
tools used in the CSDMS software stack; newer versions are incompatible.

# The version is mangled in the directory name.
%prep
%setup -q -n %{ur_name}_1_34_0

%build

# Don't build the Boost library; simply install the headers to %{_includedir}.
%install
rm -rf %{buildroot}
install -d -m755 %{buildroot}%{_includedir}/%{ur_name}
cp -R %{ur_name} %{buildroot}%{_includedir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_includedir}/

%changelog
* Mon Nov 3 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
