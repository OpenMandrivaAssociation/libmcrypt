%define major 4
%define libname	%mklibname mcrypt %{major}
%define develname %mklibname mcrypt -d

Summary:	Thread-safe data encryption library
Name:		libmcrypt
Version:	2.5.8
Release:	14
License:	LGPLv2+
Group:		System/Libraries
URL:		http://mcrypt.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mcrypt/%{name}-%{version}.tar.gz
BuildRequires:	autoconf automake libtool libtool-devel

%description
Libmcrypt is a thread-safe library providing a uniform interface
to access several block and stream encryption algorithms.

     Some algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more. 

%package -n	%{libname}
Summary:	Thread-safe data encryption library
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n	%{libname}
Libmcrypt is a thread-safe library providing a uniform interface
to access several block and stream encryption algorithms.

     Some algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more. 


%package -n	%{develname}
Summary:	Header files and libraries for developing apps with libmcrypt
Group:		Development/C
Requires:	%{libname} >= %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
This package contains the header files and libraries needed to
develop programs that use the libmcrypt library.
Install it if you want to develop such applications.

%prep

%setup -q

%build
rm -rf libltdl autom4te.cache
libtoolize --copy --force --ltdl
cp `aclocal --print-ac-dir`/libtool.m4 .
aclocal
autoconf
automake --foreign

%configure2_5x \
    --enable-dynamic-loading \
    --disable-static \
    --enable-shared \
    --disable-ltdl-install

%make

%check
make check

%install
rm -rf %{buildroot}

%makeinstall

%multiarch_binaries %{buildroot}%{_bindir}/libmcrypt-config

# cleanup
rm -rf %{buildroot}%{_libdir}/*.*a
rm -rf %{buildroot}%{_libdir}/%{name}/*.*a

%files
%{_libdir}/%{name}/*.so

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING.LIB ChangeLog INSTALL KNOWN-BUGS NEWS README THANKS TODO doc/README.* doc/*.c
%{multiarch_bindir}/libmcrypt-config
%{_bindir}/libmcrypt-config
%{_libdir}/*.so
%{_includedir}/mcrypt.h
%dir %{_includedir}/mutils
%{_includedir}/mutils/mcrypt.h
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*
