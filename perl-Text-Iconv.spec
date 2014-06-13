%define	modname	Text-Iconv

Summary:	Text::Iconv perl module
Name:		perl-%{modname}
Version:	1.7
Release:	15
License:	GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Text/%{modname}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.6.1

%description
This module provides a Perl interface to the iconv() codeset
conversion function, as defined by the Single UNIX Specification. For
more details see the POD documentation embedded in the file Iconv.pm,
which will also be installed as Text::Iconv(3) man page.

%prep
%setup -qn %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std INSTALLDIRS=vendor

rm -f %{buildroot}%{perl_archlib}/perllocal.pod

%files
%doc Changes README
%dir %{perl_vendorarch}/Text
%{perl_vendorarch}/Text/Iconv.pm
%dir %{perl_vendorarch}/auto/Text
%dir %{perl_vendorarch}/auto/Text/Iconv
%{perl_vendorarch}/auto/Text/Iconv/autosplit.ix
%{perl_vendorarch}/auto/Text/Iconv/*.so
%{_mandir}/man3/*

