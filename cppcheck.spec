#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v18
# autospec commit: f35655a
#
Name     : cppcheck
Version  : 2.15.0
Release  : 71
URL      : https://github.com/danmar/cppcheck/archive/2.15.0/cppcheck-2.15.0.tar.gz
Source0  : https://github.com/danmar/cppcheck/archive/2.15.0/cppcheck-2.15.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-3.0 Zlib
Requires: cppcheck-bin = %{version}-%{release}
Requires: cppcheck-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : glibc-dev
BuildRequires : python3
BuildRequires : qtbase-dev mesa-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# **Cppcheck**
OSS-Fuzz|Coverity Scan Build Status|License|
|:--:|:--:|:--:|
[![OSS-Fuzz](https://oss-fuzz-build-logs.storage.googleapis.com/badges/cppcheck.svg)](https://bugs.chromium.org/p/oss-fuzz/issues/list?sort=-opened&can=1&q=proj:cppcheck)|[![Coverity Scan Build Status](https://img.shields.io/coverity/scan/512.svg)](https://scan.coverity.com/projects/512)|[![License](https://img.shields.io/badge/license-GPL3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)

%package bin
Summary: bin components for the cppcheck package.
Group: Binaries
Requires: cppcheck-license = %{version}-%{release}

%description bin
bin components for the cppcheck package.


%package license
Summary: license components for the cppcheck package.
Group: Default

%description license
license components for the cppcheck package.


%prep
%setup -q -n cppcheck-2.15.0
cd %{_builddir}/cppcheck-2.15.0
pushd ..
cp -a cppcheck-2.15.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1725123293
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../../buildavx2/clr-build-avx2;
make test || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1725123293
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cppcheck
cp %{_builddir}/cppcheck-%{version}/COPYING %{buildroot}/usr/share/package-licenses/cppcheck/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/cppcheck-%{version}/externals/picojson/LICENSE %{buildroot}/usr/share/package-licenses/cppcheck/72d61ffe3f9c792cc8790c56aabe0f1a046d8c79 || :
cp %{_builddir}/cppcheck-%{version}/externals/tinyxml2/LICENSE %{buildroot}/usr/share/package-licenses/cppcheck/409ff756b1f0bb05818f6ac0996facc6de1dc7d1 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/OFF/addons/__init__.py
/usr/OFF/addons/cppcheck.py
/usr/OFF/addons/cppcheckdata.py
/usr/OFF/addons/findcasts.py
/usr/OFF/addons/misc.py
/usr/OFF/addons/misra.py
/usr/OFF/addons/misra_9.py
/usr/OFF/addons/naming.py
/usr/OFF/addons/namingng.py
/usr/OFF/addons/runaddon.py
/usr/OFF/addons/threadsafety.py
/usr/OFF/addons/y2038.py
/usr/OFF/cfg/avr.cfg
/usr/OFF/cfg/bento4.cfg
/usr/OFF/cfg/boost.cfg
/usr/OFF/cfg/bsd.cfg
/usr/OFF/cfg/cairo.cfg
/usr/OFF/cfg/cppcheck-lib.cfg
/usr/OFF/cfg/cppunit.cfg
/usr/OFF/cfg/dpdk.cfg
/usr/OFF/cfg/embedded_sql.cfg
/usr/OFF/cfg/emscripten.cfg
/usr/OFF/cfg/ginac.cfg
/usr/OFF/cfg/gnu.cfg
/usr/OFF/cfg/googletest.cfg
/usr/OFF/cfg/gtk.cfg
/usr/OFF/cfg/icu.cfg
/usr/OFF/cfg/kde.cfg
/usr/OFF/cfg/libcerror.cfg
/usr/OFF/cfg/libcurl.cfg
/usr/OFF/cfg/libsigc++.cfg
/usr/OFF/cfg/lua.cfg
/usr/OFF/cfg/mfc.cfg
/usr/OFF/cfg/microsoft_atl.cfg
/usr/OFF/cfg/microsoft_sal.cfg
/usr/OFF/cfg/microsoft_unittest.cfg
/usr/OFF/cfg/motif.cfg
/usr/OFF/cfg/nspr.cfg
/usr/OFF/cfg/ntl.cfg
/usr/OFF/cfg/opencv2.cfg
/usr/OFF/cfg/opengl.cfg
/usr/OFF/cfg/openmp.cfg
/usr/OFF/cfg/openssl.cfg
/usr/OFF/cfg/pcre.cfg
/usr/OFF/cfg/posix.cfg
/usr/OFF/cfg/protobuf.cfg
/usr/OFF/cfg/python.cfg
/usr/OFF/cfg/qt.cfg
/usr/OFF/cfg/ruby.cfg
/usr/OFF/cfg/sdl.cfg
/usr/OFF/cfg/selinux.cfg
/usr/OFF/cfg/sfml.cfg
/usr/OFF/cfg/sqlite3.cfg
/usr/OFF/cfg/std.cfg
/usr/OFF/cfg/tinyxml2.cfg
/usr/OFF/cfg/vcl.cfg
/usr/OFF/cfg/windows.cfg
/usr/OFF/cfg/wxsqlite3.cfg
/usr/OFF/cfg/wxsvg.cfg
/usr/OFF/cfg/wxwidgets.cfg
/usr/OFF/cfg/zephyr.cfg
/usr/OFF/cfg/zlib.cfg
/usr/OFF/platforms/aix_ppc64.xml
/usr/OFF/platforms/arm32-wchar_t2.xml
/usr/OFF/platforms/arm32-wchar_t4.xml
/usr/OFF/platforms/arm64-wchar_t2.xml
/usr/OFF/platforms/arm64-wchar_t4.xml
/usr/OFF/platforms/avr8.xml
/usr/OFF/platforms/cray_sv1.xml
/usr/OFF/platforms/elbrus-e1cp.xml
/usr/OFF/platforms/mips32.xml
/usr/OFF/platforms/msp430_eabi_large_datamodel.xml
/usr/OFF/platforms/pic16.xml
/usr/OFF/platforms/pic8-enhanced.xml
/usr/OFF/platforms/pic8.xml
/usr/OFF/platforms/unix32-unsigned.xml
/usr/OFF/platforms/unix64-unsigned.xml

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cppcheck
/usr/bin/cppcheck

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cppcheck/409ff756b1f0bb05818f6ac0996facc6de1dc7d1
/usr/share/package-licenses/cppcheck/72d61ffe3f9c792cc8790c56aabe0f1a046d8c79
/usr/share/package-licenses/cppcheck/8624bcdae55baeef00cd11d5dfcfa60f68710a02
