%define module  %pdir-%pnam  
%define	pdir	Text
%define	pnam	Iconv
%define name	perl-%pdir-%pnam
%define version 1.7
%define release %mkrel 10

Summary:	Text::Iconv perl module
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.6.1
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url:		http://search.cpan.org/dist/%{module}

%description
This module provides a Perl interface to the iconv() codeset
conversion function, as defined by the Single UNIX Specification. For
more details see the POD documentation embedded in the file Iconv.pm,
which will also be installed as Text::Iconv(3) man page.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std} INSTALLDIRS=vendor

%{__rm} -f %{buildroot}%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorarch}/Text
%{perl_vendorarch}/Text/Iconv.pm
%dir %{perl_vendorarch}/auto/Text
%dir %{perl_vendorarch}/auto/Text/Iconv
%{perl_vendorarch}/auto/Text/Iconv/autosplit.ix
%{perl_vendorarch}/auto/Text/Iconv/*.so
%{_mandir}/man3/*




%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.7-9mdv2012.0
+ Revision: 765759
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.7-8
+ Revision: 764276
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.7-7
+ Revision: 667396
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.7-6mdv2011.0
+ Revision: 564585
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.7-5mdv2011.0
+ Revision: 556167
- rebuild for perl 5.12

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.7-4mdv2010.1
+ Revision: 426595
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.7-3mdv2009.0
+ Revision: 224243
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 1.7-2mdv2008.1
+ Revision: 151323
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Oct 21 2007 Funda Wang <fwang@mandriva.org> 1.7-1mdv2008.1
+ Revision: 100853
- update to new version 1.7

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.6-1mdv2008.1
+ Revision: 98005
- update to new version 1.6

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2008.0
+ Revision: 77702
- update to new version 1.5


* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:18:56 (54152)
- rebuild

* Mon Aug 07 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/07/06 19:16:31 (54147)
Import perl-Text-Iconv

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 1.4-3mdk
- Fix SPEC according to Perl Policy
	- Source URL
	- URL
- use mkrel

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 1.4-2mdk
- Rebuild for new perl

* Tue Jul 20 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.4-1mdk
- 1.4

* Thu Jul 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.3-1mdk
- 1.3

* Thu Aug 14 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.2-6mdk
- Fix dir owners

