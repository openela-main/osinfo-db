# -*- rpm-spec -*-

Summary: osinfo database files
Name: osinfo-db
Version: 20230518
Release: 1%{?dist}
License: LGPLv2+
Source0: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz
Source1: https://fedorahosted.org/releases/l/i/libosinfo/%{name}-%{version}.tar.xz.asc
URL: http://libosinfo.org/
BuildRequires: intltool
BuildRequires: git-core
BuildRequires: osinfo-db-tools
BuildArch: noarch
Requires: hwdata

%description
The osinfo database provides information about operating systems and
hypervisor platforms to facilitate the automated configuration and
provisioning of new virtual machines

%prep
%autosetup -S git_am

%install
osinfo-db-import  --root %{buildroot} --dir %{_datadir}/osinfo %{SOURCE0}
%if 0%{?rhel}
# Remove the upstream virtio-win / spice-guest-tools drivers
find %{buildroot}/%{_datadir}/osinfo/os/microsoft.com/ -name "win-*.d" -type d -exec rm -rf {} +
%endif

%files
%dir %{_datadir}/osinfo/
%{_datadir}/osinfo/VERSION
%{_datadir}/osinfo/LICENSE
%{_datadir}/osinfo/datamap
%{_datadir}/osinfo/device
%{_datadir}/osinfo/os
%{_datadir}/osinfo/platform
%{_datadir}/osinfo/install-script
%{_datadir}/osinfo/schema

%changelog
* Tue May 23 2023 Victor Toso <victortoso@redhat.com> - 20230518-1
- Update to new release (v20230518)
  Resolves: rhbz#2184782
  Resolves: rhbz#2184613

* Tue Aug 02 2022 Victor Toso <victortoso@redhat.com> - 20220727-2
- Add prereleases: rhel-8.7 and rhel-9.1
  Resolves: rhbz#2103908

* Thu Jul 28 2022 Victor Toso <victortoso@redhat.com> - 20220727-1
- Update to new release (v20220727)
  Resolves: rhbz#2083663

* Tue May 17 2022 Victor Toso <victortoso@redhat.com> - 20220516-1
- Update to new release (v20220516)
  Resolves: rhbz#2083663

* Thu Dec 16 2021 Victor Toso <victortoso@redhat.com> - 20211216-1
- Update to new release (v20211216)
  Resolves: rhbz#1976818

* Mon Aug 09 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210809-1
- Update to new release (v20210806)

* Mon Feb 15 2021 Fabiano Fidêncio <fidencio@redhat.com> - 20210215-1
- Resolves: rhbz#1903300 - rebase osinfo-db to latest fedora

* Thu Feb 04 2021 Danilo C. L. de Paula <ddepaula@redhat.com> - 20201218-3
- Resolves: rhbz#1903300 - rebase osinfo-db to latest fedora

* Thu Aug 13 2020 Fabiano Fidêncio <fidencio@redhat.com> - 20200813-1
- Update to v20200813 release
- Related: rhbz#1837756 - osinfo-db is out of date
- Resolves: rhbz#1868030 - 'osinfo-query os' is missing latest version of Ubuntu and Oracle Linux

* Tue Aug 04 2020 Fabiano Fidêncio <fidencio@redhat.com> - 20200804-2
- Remove duplicated virtio1.0-fs device
- Related: rhbz#1837756 - osinfo-db is out of date

* Tue Aug 04 2020 Fabiano Fidêncio <fidencio@redhat.com> - 20200804-1
- Update to v20200804 release
- Related: rhbz#1837756 - osinfo-db is out of date

* Sun May 31 2020 Fabiano Fidêncio <fidencio@redhat.com> - 20200529-1
- Update to v20200529 release
- Resolves: rhbz#1837756 - osinfo-db is out of date
- Resolves: rhbz#1707119 - Provide information about UEFI support for guests (osinfo-db)

* Mon Feb 03 2020 Fabiano Fidêncio <fidencio@redhat.com> - 20200203-1
- Update to v20200203 release
- Resolves: rhbz#1780529 - Update to the latest upstream release

