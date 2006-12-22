#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Types
Summary:	MIME::Types Perl module - definition of MIME types
Summary(pl):	Modu³ Perla MIME::Types - definicje typów MIME
Name:		perl-MIME-Types
Version:	1.18
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fec1a57dfc4a0d7177b98fd75844685b
URL:		http://search.cpan.org/dist/MIME-Types/
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.47}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME types are used in MIME compliant lines, for instance as part of
e-mail and HTTP traffic, to indicate the type of content which is
transmitted. Sometimes real knowledge about a mime-type is need.

This module maintains a set of MIME::Type objects, which each describe
one known MIME type. There are many types defined by RFCs and vendors,
so the list is long but not complete.
 
%description -l pl
Typy MIME s± u¿ywane w liniach nag³ówka zgodnych z MIME, na przyk³ad
jako czê¶æ transmisji e-mail lub HTTP, do okre¶lenia rodzaju
przesy³anej tre¶ci. Czasem potrzebna jest znajomo¶æ prawdziwego
mime-type.

Ten modu³ utrzymuje zbiór obiektów MIME::Type, z których ka¿dy opisuje
jeden znany typ MIME. Zawiera wiele typów zdefiniowanych przez RFC i
producentów, wiêc lista jest d³uga, ale niepe³na.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/MIME/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MIME/Types.pm
%{perl_vendorlib}/MIME/Type.pm
%{_mandir}/man3/*
