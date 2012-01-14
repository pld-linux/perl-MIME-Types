#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	MIME
%define		pnam	Types
Summary:	MIME::Types Perl module - definition of MIME types
Summary(pl.UTF-8):	Moduł Perla MIME::Types - definicje typów MIME
Name:		perl-MIME-Types
Version:	1.34
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MIME/MARKOV/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	87c496480e463c0b7792e7f5429e50d1
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
 
%description -l pl.UTF-8
Typy MIME są używane w liniach nagłówka zgodnych z MIME, na przykład
jako część transmisji e-mail lub HTTP, do określenia rodzaju
przesyłanej treści. Czasem potrzebna jest znajomość prawdziwego
mime-type.

Ten moduł utrzymuje zbiór obiektów MIME::Type, z których każdy opisuje
jeden znany typ MIME. Zawiera wiele typów zdefiniowanych przez RFC i
producentów, więc lista jest długa, ale niepełna.

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

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/MIME/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/MIME/Type.pm
%{perl_vendorlib}/MIME/Types.pm
%{_mandir}/man3/MIME::Type.3pm*
%{_mandir}/man3/MIME::Types.3pm*
