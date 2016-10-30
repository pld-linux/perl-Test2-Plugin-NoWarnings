#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test2
%define		pnam	Plugin-NoWarnings
%include	/usr/lib/rpm/macros.perl
Summary:	Test2::Plugin::NoWarnings - Fail if tests warn
Name:		perl-Test2-Plugin-NoWarnings
Version:	0.04
Release:	1
License:	artistic_2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/Test2-Plugin-NoWarnings-%{version}.tar.gz
# Source0-md5:	e26bb1795ee9a0d382063977026cf795
URL:		http://search.cpan.org/dist/Test2-Plugin-NoWarnings/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-IPC-Run3
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test2-Suite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Loading this plugin causes your tests to fail if there any warnings
while they run. Each warning generates a new failing test and the
warning content is outputted via diag.

This module uses $SIG{__WARN__}, so if the code you're testing sets
this, then this module will stop working.

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
%doc Changes INSTALL
%{perl_vendorlib}/Test2/Event/Warning.pm
%{perl_vendorlib}/Test2/Plugin/NoWarnings.pm
%{_mandir}/man3/Test2*.3pm*
