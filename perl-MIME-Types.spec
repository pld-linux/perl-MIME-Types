#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	Types
Summary:	MIME::Types Perl module
Summary(pl):	Modu³ Perla MIME::Types
Name:		perl-MIME-Types
Version:	1.005
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-libnet
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MIME::Types - Definition of MIME types.

%description -l pl
MIME::Types - definicje typów MIME.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/MIME/Types.pm
%{perl_vendorlib}/MIME/Type.pm
%{_mandir}/man3/*
