%define prj Horde_NLS

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-nls
Version:       0.0.2
Release:       12
Summary:       Localization package
License:       LGPL
Group:         Networking/Mail
Url:           https://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(post):php-pear
Requires(preun):php-pear
Requires: 	php-pear
Requires:      php-pear-channel-horde
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde



%description
This package provides horde localization

%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear install --packagingroot %{buildroot} --nodeps package.xml

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/NLS
%{peardir}/Horde/NLS.php
%{peardir}/Horde/NLS/GeoIP.php
%{peardir}/Horde/NLS/carsigns.php
%{peardir}/Horde/NLS/coordinates.php
%{peardir}/Horde/NLS/countries.php
%{peardir}/Horde/NLS/tld.php


%changelog
* Sat Jul 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-11mdv2011.0
+ Revision: 564077
- Increased release for rebuild

* Wed Mar 17 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-10mdv2010.1
+ Revision: 522925
- remove Requires(pre): %%{_bindir}/pear
  increased release version to 10

* Tue Mar 16 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-9mdv2010.1
+ Revision: 520662
- increased version
- added Requires(post):php-pear
  added Requires(preun):php-pear
  added Requires:	php-pear
- added PreReq: php-pear and bumped release

* Mon Mar 01 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-7mdv2010.1
+ Revision: 512869
- added     Requires: php-pear
  removed BuildRequires: horde-framework
- remove Requires: horde-util
- added BuildRequires: horde-framework

* Thu Feb 25 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-6mdv2010.1
+ Revision: 510864
- removed BuildRequires: horde-framework
- added Requires: php-pear-channel-horde
- reversed last change
- removed Requires(pre): %%{_bindir}/pear
- added BuildRequires: horde-framework as it may now work

* Mon Feb 22 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-5mdv2010.1
+ Revision: 509353
- forgot to update rel version to 5
- removed Buildrequires horde-framework
- reversed requires after package built

* Sun Feb 21 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.0.2-2mdv2010.1
+ Revision: 509214
- removed more requires to get it built
- AutoReqProv: 0 to get it to build
- replace PreReq with Requires(pre)
- Initial import


