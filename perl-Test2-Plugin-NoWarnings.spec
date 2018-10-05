#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test2
%define		pnam	Plugin-NoWarnings
%include	/usr/lib/rpm/macros.perl
Summary:	Test2::Plugin::NoWarnings - Fail if tests warn
Summary(pl.UTF-8):	Test2::Plugin::NoWarnings -niepowodzenie w przypadku ostrzeżeń z testów
Name:		perl-Test2-Plugin-NoWarnings
Version:	0.06
Release:	1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-%{version}.tar.gz
# Source0-md5:	c329dcd57b3d5990e134508fc02d76d2
URL:		https://metacpan.org/release/Test2-Plugin-NoWarnings
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-Test-Simple >= 1.302015
BuildRequires:	perl-Test2-Suite
%endif
Requires:	perl-Test-Simple >= 1.302015
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Loading this plugin causes your tests to fail if there any warnings
while they run. Each warning generates a new failing test and the
warning content is outputted via diag.

%description -l pl.UTF-8
Wczytanie tej wtyczki powoduje, że testy kończą się niepowodzeniem,
jeśli w trakcie ich działania pojawią się jakieś ostrzeżenia. Każde
ostrzeżenie tworzy nowy test zakończony niepowodzeniem, a treść
ostrzeżenia jest wypisywana poprzez diag.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Test2/Event/Warning.pm
%{perl_vendorlib}/Test2/Plugin/NoWarnings.pm
%{_mandir}/man3/Test2::Event::Warning.3pm*
%{_mandir}/man3/Test2::Plugin::NoWarnings.3pm*
