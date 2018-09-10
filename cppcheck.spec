#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cppcheck
Version  : 1.84
Release  : 20
URL      : https://github.com/danmar/cppcheck/archive/1.84.tar.gz
Source0  : https://github.com/danmar/cppcheck/archive/1.84.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: cppcheck-bin
Requires: cppcheck-data
Requires: cppcheck-license
Requires: Pygments
BuildRequires : Pygments
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-qmake
BuildRequires : cmake(Qt5Core)
BuildRequires : cmake(Qt5Gui)
BuildRequires : cmake(Qt5PrintSupport)
BuildRequires : cmake(Qt5Widgets)
BuildRequires : python3
BuildRequires : qttools-dev

%description
==================================
Contents
1. What is Y2038?
2. What is the Y2038 cppcheck addon?
3. How does the Y2038 cppcheck addon work?
4. How to use the Y2038 cppcheck addon

%package bin
Summary: bin components for the cppcheck package.
Group: Binaries
Requires: cppcheck-data
Requires: cppcheck-license

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
%setup -q -n cppcheck-1.84

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536563768
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1536563768
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/cppcheck
cp COPYING %{buildroot}/usr/share/doc/cppcheck/COPYING
cp externals/simplecpp/LICENSE %{buildroot}/usr/share/doc/cppcheck/externals_simplecpp_LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/cppcheck

%files data
%defattr(-,root,root,-)
/usr/share/CppCheck/avr.cfg
/usr/share/CppCheck/bsd.cfg
/usr/share/CppCheck/cppcheck-lib.cfg
/usr/share/CppCheck/embedded_sql.cfg
/usr/share/CppCheck/gnu.cfg
/usr/share/CppCheck/gtk.cfg
/usr/share/CppCheck/microsoft_sal.cfg
/usr/share/CppCheck/motif.cfg
/usr/share/CppCheck/posix.cfg
/usr/share/CppCheck/qt.cfg
/usr/share/CppCheck/sdl.cfg
/usr/share/CppCheck/sfml.cfg
/usr/share/CppCheck/std.cfg
/usr/share/CppCheck/windows.cfg
/usr/share/CppCheck/wxwidgets.cfg

%files license
%defattr(-,root,root,-)
/usr/share/doc/cppcheck/COPYING
/usr/share/doc/cppcheck/externals_simplecpp_LICENSE
