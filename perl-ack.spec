#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	ack
Summary:	grep-like text finder
Name:		perl-ack
Version:	1.92
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/P/PE/PETDANCE/ack-%{version}.tar.gz
# Source0-md5:	c25b5a16d0a27386a75c91d531b86cea
URL:		http://betterthangrep.com/
BuildRequires:	perl-File-Next
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-perldoc
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ack is designed as a replacement for 99% of the uses of grep.

Ack searches the named input FILEs (or standard input if no files are
named, or the file name - is given) for lines containing a match to
the given PATTERN. By default, ack prints the matching lines.

Ack can also list files that would be searched, without actually
searching them, to let you take advantage of ack's file-type filtering
capabilities.


%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO ack-help.txt ack-help-types.txt
%attr(755,root,root) %{_bindir}/ack
%{perl_vendorlib}/App/Ack.pm
%{perl_vendorlib}/App/Ack
%{_mandir}/man1/*
