%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc
%define bigname Python

Name:		csdms-python
Version:	2.7.6
Release:	2%{?dist}
Summary:	A Python distibution built for use by CSDMS software
Group:		Development/Languages
License:	Python
URL:		http://www.python.org
#Source0:	https://www.python.org/ftp/python/2.7.6/Python-2.7.6.tgz
Source0:	%{name}-%version.tar.gz
BuildRoot:	%{_topdir}/BUILDROOT/%name-%version-%release
Prefix:         %{_prefix}
Autoreq:	0

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
A Python 2.7 distribution that serves as the base for building CSDMS
software tools. This distribution is installed alongside the CSDMS
software stack so it won't interfere with the native Python
distribution on a user's machine. Includes setuptools (post-install).

%prep
%setup -q -n %bigname-%version

%build
%configure --libdir=%{lib32dir}
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 LICENSE README %{buildroot}%{docdir}/%{name}-%{version}/
rm -rf %{buildroot}/usr/share/man/

# Install ez_setup.py to share/.
install -d -m755 %{buildroot}%{_datadir}/%{name}-%{version}
install -m664 %{_sourcedir}/ez_setup.py \
	%{buildroot}%{_datadir}/%{name}-%{version}/

# Install setuptools.
%post
/sbin/ldconfig
%{_bindir}/python %{_datadir}/%{name}-%{version}/ez_setup.py

# Uninstall setuptools.
%preun
rm %{_bindir}/easy_install*
rm %{lib32dir}/python2.7/site-packages/easy-install*
rm %{lib32dir}/python2.7/site-packages/setuptools*

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/
%{_includedir}/
%{_datadir}

%changelog
* Thu Oct 16 2014 Mark Piper <mark.piper@colorado.edu> - 2.7.6-2
- Use %post to install setuptools

* Thu Oct  9 2014 Mark Piper <mark.piper@colorado.edu> - 2.7.6-1
- Initial build
