%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		coupling
Version:	head
Release:	1%{?dist}
Summary:	Provides services for coupling CSDMS components
Group:		Development/Tools
License:	MIT
URL:		http://csdms.colorado.edu
# The Coupling source can be obtained with `git` from:
# $ git clone git://github.com/csdms/coupling.git
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
A Python package that provides services for coupling CSDMS components.

%prep
%setup -q

%build
%{_bindir}/python setup.py build

%install
rm -rf %{buildroot}
%{_bindir}/python setup.py install -O1 --skip-build --root=%{buildroot} \
		  --record="installed.txt"
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 installed.txt %{buildroot}%{docdir}/%{name}-%{version}/

%check
export PATH=%{_bindir}:$PATH
export PYTHONPATH=$(%{_bindir}/python -c "import site; print site.getsitepackages()[0]"):$PYTHONPATH
export ESMFMKFILE=%{lib32dir}/libO/Linux.gfortran.64.mpiuni.default/esmf.mk
%{_bindir}/nosetests --stop

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/
%{_datadir}/

%changelog
* Tue Oct 21 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
