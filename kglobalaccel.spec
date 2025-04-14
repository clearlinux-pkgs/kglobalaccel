#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v24
# autospec commit: a88ffdc
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kglobalaccel
Version  : 6.13.0
Release  : 95
URL      : https://download.kde.org/stable/frameworks/6.13/kglobalaccel-6.13.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.13/kglobalaccel-6.13.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.13/kglobalaccel-6.13.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : Add support for global workspace shortcuts
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0
Requires: kglobalaccel-data = %{version}-%{release}
Requires: kglobalaccel-lib = %{version}-%{release}
Requires: kglobalaccel-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : qt6base-dev
BuildRequires : xcb-util-keysyms-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KGlobalAccel
Global desktop keyboard shortcuts
## Introduction
KGlobalAccel allows you to have global accelerators that are independent of
the focused window.  Unlike regular shortcuts, the application's window does not
need focus for them to be activated.

%package data
Summary: data components for the kglobalaccel package.
Group: Data

%description data
data components for the kglobalaccel package.


%package dev
Summary: dev components for the kglobalaccel package.
Group: Development
Requires: kglobalaccel-lib = %{version}-%{release}
Requires: kglobalaccel-data = %{version}-%{release}
Provides: kglobalaccel-devel = %{version}-%{release}
Requires: kglobalaccel = %{version}-%{release}

%description dev
dev components for the kglobalaccel package.


%package lib
Summary: lib components for the kglobalaccel package.
Group: Libraries
Requires: kglobalaccel-data = %{version}-%{release}
Requires: kglobalaccel-license = %{version}-%{release}

%description lib
lib components for the kglobalaccel package.


%package license
Summary: license components for the kglobalaccel package.
Group: Default

%description license
license components for the kglobalaccel package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kglobalaccel-6.13.0
cd %{_builddir}/kglobalaccel-6.13.0
pushd ..
cp -a kglobalaccel-6.13.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1744639977
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
export SOURCE_DATE_EPOCH=1744639977
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kglobalaccel
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/20079e8f79713dce80ab09774505773c926afa2a || :
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

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf6_org.kde.KGlobalAccel.xml
/usr/share/dbus-1/interfaces/kf6_org.kde.kglobalaccel.Component.xml
/usr/share/locale/af/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/as/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/az/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/be/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/br/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/da/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/de/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/el/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/es/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/et/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/he/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/id/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/is/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/it/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/km/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/or/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sa/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/se/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/si/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/te/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/th/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kglobalaccel6_qt.qm
/usr/share/qlogging-categories6/kglobalaccel.categories
/usr/share/qlogging-categories6/kglobalaccel.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/KGlobalAccel/KGlobalAccel
/usr/include/KF6/KGlobalAccel/KGlobalShortcutInfo
/usr/include/KF6/KGlobalAccel/kglobalaccel.h
/usr/include/KF6/KGlobalAccel/kglobalaccel_export.h
/usr/include/KF6/KGlobalAccel/kglobalaccel_version.h
/usr/include/KF6/KGlobalAccel/kglobalshortcutinfo.h
/usr/lib64/cmake/KF6GlobalAccel/KF6GlobalAccelConfig.cmake
/usr/lib64/cmake/KF6GlobalAccel/KF6GlobalAccelConfigVersion.cmake
/usr/lib64/cmake/KF6GlobalAccel/KF6GlobalAccelTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6GlobalAccel/KF6GlobalAccelTargets.cmake
/usr/lib64/libKF6GlobalAccel.so

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6GlobalAccel.so.6.13.0
/usr/lib64/libKF6GlobalAccel.so.6
/usr/lib64/libKF6GlobalAccel.so.6.13.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kglobalaccel/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kglobalaccel/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
