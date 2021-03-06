%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		ccaffeine
Version:	0.8.8
Release:	2%{?dist}
Summary:	A Common Component Architecture framework for parallel computing
Group:		Applications/Engineering
License:	Other
URL:		http://www.cca-forum.org
Source0:	http://www.cca-forum.org/download/cca-tools/cca-tools-latest/ccaffeine-0.8.8.tar.gz
# This patch includes $DESTDIR in the Makefile for a staged install.
Patch0:		%{name}-use-DESTDIR-in-Makefile.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
Ccaffeine is a Common Component Architecture prototype framework for
distributed memory message passing high performance computing.  The
Ccaffeine executable orchestrates a set of SCMD (Single Component
Multiple Data) components on a parallel machine. It has the ability to
instantiate, connect and run components interactively or in batch
mode. Additionally, it has debug mode that runs as a single processor
serial program. Ccaffeine is largely a product of the High Performance
Computing Research Division at Sandia National Labs in Livermore, but
also has benefited from many contributions from other labs and
universities.

%prep
%setup -q
%patch0

# Following babel, allow ccaffeine to install in %{lib32dir}.
# The install location of cca-spec-babel and the Boost libraries
# should be /usr/local/csdms.
%build
%configure --disable-doc \
	   --libdir=%{lib32dir} \
	   --with-cca-babel=%{_prefix} \
	   --with-babel-libtool=%{_bindir}/babel-libtool \
	   --without-mpi \
	   --with-boost=%{_includedir}
make # deparallelize

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 A.GETTING.STARTED.html Changelog.* DEVELOPER README* TODO-list \
	%{buildroot}%{docdir}/%{name}-%{version}/

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/
%{_includedir}/
%{_datadir}/
%{lib32dir}/

%changelog
* Mon Nov  3 2014 Mark Piper <mark.piper@colorado.edu> - 0.8.8-2
- Provide headers for Boost libraries as a CSDMS package

* Thu Oct 2 2014 Mark Piper <mark.piper@colorado.edu>
- Initial build
