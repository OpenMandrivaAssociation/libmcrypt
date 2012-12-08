%define major 4
%define libname	%mklibname mcrypt %{major}
%define develname %mklibname mcrypt -d

Summary:	Thread-safe data encryption library
Name:		libmcrypt
Version:	2.5.8
Release:	16
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


%changelog
* Sat Dec 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-14
+ Revision: 737482
- drop the static lib, its sub package and the libtool *.la file
- various fixes

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-13
+ Revision: 661960
- rebuild

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-12
+ Revision: 661449
- multiarch fixes

* Sun Jan 02 2011 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-11mdv2011.0
+ Revision: 627633
- don't force the usage of automake1.7

* Thu Nov 25 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-10mdv2011.0
+ Revision: 601050
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-9mdv2010.1
+ Revision: 519023
- rebuild

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.5.8-8mdv2010.0
+ Revision: 425619
- rebuild

* Thu Jan 29 2009 Funda Wang <fwang@mandriva.org> 2.5.8-7mdv2009.1
+ Revision: 335081
- rebuild for new libtool

* Thu Dec 18 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-6mdv2009.1
+ Revision: 315576
- rebuild

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 2.5.8-5mdv2009.0
+ Revision: 275907
- apply devel policy
- drop old conditionnal
- check major

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.5.8-4mdv2009.0
+ Revision: 222927
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-3mdv2008.1
+ Revision: 178930
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Feb 20 2007 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-1mdv2007.0
+ Revision: 122971
- rebuild

* Mon Feb 19 2007 Oden Eriksson <oeriksson@mandriva.com> 2.5.8-0.0.0mdv2007.1
+ Revision: 122873
- 2.5.8
- drop upstream patches

* Tue Oct 31 2006 Oden Eriksson <oeriksson@mandriva.com> 2.5.7-10mdv2007.1
+ Revision: 74192
- Import libmcrypt

* Sat Aug 19 2006 Frederic Crozat <fcrozat@mandriva.com> 2.5.7-10mdv2007.0
- Patch0: fix aclocal warning
- use mkrel

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.5.7-9mdk
- Rebuild

* Fri May 13 2005 Oden Eriksson <oeriksson@mandriva.com> 2.5.7-8mdk
- make it compile correctly on x86_64

* Mon Jan 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 2.5.7-7mdk
- fix deps and conditional %%multiarch
- run the tests
- fix requires-on-release

* Tue Dec 07 2004 Lenny Cartier <lenny@mandrakesoft.com> 2.5.7-6mdk
- rebuild

