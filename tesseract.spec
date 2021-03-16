#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tesseract
Version  : 4.1.1
Release  : 6
URL      : https://github.com/tesseract-ocr/tesseract/archive/4.1.1/tesseract-4.1.1.tar.gz
Source0  : https://github.com/tesseract-ocr/tesseract/archive/4.1.1/tesseract-4.1.1.tar.gz
Summary  : An OCR Engine that was developed at HP Labs between 1985 and 1995... and now at Google.
Group    : Development/Tools
License  : Apache-2.0
Requires: tesseract-bin = %{version}-%{release}
Requires: tesseract-data = %{version}-%{release}
Requires: tesseract-lib = %{version}-%{release}
Requires: tesseract-license = %{version}-%{release}
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : buildreq-cmake
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(icu-i18n)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(lept)
BuildRequires : pkgconfig(libarchive)
BuildRequires : pkgconfig(libcurl)
BuildRequires : pkgconfig(pango)
BuildRequires : tiff-dev
Patch1: 0001-Do-not-use-native.patch
Patch2: 0002-Make-tesseract.pc-depend-on-libarchive-libcurl-.pc.patch

%description
# Tesseract OCR
[![Build Status](https://travis-ci.org/tesseract-ocr/tesseract.svg?branch=master)](https://travis-ci.org/tesseract-ocr/tesseract)
[![Build status](https://ci.appveyor.com/api/projects/status/miah0ikfsf0j3819/branch/master?svg=true)](https://ci.appveyor.com/project/zdenop/tesseract/)<br>
[![Coverity Scan Build Status](https://scan.coverity.com/projects/tesseract-ocr/badge.svg)](https://scan.coverity.com/projects/tesseract-ocr)
[![Code Quality: Cpp](https://img.shields.io/lgtm/grade/cpp/g/tesseract-ocr/tesseract.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tesseract-ocr/tesseract/context:cpp)
[![Total Alerts](https://img.shields.io/lgtm/alerts/g/tesseract-ocr/tesseract.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/tesseract-ocr/tesseract/alerts)<br/>
[![GitHub license](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](https://raw.githubusercontent.com/tesseract-ocr/tesseract/master/LICENSE)
[![Downloads](https://img.shields.io/badge/download-all%20releases-brightgreen.svg)](https://github.com/tesseract-ocr/tesseract/releases/)

%package bin
Summary: bin components for the tesseract package.
Group: Binaries
Requires: tesseract-data = %{version}-%{release}
Requires: tesseract-license = %{version}-%{release}

%description bin
bin components for the tesseract package.


%package data
Summary: data components for the tesseract package.
Group: Data

%description data
data components for the tesseract package.


%package dev
Summary: dev components for the tesseract package.
Group: Development
Requires: tesseract-lib = %{version}-%{release}
Requires: tesseract-bin = %{version}-%{release}
Requires: tesseract-data = %{version}-%{release}
Provides: tesseract-devel = %{version}-%{release}
Requires: tesseract = %{version}-%{release}

%description dev
dev components for the tesseract package.


%package lib
Summary: lib components for the tesseract package.
Group: Libraries
Requires: tesseract-data = %{version}-%{release}
Requires: tesseract-license = %{version}-%{release}

%description lib
lib components for the tesseract package.


%package license
Summary: license components for the tesseract package.
Group: Default

%description license
license components for the tesseract package.


%prep
%setup -q -n tesseract-4.1.1
cd %{_builddir}/tesseract-4.1.1
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1605640913
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%autogen --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1605640913
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tesseract
cp %{_builddir}/tesseract-4.1.1/LICENSE %{buildroot}/usr/share/package-licenses/tesseract/2b8b815229aa8a61e483fb4ba0588b8b6c491890
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tesseract

%files data
%defattr(-,root,root,-)
/usr/share/tessdata/configs/alto
/usr/share/tessdata/configs/ambigs.train
/usr/share/tessdata/configs/api_config
/usr/share/tessdata/configs/bigram
/usr/share/tessdata/configs/box.train
/usr/share/tessdata/configs/box.train.stderr
/usr/share/tessdata/configs/digits
/usr/share/tessdata/configs/get.images
/usr/share/tessdata/configs/hocr
/usr/share/tessdata/configs/inter
/usr/share/tessdata/configs/kannada
/usr/share/tessdata/configs/linebox
/usr/share/tessdata/configs/logfile
/usr/share/tessdata/configs/lstm.train
/usr/share/tessdata/configs/lstmbox
/usr/share/tessdata/configs/lstmdebug
/usr/share/tessdata/configs/makebox
/usr/share/tessdata/configs/pdf
/usr/share/tessdata/configs/quiet
/usr/share/tessdata/configs/rebox
/usr/share/tessdata/configs/strokewidth
/usr/share/tessdata/configs/tsv
/usr/share/tessdata/configs/txt
/usr/share/tessdata/configs/unlv
/usr/share/tessdata/configs/wordstrbox
/usr/share/tessdata/pdf.ttf
/usr/share/tessdata/tessconfigs/batch
/usr/share/tessdata/tessconfigs/batch.nochop
/usr/share/tessdata/tessconfigs/matdemo
/usr/share/tessdata/tessconfigs/msdemo
/usr/share/tessdata/tessconfigs/nobatch
/usr/share/tessdata/tessconfigs/segdemo

%files dev
%defattr(-,root,root,-)
/usr/include/tesseract/apitypes.h
/usr/include/tesseract/baseapi.h
/usr/include/tesseract/capi.h
/usr/include/tesseract/genericvector.h
/usr/include/tesseract/helpers.h
/usr/include/tesseract/ltrresultiterator.h
/usr/include/tesseract/ocrclass.h
/usr/include/tesseract/osdetect.h
/usr/include/tesseract/pageiterator.h
/usr/include/tesseract/platform.h
/usr/include/tesseract/publictypes.h
/usr/include/tesseract/renderer.h
/usr/include/tesseract/resultiterator.h
/usr/include/tesseract/serialis.h
/usr/include/tesseract/strngs.h
/usr/include/tesseract/tess_version.h
/usr/include/tesseract/tesscallback.h
/usr/include/tesseract/thresholder.h
/usr/include/tesseract/unichar.h
/usr/lib64/libtesseract.so
/usr/lib64/pkgconfig/tesseract.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtesseract.so.4
/usr/lib64/libtesseract.so.4.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tesseract/2b8b815229aa8a61e483fb4ba0588b8b6c491890
