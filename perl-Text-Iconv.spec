%define module  %pdir-%pnam  
%define	pdir	Text
%define	pnam	Iconv
%define name	perl-%pdir-%pnam
%define version 1.5
%define release %mkrel 1

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
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall_std} INSTALLDIRS=vendor

%{__rm} -f $RPM_BUILD_ROOT%{perl_archlib}/perllocal.pod

%clean
%{__rm} -rf $RPM_BUILD_ROOT

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


