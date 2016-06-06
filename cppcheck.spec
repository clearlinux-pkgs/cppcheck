#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cppcheck
Version  : 1.74
Release  : 2
URL      : https://github.com/danmar/cppcheck/archive/1.74.tar.gz
Source0  : https://github.com/danmar/cppcheck/archive/1.74.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: cppcheck-bin
Requires: cppcheck-data
BuildRequires : cmake
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : setuptools

%description
==================================
Contents
1. What is Y2038?
2. What is the Y2038 ccpcheck addon?
3. How does the Y2038 cppcheck addon work?
4. How to use the Y2038 cppcheck addon

%package bin
Summary: bin components for the cppcheck package.
Group: Binaries
Requires: cppcheck-data

%description bin
bin components for the cppcheck package.


%package data
Summary: data components for the cppcheck package.
Group: Data

%description data
data components for the cppcheck package.


%prep
%setup -q -n cppcheck-1.74

%build
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=%{_libdir}
make V=1  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd clr-build ; make test ; popd

%install
rm -rf %{buildroot}
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
/usr/share/CppCheck/gnu.cfg
/usr/share/CppCheck/gtk.cfg
/usr/share/CppCheck/microsoft_sal.cfg
/usr/share/CppCheck/posix.cfg
/usr/share/CppCheck/qt.cfg
/usr/share/CppCheck/sdl.cfg
/usr/share/CppCheck/std.cfg
/usr/share/CppCheck/windows.cfg
