%define upstream_name    Pod-Constants
%define upstream_version 0.16

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Pod::Constants - Include constants from POD
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SAMV/%{upstream_name}-%{upstream_version}.tar.bz2
# Fails with current MakeMaker
Patch0:		Pod-Constants-0.16-makemaker.patch

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Pod::Constants allows you to extract data from your POD at run-time,
meaning you can do things like declare constants in POD and not have
to update two places at once every time you make a change.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Pod/Constants.pm
%{_mandir}/*/*


%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.160.0-1mdv2010.0
+ Revision: 404292
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.16-4mdv2009.0
+ Revision: 258229
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.16-3mdv2009.0
+ Revision: 246291
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Nov 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.1
+ Revision: 104565
- update to new version 0.16

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-2mdv2008.0
+ Revision: 86794
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.15-1mdv2007.0
- rebuild

* Fri Jul 15 2005 Oden Eriksson <oeriksson@mandriva.com> 0.15-1mdk
- initial Mandriva package

