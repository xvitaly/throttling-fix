Name: throttling-fix
Version: 1.0.0
Release: 1%{?dist}

Summary: Fixes throttling issues on some laptops
License: MIT
URL: https://github.com/xvitaly/%{name}

Source0: %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: systemd-rpm-macros

%description
Fixes throttling issues by explicitly setting correct power scheme.
Use with extremely caution! Incorrect usage can destroy your system.

%package t480
Summary: Fixes throttling issues on T480/T580
%{?systemd_requires}

%description t480
Fixes throttling issues on T480 and T580 series laptops by explicitly
setting correct power scheme.

Use with extremely caution! Incorrect usage can destroy your system.

%prep
%autosetup

cp -f src/systemd/%{name}.service src/systemd/%{name}-t480.service
sed -e "s/some/T480 and T580/" -e "s/%{name}/%{name}-t480/" -i src/systemd/%{name}-t480.service

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 src/scripts/%{name}-t480.sh %{buildroot}%{_bindir}/%{name}-t480

mkdir -p %{buildroot}%{_unitdir}
install -p -m 0644 src/systemd/%{name}-t480.service %{buildroot}%{_unitdir}

%post t480
%systemd_post %{name}-t480.service

%preun t480
%systemd_preun %{name}-t480.service

%postun t480
%systemd_postun_with_restart %{name}-t480.service

%files t480
%doc README.md
%license LICENSE
%{_bindir}/%{name}-t480
%{_unitdir}/%{name}-t480.service

%changelog
* Tue Jul 23 2019 Vitaly Zaitsev <vitaly@easycoding.org> - 1.0.0-1
- Initial release of version 1.0.0.
