%define real_name Pod-Constants

Summary:	Pod::Constants - Include constants from POD
Name:		perl-%{real_name}
Version:	0.16
Release:	%mkrel 3
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/S/SA/SAMV/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Pod::Constants allows you to extract data from your POD at run-time,
meaning you can do things like declare constants in POD and not have
to update two places at once every time you make a change.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Pod/Constants.pm
%{_mandir}/*/*

