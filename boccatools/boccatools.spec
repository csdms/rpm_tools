%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		bocca
Version:	0.5.7
Release:	1%{?dist}
Summary:	A CCA tool for managing a set of SIDL-based entities
Group:		Applications/Engineering
License:	Other
URL:		http://www.cca-forum.org
Source0:	http://www.cca-forum.org/download/cca-tools/cca-tools-latest/bocca-0.5.7.tar.gz
# This patch includes $DESTDIR in the Makefile for a staged install.
Patch0:		%{name}-use-DESTDIR-in-Makefile.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Bocca is a tool in the CCA tool chain that was designed to help users
create, edit, and manage a set of SIDL-based entities, including the
CCA components and ports associated with a particular project. Bocca
was developed to address usability concerns and reduce the development
effort required to implement multilanguage component
applications. Bocca was designed specifically to free users from
mundane, time-consuming, low-level tasks so they can focus on the
scientific aspects of their applications. It can be viewed as a
development environment tool that allows application developers to
perform rapid component prototyping while maintaining robust software
engineering practices suitable to HPC environments.

%prep
%setup -q
%patch0

# Following babel, allow bocca to install libraries in %{lib32dir}.
# The package install location should be /usr/local/csdms.
# Python 2.7 is required for the CSDMS software stack.
%build
%configure --libdir=%{lib32dir} \
	   --with-ccafe-config=%{_prefix}/bin/ccafe-config \
	   --with-cca-spec-babel-config=%{_prefix}/bin/cca-spec-babel-config \
	   --with-babel-config=%{_prefix}/bin/babel-config \
	   --with-python=/usr/local/bin/python2.7
make build %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 proposed.LICENSE.bocca.txt README TODO \
	%{buildroot}%{docdir}/%{name}-%{version}/
mv %{buildroot}/%{_prefix}/share/doc/*.html \
   %{buildroot}%{docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{lib32dir}/
%{docdir}/

%changelog
* Mon Oct 6 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
