#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : isa-l
Version  : 2.30.0
Release  : 41
URL      : https://github.com/01org/isa-l/archive/v2.30.0/isa-l-2.30.0.tar.gz
Source0  : https://github.com/01org/isa-l/archive/v2.30.0/isa-l-2.30.0.tar.gz
Summary  : Library for storage systems
Group    : Development/Tools
License  : BSD-3-Clause
Requires: isa-l-bin = %{version}-%{release}
Requires: isa-l-filemap = %{version}-%{release}
Requires: isa-l-lib = %{version}-%{release}
Requires: isa-l-license = %{version}-%{release}
Requires: isa-l-man = %{version}-%{release}
BuildRequires : nasm
BuildRequires : sed
BuildRequires : yasm

%description
Intel(R) Intelligent Storage Acceleration Library
=================================================

%package bin
Summary: bin components for the isa-l package.
Group: Binaries
Requires: isa-l-license = %{version}-%{release}
Requires: isa-l-filemap = %{version}-%{release}

%description bin
bin components for the isa-l package.


%package dev
Summary: dev components for the isa-l package.
Group: Development
Requires: isa-l-lib = %{version}-%{release}
Requires: isa-l-bin = %{version}-%{release}
Provides: isa-l-devel = %{version}-%{release}
Requires: isa-l = %{version}-%{release}

%description dev
dev components for the isa-l package.


%package filemap
Summary: filemap components for the isa-l package.
Group: Default

%description filemap
filemap components for the isa-l package.


%package lib
Summary: lib components for the isa-l package.
Group: Libraries
Requires: isa-l-license = %{version}-%{release}
Requires: isa-l-filemap = %{version}-%{release}

%description lib
lib components for the isa-l package.


%package license
Summary: license components for the isa-l package.
Group: Default

%description license
license components for the isa-l package.


%package man
Summary: man components for the isa-l package.
Group: Default

%description man
man components for the isa-l package.


%prep
%setup -q -n isa-l-2.30.0
cd %{_builddir}/isa-l-2.30.0
pushd ..
cp -a isa-l-2.30.0 buildavx2
popd
pushd ..
cp -a isa-l-2.30.0 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656126966
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
%reconfigure --disable-static
make  %{?_smp_mflags}
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256 -Wl,-z,x86-64-v4"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=256"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%reconfigure --disable-static
make  %{?_smp_mflags}
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :
cd ../buildavx512;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656126966
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/isa-l
cp %{_builddir}/isa-l-2.30.0/LICENSE %{buildroot}/usr/share/package-licenses/isa-l/c41999097043083c4213a15101a122f1401e41df
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/igzip
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/isa-l.h
/usr/include/isa-l/crc.h
/usr/include/isa-l/crc64.h
/usr/include/isa-l/erasure_code.h
/usr/include/isa-l/gf_vect_mul.h
/usr/include/isa-l/igzip_lib.h
/usr/include/isa-l/mem_routines.h
/usr/include/isa-l/raid.h
/usr/include/isa-l/test.h
/usr/include/isa-l/types.h
/usr/lib64/libisal.so
/usr/lib64/pkgconfig/libisal.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-isa-l

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libisal.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libisal.so.2
/usr/lib64/glibc-hwcaps/x86-64-v3/libisal.so.2.0.30
/usr/lib64/glibc-hwcaps/x86-64-v4/libisal.so
/usr/lib64/glibc-hwcaps/x86-64-v4/libisal.so.2
/usr/lib64/glibc-hwcaps/x86-64-v4/libisal.so.2.0.30
/usr/lib64/libisal.so.2
/usr/lib64/libisal.so.2.0.30

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/isa-l/c41999097043083c4213a15101a122f1401e41df

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/igzip.1
