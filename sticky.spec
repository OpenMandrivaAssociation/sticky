Name:		sticky
Version:	1.33
Release:	1
Summary:	Sticky Notes app
License:        GPL-3+
URL:            https://github.com/linuxmint/sticky
Source0:	https://github.com/linuxmint/sticky/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildSystem:    meson

BuildRequires:	gettext
BuildRequires:  meson
BuildRequires:  python

Requires:       lib64glib-gir2.0
Requires:       lib64gtk-gir3.0
Requires:	lib64xapp-gir3.2
Requires:	lib64gspell-gir1
Requires:       python
Requires:       python-gi
Requires:       python-xapp

%description
Sticky Notes app

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -exec sed -i -e "s/__DEB_VERSION__/%{version}/g" {} +
find %{buildroot} -type f -name "sticky.py" -exec sed -i 's/<i>//g; s/<\/i>//g' {} +
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%{_bindir}/sticky
/usr/lib/sticky
%{_datadir}/sticky
%{_datadir}/applications/sticky.desktop
%{_datadir}/icons/hicolor/scalable/status/*
%{_sysconfdir}/xdg/autostart/sticky.desktop
%{_datadir}/glib-2.0/schemas/org.x.sticky.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/dbus-1/services/org.x.sticky.service
