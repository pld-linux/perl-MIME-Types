#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MIME
%define	pnam	Types
Summary:	MIME::Types Perl module
Summary(pl):	Modu³ Perla MIME::Types
Name:		perl-MIME-Types
Version:	1.13
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	04c6554f73307628aa87e7ddba8861d8
BuildRequires:	perl-devel >= 1:5.8.0
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{perl_vendorlib}/%{pdir}/Type.pm
%{_mandir}/man3/*
