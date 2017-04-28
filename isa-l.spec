#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isa-l
Version  : 2.18.0
Release  : 13
URL      : https://github.com/01org/isa-l/archive/v2.18.0.tar.gz
Source0  : https://github.com/01org/isa-l/archive/v2.18.0.tar.gz
Summary  : Library for storage systems
Group    : Development/Tools
License  : BSD-3-Clause
Requires: isa-l-lib
BuildRequires : nasm
BuildRequires : sed
BuildRequires : yasm

%description
Intel(R) Intelligent Storage Acceleration Library
=================================================

%package dev
Summary: dev components for the isa-l package.
Group: Development
Requires: isa-l-lib
Provides: isa-l-devel

%description dev
dev components for the isa-l package.


%package lib
Summary: lib components for the isa-l package.
Group: Libraries

%description lib
lib components for the isa-l package.


%prep
%setup -q -n isa-l-2.18.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1493392142
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto -fno-semantic-interposition "
%reconfigure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493392142
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/isa-l/crc.h
/usr/include/isa-l/crc64.h
/usr/include/isa-l/erasure_code.h
/usr/include/isa-l/gf_vect_mul.h
/usr/include/isa-l/igzip_lib.h
/usr/include/isa-l/raid.h
/usr/include/isa-l/test.h
/usr/include/isa-l/types.h
/usr/lib64/libisal.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libisal.so.2
/usr/lib64/libisal.so.2.0.18
