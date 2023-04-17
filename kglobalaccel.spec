#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kglobalaccel
Version  : 5.105.0
Release  : 63
URL      : https://download.kde.org/stable/frameworks/5.105/kglobalaccel-5.105.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.105/kglobalaccel-5.105.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.105/kglobalaccel-5.105.0.tar.xz.sig
Summary  : Add support for global workspace shortcuts
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: kglobalaccel-bin = %{version}-%{release}
Requires: kglobalaccel-data = %{version}-%{release}
Requires: kglobalaccel-lib = %{version}-%{release}
Requires: kglobalaccel-license = %{version}-%{release}
Requires: kglobalaccel-services = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kwindowsystem-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev
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

%package bin
Summary: bin components for the kglobalaccel package.
Group: Binaries
Requires: kglobalaccel-data = %{version}-%{release}
Requires: kglobalaccel-license = %{version}-%{release}
Requires: kglobalaccel-services = %{version}-%{release}

%description bin
bin components for the kglobalaccel package.


%package data
Summary: data components for the kglobalaccel package.
Group: Data

%description data
data components for the kglobalaccel package.


%package dev
Summary: dev components for the kglobalaccel package.
Group: Development
Requires: kglobalaccel-lib = %{version}-%{release}
Requires: kglobalaccel-bin = %{version}-%{release}
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


%package services
Summary: services components for the kglobalaccel package.
Group: Systemd services
Requires: systemd

%description services
services components for the kglobalaccel package.


%prep
%setup -q -n kglobalaccel-5.105.0
cd %{_builddir}/kglobalaccel-5.105.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1681741602
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1681741602
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kglobalaccel
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kglobalaccel-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kglobalaccel/e458941548e0864907e654fa2e192844ae90fc32 || :
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kglobalaccel5

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/kf5_org.kde.KGlobalAccel.xml
/usr/share/dbus-1/interfaces/kf5_org.kde.kglobalaccel.Component.xml
/usr/share/dbus-1/services/org.kde.kglobalaccel.service
/usr/share/kservices5/kglobalaccel5.desktop
/usr/share/locale/af/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ar/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/as/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/az/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/be/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/be@latin/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/bg/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/bn/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/bn_IN/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/br/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/bs/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ca/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/crh/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/cs/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/csb/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/cy/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/da/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/de/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/el/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/eo/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/es/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/et/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/eu/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/fa/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/fi/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/fr/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/fy/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ga/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/gd/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/gl/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/gu/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ha/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/he/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/hi/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/hne/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/hr/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/hsb/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/hu/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/hy/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ia/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/id/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/is/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/it/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ja/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ka/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/kk/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/km/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/kn/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ko/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ku/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/lb/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/lt/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/lv/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/mai/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/mk/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ml/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/mr/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ms/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/nb/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/nds/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ne/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/nl/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/nn/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/oc/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/or/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/pa/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/pl/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ps/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/pt/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ro/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ru/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/se/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/si/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sk/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sl/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sq/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sr/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/sv/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ta/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/te/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/tg/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/th/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/tr/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/tt/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/ug/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/uk/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/uz/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/uz@cyrillic/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/vi/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/wa/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/xh/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/zh_HK/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/kglobalaccel5_qt.qm
/usr/share/qlogging-categories5/kglobalaccel.categories
/usr/share/qlogging-categories5/kglobalaccel.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KGlobalAccel/KGlobalAccel
/usr/include/KF5/KGlobalAccel/KGlobalShortcutInfo
/usr/include/KF5/KGlobalAccel/kglobalaccel.h
/usr/include/KF5/KGlobalAccel/kglobalaccel_export.h
/usr/include/KF5/KGlobalAccel/kglobalaccel_version.h
/usr/include/KF5/KGlobalAccel/kglobalshortcutinfo.h
/usr/include/KF5/KGlobalAccel/private/kf5globalaccelprivate_export.h
/usr/include/KF5/KGlobalAccel/private/kglobalaccel_interface.h
/usr/include/KF5/KGlobalAccel/private/kglobalacceld.h
/usr/lib64/cmake/KF5GlobalAccel/KF5GlobalAccelConfig.cmake
/usr/lib64/cmake/KF5GlobalAccel/KF5GlobalAccelConfigVersion.cmake
/usr/lib64/cmake/KF5GlobalAccel/KF5GlobalAccelTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5GlobalAccel/KF5GlobalAccelTargets.cmake
/usr/lib64/libKF5GlobalAccel.so
/usr/lib64/qt5/mkspecs/modules/qt_KGlobalAccel.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5GlobalAccel.so.5
/usr/lib64/libKF5GlobalAccel.so.5.105.0
/usr/lib64/libKF5GlobalAccelPrivate.so.5
/usr/lib64/libKF5GlobalAccelPrivate.so.5.105.0
/usr/lib64/qt5/plugins/org.kde.kglobalaccel5.platforms/KF5GlobalAccelPrivateXcb.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kglobalaccel/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kglobalaccel/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kglobalaccel/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kglobalaccel/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kglobalaccel/e458941548e0864907e654fa2e192844ae90fc32

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/user/plasma-kglobalaccel.service
