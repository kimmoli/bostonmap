Name:       bostonmap

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    AltGr fixed boston keymap for jolla
Version:    0.0.1
Release:    1
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/kimmoli/
Source0:    %{name}-%{version}.tar.bz2
BuildArch:  noarch
BuildRequires: qt5-qttools-kmap2qmap

%description
Replacement boston map for Jolla to support AltGr

%prep
%setup -q -n %{name}-%{version}

%build

%qtc_qmake5 SPECVERSION=%{version}

%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%qmake5_install


%files
%defattr(644,root,root,755)
/usr/share/qt5/keymaps/
