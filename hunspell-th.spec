Name: hunspell-th
Summary: Thai hunspell dictionaries
%define upstreamid 20061212
Version: 0.%{upstreamid}
Release: 10%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/th_TH.zip
Group: Applications/Text
URL: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: LGPLv2+
BuildArch: noarch

Requires: hunspell

%description
Thai hunspell dictionaries.

%prep
%setup -q -c -n hunspell-th

%build
#set encoding to IANA prefered name
sed -i -e 's/TIS620-2533/TIS620/g' th_TH.aff
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_TH.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20061212-10
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 04 2010 Caolán McNamara <caolanm@redhat.com> - 0.20061212-5
- set encoding to IANA prefered name

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20061212-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Aug 09 2007 Caolán McNamara <caolanm@redhat.com> - 0.20061212-2
- clarify license version

* Wed Feb 14 2007 Caolán McNamara <caolanm@redhat.com> - 0.20061212-1
- update to latest

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20050530-1
- initial version
