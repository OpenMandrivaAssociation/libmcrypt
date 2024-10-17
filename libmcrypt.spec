%define major 4
%define libname %mklibname mcrypt %{major}
%define devname %mklibname mcrypt -d

Summary:	Thread-safe data encryption library
Name:		libmcrypt
Version:	2.5.8
Release:	30
License:	LGPLv2+
Group:		System/Libraries
Url:		https://mcrypt.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mcrypt/%{name}-%{version}.tar.gz
BuildRequires:	libtool
BuildRequires:	libtool-devel
BuildRequires:	automake

%description
Libmcrypt is a thread-safe library providing a uniform interface
to access several block and stream encryption algorithms.

     Some algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more. 

%package -n %{libname}
Summary:	Thread-safe data encryption library
Group:		System/Libraries
Requires:	%{name} >= %{EVRD}

%description -n %{libname}
Libmcrypt is a thread-safe library providing a uniform interface
to access several block and stream encryption algorithms.

     Some algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more. 

%package -n %{devname}
Summary:	Header files and libraries for developing apps with libmcrypt
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the header files and libraries needed to
develop programs that use the libmcrypt library.
Install it if you want to develop such applications.

%prep
%autosetup -p1
rm -rf libltdl
libtoolize --copy --force --install --ltdl
cp $(aclocal --print-ac-dir)/libtool.m4 .
aclocal
autoconf
automake --foreign -acf

%build
%configure \
	--enable-dynamic-loading \
	--disable-static \
	--enable-shared \
	--disable-ltdl-install

%make_build

%install
%make_install

%files
%{_libdir}/%{name}/*.so

%files -n %{libname}
%{_libdir}/libmcrypt.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING.LIB ChangeLog INSTALL KNOWN-BUGS NEWS README THANKS TODO doc/README.* doc/*.c
%{_bindir}/libmcrypt-config
%{_libdir}/lib*.so
%{_includedir}/mcrypt.h
%dir %{_includedir}/mutils
%{_includedir}/mutils/mcrypt.h
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*

