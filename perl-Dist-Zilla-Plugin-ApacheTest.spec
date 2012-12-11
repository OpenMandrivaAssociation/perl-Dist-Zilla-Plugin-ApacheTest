%define upstream_name    Dist-Zilla-Plugin-ApacheTest
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Build a Makefile.PL that uses ExtUtils::MakeMaker with Apache::Test
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Dumper)
BuildRequires:	perl(Dist::Zilla::File::InMemory)
BuildRequires:	perl(Dist::Zilla::Role::BuildRunner)
BuildRequires:	perl(Dist::Zilla::Role::InstallTool)
BuildRequires:	perl(Dist::Zilla::Role::PrereqSource)
BuildRequires:	perl(Dist::Zilla::Role::TestRunner)
BuildRequires:	perl(Dist::Zilla::Role::TextTemplate)
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
This plugin will produce an the ExtUtils::MakeMaker manpage-powered
_Makefile.PL_ with Apache::Test hooks for the distribution. If loaded, the
Dist::Zilla::Plugin::Manifest plugin should also be loaded, and the
Dist::Zilla::Plugin::MakeMaker plugin should not be loaded.

At this time, this module is essentially a copy of the
Dist::Zilla::Plugin::MakeMaker plugin. Hopefully, over time, the
Dist::Zilla::Plugin::MakeMaker plugin will allow more customization so that
this module will not need to reimplement all of it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

