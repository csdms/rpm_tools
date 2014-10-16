%define lib32dir %{_prefix}/lib
%define docdir %{_datadir}/doc

Name:		cmi
Version:	%{_version}
Release:	2%{?dist}
Summary:	Component wrappers for the Component Modeling Interface
Group:		Applications/Engineering
License:	MIT
URL:		http://csdms.colorado.edu
# The CMI source can be obtained with `git` from:
# $ git clone git://github.com/csdms/cmi.git
Source0:	%{name}-%{version}.tar.gz
# These patches include $DESTDIR in two Makefiles for a staged install.
Patch0:		%{name}-use-DESTDIR-in-Makefile.patch
Patch1:		%{name}-use-DESTDIR-in-make.vars.common.in.patch
BuildRoot:	%{_topdir}/BUILDROOT/%{name}-%{version}-%{release}
Prefix:         %{_prefix}

%if 0%{?_buildrequires:1}
BuildRequires:	%{_buildrequires}
%endif

%description
The Component Modeling Interface (CMI) wraps any model that provides a
Basic Model Interface (BMI) to create a CSDMS plug-and-play component.

%prep
%setup -q -n %{name}

%build
export PATH=$CSDMS_DIR/bin:$PATH
export PKG_CONFIG_PATH=$CSDMS_DIR/lib/pkgconfig
export AVULSION_CPPFLAGS=$(pkg-config --cflags avulsion)
export AVULSION_LDFLAGS=$(pkg-config --libs avulsion)
export CEM_CPPFLAGS=$(pkg-config --cflags deltas)
export CEM_LDFLAGS=$(pkg-config --libs deltas)
export CHILD_CPPFLAGS=$(pkg-config --cflags child)
export CHILD_LDFLAGS=$(pkg-config --libs child)
export HYDROTREND_CPPFLAGS=$(pkg-config --cflags hydrotrend)
export HYDROTREND_LDFLAGS=$(pkg-config --libs hydrotrend)
export PLUME_CPPFLAGS=$(pkg-config --cflags plume)
export PLUME_LDFLAGS=$(pkg-config --libs plume)
export SEDFLUX2D_CPPFLAGS=$(pkg-config --cflags sedflux2d)
export SEDFLUX2D_LDFLAGS=$(pkg-config --libs sedflux2d)
export SEDFLUX3D_CPPFLAGS=$(pkg-config --cflags sedflux3d)
export SEDFLUX3D_LDFLAGS=$(pkg-config --libs sedflux3d)
export WAVES_CPPFLAGS=$(pkg-config --cflags waves)
export WAVES_LDFLAGS=$(pkg-config --libs waves)
export PYTHONPATH=$($CSDMS_PYTHON -c "import site; print site.getsitepackages()[0]"):$PYTHONPATH
%cmake .
make just_hydrotrend
cd csdms
patch -i %{_sourcedir}/%{name}-use-DESTDIR-in-Makefile.patch
patch -p0 -i %{_sourcedir}/%{name}-use-DESTDIR-in-make.vars.common.in.patch
%configure --libdir=%{lib32dir}
make

%install
rm -rf %{buildroot}
cd csdms
make DESTDIR=%{buildroot} install
cd %{_builddir}/%{name}
install -d -m755 %{buildroot}%{docdir}/%{name}-%{version}
install -m664 INSTALL.md LICENSE README.md \
	%{buildroot}%{docdir}/%{name}-%{version}/

# Replace ".la" with ".so" in share/cca/*.cca files.
sed -i 's@\.la@.so@' %{buildroot}%{_datadir}/cca/*.cca

# Remove bogus %{buildroot} path from share/cca/*.cca and lib/*.la files.
sed -i 's@%{buildroot}@@' %{buildroot}%{_datadir}/cca/*.cca
sed -i 's@%{buildroot}@@g' %{buildroot}%{lib32dir}/*.la

%check
cd csdms
make check

%post -p /sbin/ldconfig
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
* Thu Oct 16 2014 Mark Piper <mpiper@siwenna.colorado.edu> - %{_version}-2
- Remove bogus %{buildroot} paths from output

* Tue Oct 14 2014 Mark Piper <mark.piper@colorado.edu> - %{_version}-1
- Initial build
