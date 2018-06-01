#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isa-l
Version  : 2.22.0
Release  : 22
URL      : https://github.com/01org/isa-l/archive/v2.22.0.tar.gz
Source0  : https://github.com/01org/isa-l/archive/v2.22.0.tar.gz
Summary  : Library for storage systems
Group    : Development/Tools
License  : BSD-3-Clause
Requires: isa-l-lib
BuildRequires : nasm
BuildRequires : sed
BuildRequires : yasm
Patch1: build.patch

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
%setup -q -n isa-l-2.22.0
%patch1 -p1
pushd ..
cp -a isa-l-2.22.0 buildavx2
popd
pushd ..
cp -a isa-l-2.22.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527840781
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%reconfigure --disable-static    --libdir=/usr/lib64/haswell --bindir=/usr/bin/haswell
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export CXXFLAGS="$CXXFLAGS -m64 -march=skylake-avx512 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=skylake-avx512"
%reconfigure --disable-static    --libdir=/usr/lib64/haswell/avx512_1 --bindir=/usr/bin/haswell/avx512_1
make  %{?_smp_mflags}
popd

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1527840781
rm -rf %{buildroot}
pushd ../buildavx2/
%make_install
popd
pushd ../buildavx512/
%make_install
popd
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
/usr/lib64/haswell/libisal.so
/usr/lib64/libisal.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libisal.so
/usr/lib64/haswell/avx512_1/libisal.so.2
/usr/lib64/haswell/avx512_1/libisal.so.2.0.22
/usr/lib64/haswell/libisal.so.2
/usr/lib64/haswell/libisal.so.2.0.22
/usr/lib64/libisal.so.2
/usr/lib64/libisal.so.2.0.22
