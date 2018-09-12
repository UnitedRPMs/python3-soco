Name:           python3-soco
Version:        0.16
Release:        1%{?dist}
Summary:        SoCo (Sonos Controller) is a simple library to control Sonos speakers
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/SoCo/SoCo
Source:         https://github.com/SoCo/SoCo/archive/v%{version}.tar.gz
BuildRequires:  python3-devel
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-xmltodict
BuildRequires:  python3-rpm-macros
#-------------------------------
Requires:       python3-requests
Requires:       python3-xmltodict
BuildArch:      noarch


%description
SoCo (Sonos Controller) is a simple Python class that allows you to
programmatically control Sonos speakers.

%prep
%autosetup -n SoCo-%{version} 

%build
%py3_build

%install
%py3_install

%files 
%doc AUTHORS.rst README.rst LICENSE.rst
%{python3_sitelib}/soco
%{python3_sitelib}/soco-%{version}-py*.egg-info

%changelog

* Wed Sep 12 2018 David Va <davidva AT tuta DOT io> 0.16-1 
- Updated to 0.16

* Thu Aug 02 2018 David Va <davidva AT tuta DOT io> 0.15-1 
- Initial build