* Tue Dec 10 2019 Fabiano Fidêncio <fidencio@redhat.com> - 20191125-1
- Updated to v20191125 release
- Resolves: rhbz#1780529 - Update to the latest upstream release
- Add rhel8.2 & rhel7.8 entries
- Remove upstream virtio-win / spice-guest-tools drivers

* Wed Jun 12 2019 Fabiano Fidêncio <fidencio@redhat.com> - 20190611-1
- Update to v20190611 release
- Resolves: rhbz#1699990 - Rebase to the latest upstream release

* Thu May 23 2019 Fabiano Fidêncio <fidencio@redhat.com> - 20190504-2
- Add rhel-8.1 & rhel-7.7 entry
- Resolves: rhbz#1713245 - Add rhel-8.1 and rhel-7.7 entries

* Fri May 10 2019 Fabiano Fidêncio <fidencio@redhat.com> - 20190504-1
- Update to v20190504 release
- Resolves: rhbz#1699990 - Rebase to the latest upstream release
- Resolves: rhbz#1689817 - virt-manager cannot detect operating system name
                           for rhel8.0.0 tree automatically
- Resolves: rhbz#1703480 - rhel8.0.x is not detected as rhel8.0
- Resolves: rhbz#1685364 - Add win2019 to libosinfo

* Fri Dec 07 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-8
- Resolves: rhbz#1656917 - backport change to support Fedora 29 Silverblue

* Fri Nov 16 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-7
- Resolves: rhbz#1650197 - Fix the volume-ids of rhel8.0 entry
- Resolves: rhbz#1650459 - test-mediauris is failing because of ubuntu change
- Related: rhbz#1580232 - Add support to RHEL7.6 and RHEL8.0

* Wed Nov 14 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-6
- Related: rhbz#1580232 - Add support to RHEL7.6 and RHEL8.0

* Sat Nov 03 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-5
- Related:  rhbz#1580232 - Add support to RHEL7.6 and RHEL8.0

* Thu Nov 01 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-4
- Related: rhbz#1644738 - Fix a typo in the Fedora 29 XML

* Thu Nov 01 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-3
- Resolves: rhbz#1644738 - Latest released Fedora 29 support in RHEL8 instead
                           of Fedora 29 Beta

* Mon Oct 22 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-2
- Resolves: rhbz#1640458 - Debian Testing should derive-from/upgrade Debian 9

* Thu Oct 11 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20181011-1
- Related: rhbz#1627271 - Update to 20181011 release

* Fri Sep 21 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20180920-1
- Related: rhbz#1627271 - Update to 20180920 release

* Mon Sep 10 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20180903-1
- Related: rhbz#1627271 - Update to 20180903 release

* Mon Sep 10 2018 Fabiano Fidêncio <fidencio@redhat.com> - 20180612-2
- Resolves: rhbz#1580232 - Add support to RHEL-7.6 and RHEL-8.0

* Wed Jun 20 2018 Daniel P. Berrangé <berrange@redhat.com> - 20180612-1
- Update to 20180612 release

* Mon Apr 16 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 20180416-1
- Update to new release

* Sun Mar 25 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 20180325-1
- Update to new release

* Sun Mar 18 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 20180318-1
- Update to new release

* Sun Mar 11 2018 Fabiano Fidêncio <fabiano@fidencio.org> - 20180311-1
- Update to new release

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 20170813-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 13 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170813-1
- Update to new release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170423-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 23 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170423-1
- Update to new release

* Sun Mar 26 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170326-1
- Update to new release

* Sat Feb 25 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170225-1
- Update to new release

* Sat Feb 11 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170211-1
- Update to new release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20170121-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 21 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170121-2
- 20170121-1 used an incorrect tarball

* Sat Jan 21 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170121-1
- Update to new release

* Sat Jan 14 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170114-1
- Update to new release

* Sat Jan 07 2017 Fabiano Fidêncio <fabiano@fidencio.org> - 20170107-1
- Update to new release

* Wed Oct 26 2016 Daniel P. Berrange <berrange@redhat.com> - 20161026-1
- Update to new release

* Fri Jul 29 2016 Daniel P. Berrange <berrange@redhat.com> - 20160728-1
- Initial package after split from libosinfo (rhbz #1361596)
