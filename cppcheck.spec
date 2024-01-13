#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v3
# autospec commit: ab27b0e
#
Name     : cppcheck
Version  : 2.13.1
Release  : 63
URL      : https://github.com/danmar/cppcheck/archive/2.13.1/cppcheck-2.13.1.tar.gz
Source0  : https://github.com/danmar/cppcheck/archive/2.13.1/cppcheck-2.13.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause GPL-3.0 LGPL-3.0 Zlib
Requires: cppcheck-bin = %{version}-%{release}
Requires: cppcheck-data = %{version}-%{release}
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
Requires: cppcheck-data = %{version}-%{release}
Requires: cppcheck-license = %{version}-%{release}

%description bin
bin components for the cppcheck package.


%package data
Summary: data components for the cppcheck package.
Group: Data

%description data
data components for the cppcheck package.


%package license
Summary: license components for the cppcheck package.
Group: Default

%description license
license components for the cppcheck package.


%prep
%setup -q -n cppcheck-2.13.1
cd %{_builddir}/cppcheck-2.13.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1705164022
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
%cmake ..
make  %{?_smp_mflags}
popd
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
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test
cd ../clr-build-avx2;
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
export SOURCE_DATE_EPOCH=1705164022
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cppcheck
cp %{_builddir}/cppcheck-%{version}/COPYING %{buildroot}/usr/share/package-licenses/cppcheck/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/cppcheck-%{version}/externals/picojson/LICENSE %{buildroot}/usr/share/package-licenses/cppcheck/72d61ffe3f9c792cc8790c56aabe0f1a046d8c79 || :
cp %{_builddir}/cppcheck-%{version}/externals/simplecpp/LICENSE %{buildroot}/usr/share/package-licenses/cppcheck/49d4c0ce1a16601f1e265d446b6c5ea6b512f27c || :
cp %{_builddir}/cppcheck-%{version}/externals/tinyxml2/LICENSE %{buildroot}/usr/share/package-licenses/cppcheck/409ff756b1f0bb05818f6ac0996facc6de1dc7d1 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/cppcheck
/usr/bin/cppcheck

%files data
%defattr(-,root,root,-)
/usr/share/Cppcheck/addons/__init__.py
/usr/share/Cppcheck/addons/cppcheck.py
/usr/share/Cppcheck/addons/cppcheckdata.py
/usr/share/Cppcheck/addons/findcasts.py
/usr/share/Cppcheck/addons/misc.py
/usr/share/Cppcheck/addons/misra.py
/usr/share/Cppcheck/addons/misra_9.py
/usr/share/Cppcheck/addons/naming.py
/usr/share/Cppcheck/addons/namingng.py
/usr/share/Cppcheck/addons/runaddon.py
/usr/share/Cppcheck/addons/threadsafety.py
/usr/share/Cppcheck/addons/y2038.py
/usr/share/Cppcheck/cfg/avr.cfg
/usr/share/Cppcheck/cfg/bento4.cfg
/usr/share/Cppcheck/cfg/boost.cfg
/usr/share/Cppcheck/cfg/bsd.cfg
/usr/share/Cppcheck/cfg/cairo.cfg
/usr/share/Cppcheck/cfg/cppcheck-lib.cfg
/usr/share/Cppcheck/cfg/cppunit.cfg
/usr/share/Cppcheck/cfg/dpdk.cfg
/usr/share/Cppcheck/cfg/embedded_sql.cfg
/usr/share/Cppcheck/cfg/emscripten.cfg
/usr/share/Cppcheck/cfg/ginac.cfg
/usr/share/Cppcheck/cfg/gnu.cfg
/usr/share/Cppcheck/cfg/googletest.cfg
/usr/share/Cppcheck/cfg/gtk.cfg
/usr/share/Cppcheck/cfg/icu.cfg
/usr/share/Cppcheck/cfg/kde.cfg
/usr/share/Cppcheck/cfg/libcerror.cfg
/usr/share/Cppcheck/cfg/libcurl.cfg
/usr/share/Cppcheck/cfg/libsigc++.cfg
/usr/share/Cppcheck/cfg/lua.cfg
/usr/share/Cppcheck/cfg/mfc.cfg
/usr/share/Cppcheck/cfg/microsoft_atl.cfg
/usr/share/Cppcheck/cfg/microsoft_sal.cfg
/usr/share/Cppcheck/cfg/microsoft_unittest.cfg
/usr/share/Cppcheck/cfg/motif.cfg
/usr/share/Cppcheck/cfg/nspr.cfg
/usr/share/Cppcheck/cfg/ntl.cfg
/usr/share/Cppcheck/cfg/opencv2.cfg
/usr/share/Cppcheck/cfg/opengl.cfg
/usr/share/Cppcheck/cfg/openmp.cfg
/usr/share/Cppcheck/cfg/openssl.cfg
/usr/share/Cppcheck/cfg/pcre.cfg
/usr/share/Cppcheck/cfg/posix.cfg
/usr/share/Cppcheck/cfg/python.cfg
/usr/share/Cppcheck/cfg/qt.cfg
/usr/share/Cppcheck/cfg/ruby.cfg
/usr/share/Cppcheck/cfg/sdl.cfg
/usr/share/Cppcheck/cfg/sfml.cfg
/usr/share/Cppcheck/cfg/sqlite3.cfg
/usr/share/Cppcheck/cfg/std.cfg
/usr/share/Cppcheck/cfg/tinyxml2.cfg
/usr/share/Cppcheck/cfg/vcl.cfg
/usr/share/Cppcheck/cfg/windows.cfg
/usr/share/Cppcheck/cfg/wxsqlite3.cfg
/usr/share/Cppcheck/cfg/wxsvg.cfg
/usr/share/Cppcheck/cfg/wxwidgets.cfg
/usr/share/Cppcheck/cfg/zephyr.cfg
/usr/share/Cppcheck/cfg/zlib.cfg
/usr/share/Cppcheck/platforms/aix_ppc64.xml
/usr/share/Cppcheck/platforms/arm32-wchar_t2.xml
/usr/share/Cppcheck/platforms/arm32-wchar_t4.xml
/usr/share/Cppcheck/platforms/arm64-wchar_t2.xml
/usr/share/Cppcheck/platforms/arm64-wchar_t4.xml
/usr/share/Cppcheck/platforms/avr8.xml
/usr/share/Cppcheck/platforms/cray_sv1.xml
/usr/share/Cppcheck/platforms/elbrus-e1cp.xml
/usr/share/Cppcheck/platforms/mips32.xml
/usr/share/Cppcheck/platforms/msp430_eabi_large_datamodel.xml
/usr/share/Cppcheck/platforms/pic16.xml
/usr/share/Cppcheck/platforms/pic8-enhanced.xml
/usr/share/Cppcheck/platforms/pic8.xml
/usr/share/Cppcheck/platforms/unix32-unsigned.xml
/usr/share/Cppcheck/platforms/unix64-unsigned.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cppcheck/409ff756b1f0bb05818f6ac0996facc6de1dc7d1
/usr/share/package-licenses/cppcheck/49d4c0ce1a16601f1e265d446b6c5ea6b512f27c
/usr/share/package-licenses/cppcheck/72d61ffe3f9c792cc8790c56aabe0f1a046d8c79
/usr/share/package-licenses/cppcheck/8624bcdae55baeef00cd11d5dfcfa60f68710a02
