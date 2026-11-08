Name:		sticky
Version:	1.33
Release:	3
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

Requires:       typelib(GLib)
Requires:       typelib(Gtk)
Requires:	typelib(XApp)
Requires:	typelib(Gspell)
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
install -d %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/sticky %{buildroot}/usr/lib64/sticky
find %{buildroot}/usr/bin %{buildroot}/usr/lib64 %{buildroot}/usr/share %{buildroot}/etc -type f -exec sed -i 's|/usr/lib/sticky|/usr/lib64/sticky|g' {} +
find %{buildroot} -type f -exec sed -i -e "s/__DEB_VERSION__/%{version}/g" {} +
find %{buildroot} -type f -name "sticky.py" -exec sed -i 's/<i>//g; s/<\/i>//g' {} +
%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%{_bindir}/sticky
/usr/lib64/sticky
%{_datadir}/sticky
%{_datadir}/applications/sticky.desktop
%{_datadir}/icons/hicolor/scalable/status/*
%{_sysconfdir}/xdg/autostart/sticky.desktop
%{_datadir}/glib-2.0/schemas/org.x.sticky.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/dbus-1/services/org.x.sticky.service
