%define major 4
%define libname	%mklibname mcrypt %{major}
%define develname %mklibname mcrypt -d
%define static_develname %mklibname mcrypt -d -s

Summary:	Thread-safe data encryption library
Name:		libmcrypt
Version:	2.5.8
Release:	%mkrel 10
License:	LGPLv2+
Group:		System/Libraries
URL:		http://mcrypt.sourceforge.net/
Source0:	http://downloads.sourceforge.net/mcrypt/%{name}-%{version}.tar.gz
BuildRequires:	libtool-devel
BuildRequires:	automake1.7
BuildRequires:	autoconf2.5
BuildRequires:	multiarch-utils >= 1.0.3
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Libmcrypt is a thread-safe library providing a uniform interface
to access several block and stream encryption algorithms.

     Some algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more. 

%package -n	%{libname}
Summary:	Thread-safe data encryption library
Group:		System/Libraries
Requires:	%{name} >= %{version}

%description -n	%{libname}
Libmcrypt is a thread-safe library providing a uniform interface
to access several block and stream encryption algorithms.

     Some algorithms which are supported:
SERPENT, RIJNDAEL, 3DES, GOST, SAFER+, CAST-256, RC2, XTEA, 3WAY,
TWOFISH, BLOWFISH, ARCFOUR, WAKE and more. 


%package -n	%{develname}
Summary:	Header files and libraries for developing apps with libmcrypt
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Obsoletes:	%{libname}-devel

%description -n	%{develname}
This package contains the header files and libraries needed to
develop programs that use the libmcrypt library.
Install it if you want to develop such applications.

%package -n	%{static_develname}
Summary:	Static libraries for developing apps with libmcrypt
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{name}-devel = %{version}
Provides:	%{name}-static-devel = %{version}
Obsoletes:	%{libname}-static-devel

%description -n	%{static_develname}
This package contains the static libraries needed to
develop programs that use the libmcrypt library.
Install it if you want to develop such applications.

%prep

%setup -q

%build
rm -rf libltdl
libtoolize --copy --force --ltdl
cp `aclocal-1.7 --print-ac-dir`/libtool.m4 .
aclocal-1.7
autoconf
automake-1.7 --foreign

%configure2_5x \
    --enable-dynamic-loading \
    --enable-static \
    --enable-shared \
    --disable-ltdl-install
    
%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall

%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/libmcrypt-config
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%doc AUTHORS COPYING.LIB ChangeLog INSTALL KNOWN-BUGS NEWS README THANKS TODO doc/README.* doc/*.c
%multiarch %{multiarch_bindir}/libmcrypt-config
%{_bindir}/libmcrypt-config
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/mcrypt.h
%dir %{_includedir}/mutils
%{_includedir}/mutils/mcrypt.h
%{_datadir}/aclocal/*.m4
%{_mandir}/man3/*

%files -n %{static_develname}
%defattr(-, root, root)
%{_libdir}/*.a
%{_libdir}/%{name}/*.a

%files
%defattr(-,root,root)
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.so


