#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
#
Name     : perl-IO-CaptureOutput
Version  : 1.1105
Release  : 30
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/IO-CaptureOutput-1.1105.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/IO-CaptureOutput-1.1105.tar.gz
Summary  : '(DEPRECATED) capture STDOUT and STDERR from Perl code, subprocesses or XS'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-IO-CaptureOutput-license = %{version}-%{release}
Requires: perl-IO-CaptureOutput-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : util-linux
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
IO::CaptureOutput - (DEPRECATED) capture STDOUT and STDERR from Perl
code, subprocesses or XS

%package dev
Summary: dev components for the perl-IO-CaptureOutput package.
Group: Development
Provides: perl-IO-CaptureOutput-devel = %{version}-%{release}
Requires: perl-IO-CaptureOutput = %{version}-%{release}

%description dev
dev components for the perl-IO-CaptureOutput package.


%package license
Summary: license components for the perl-IO-CaptureOutput package.
Group: Default

%description license
license components for the perl-IO-CaptureOutput package.


%package perl
Summary: perl components for the perl-IO-CaptureOutput package.
Group: Default
Requires: perl-IO-CaptureOutput = %{version}-%{release}

%description perl
perl components for the perl-IO-CaptureOutput package.


%prep
%setup -q -n IO-CaptureOutput-1.1105
cd %{_builddir}/IO-CaptureOutput-1.1105

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-IO-CaptureOutput
cp %{_builddir}/IO-CaptureOutput-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-IO-CaptureOutput/e283f5a12224408f54e908e5fb57b938cae1a94d || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/IO::CaptureOutput.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-IO-CaptureOutput/e283f5a12224408f54e908e5fb57b938cae1a94d

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
