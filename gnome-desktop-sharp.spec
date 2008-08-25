%define name gnome-desktop-sharp
%define version 2.23.90
%define release %mkrel 2
%define gtk_sharp 2.12.2
%define gnome_sharp 2.20.0
%define monodir %_prefix/lib/mono

Summary: C# language bindings for GNOME desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch: gnome-desktop-sharp-2.20.1-major.patch
Patch1: gnome-desktop-sharp-2.23.90-dllmap.patch
License: LGPLv2
Group: System/Libraries
Url: http://www.mono-project.com/Main_Page
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel >= %{gtk_sharp}
BuildRequires:	gtk-sharp2 >= %{gtk_sharp}
BuildRequires:	glade-sharp2 >= %{gtk_sharp}
BuildRequires:	librsvg-devel >= 2.18.2
BuildRequires:	gtkhtml-3.14-devel >= 3.16.0
BuildRequires:	vte-devel >= 0.16.9
BuildRequires:	libnautilus-cd-burner-devel >= 2.20.0
BuildRequires:	gnome-panel-devel
BuildRequires:	libgnomeprintui-devel
BuildRequires:	gnome-desktop-devel
BuildRequires:	libwnck-devel >= 2.20.0
BuildRequires:	gtksourceview-devel >= 2.0.0
BuildRequires:	gnome-sharp2-devel >= %{gnome_sharp}
Conflicts: gnome-sharp2 < 2.19.90

%description
This contains C# language bindings for some of the GNOME desktop libraries.

%package devel
Summary: C# language binding for the GNOME desktop - devel files
Group: Development/Other
Requires: %name = %version
Requires: gtkhtml-sharp = %version
Requires: vte-sharp = %version
Requires: nautilusburn-sharp = %version
Requires: rsvg-sharp = %version
Requires: wnck-sharp = %version
Requires: gtksourceview-sharp2 = %version
Requires: gnome-panel-sharp = %version
Requires: gnome-print-sharp = %version

%description devel
This is a C# language binding for the GNOME desktop. It contains all
files that are needed to build against %{name}.

%package -n gnome-print-sharp
Group: System/Libraries
Summary: C# language binding for the GNOME print library

%description -n gnome-print-sharp
This contains the C# language binding for the GNOME print library.

%package -n gnome-panel-sharp
Group: System/Libraries
Summary: C# language binding for the GNOME panel

%description -n gnome-panel-sharp
This contains the C# language binding for the GNOME panel.

%package -n vte-sharp
Group: System/Libraries
Summary: C# language binding for VTE

%description -n vte-sharp
This contains the C# language binding for the VTE library.

%package -n rsvg-sharp
Group: System/Libraries
Summary: C# language binding for librsvg

%description -n rsvg-sharp
This contains the C# language binding for the librsvg library.

%package -n wnck-sharp
Group: System/Libraries
Summary: C# language binding for libwnck

%description -n wnck-sharp
This contains the C# language binding for the libwnck library.

%package -n nautilusburn-sharp
Group: System/Libraries
Summary: C# language binding for the Nautilus CD burner

%description -n nautilusburn-sharp
This contains the C# language binding for the Nautilus CD burner library.

%package -n gtkhtml-sharp
Group: System/Libraries
Summary: C# language binding for gtkhtml

%description -n gtkhtml-sharp
This contains the C# language binding for the gtkhtml library.

%package -n gtksourceview-sharp2
Group: System/Libraries
Summary: C# language binding for gtksourceview 2

%description -n gtksourceview-sharp2
This contains the C# language binding for the gtksourceview 2 library.


%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%configure2_5x
make

%install
rm -rf %{buildroot}
%makeinstall
rm -rf %buildroot%_libdir/lib*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS  HACKING AUTHORS
%monodir/gac/gnomedesktop-sharp
%monodir/gnomedesktop-sharp-2.20

%files -n gnome-print-sharp
%defattr(-,root,root)
%monodir/gac/gnome-print-sharp
%monodir/gnome-print-sharp-2.18

%files -n gnome-panel-sharp
%defattr(-,root,root)
%monodir/gac/gnome-panel-sharp
%_libdir/libgnomepanelsharpglue-2.so
%monodir/gnome-panel-sharp-2.24

%files -n vte-sharp
%defattr(-,root,root)
%monodir/gac/vte-sharp
%_libdir/libvtesharpglue-2.so
%monodir/vte-sharp-0.16

%files -n rsvg-sharp
%defattr(-,root,root)
%monodir/gac/rsvg2-sharp
%monodir/rsvg2-sharp-2.0

%files -n wnck-sharp
%defattr(-,root,root)
%monodir/gac/wnck-sharp
%monodir/wnck-sharp-2.20
%_libdir/libwncksharpglue-2.so

%files -n gtksourceview-sharp2
%defattr(-,root,root)
%monodir/gac/gtksourceview2-sharp
%monodir/gtksourceview2-sharp-2.0
%_libdir/libgtksourceview2sharpglue-2.so

%files -n nautilusburn-sharp
%defattr(-,root,root)
%monodir/gac/nautilusburn-sharp
%monodir/nautilusburn-sharp-2.20
%_libdir/libnautilusburnsharpglue-2.so

%files -n gtkhtml-sharp
%defattr(-,root,root)
%monodir/gac/gtkhtml-sharp
%monodir/gtkhtml-sharp-3.14
%_libdir/libgtkhtmlsharpglue-2.so

%files devel
%defattr(-,root,root)
%doc ChangeLog
%_libdir/pkgconfig/gnome-desktop-sharp-2.0.pc
%_libdir/pkgconfig/gtkhtml-sharp-3.14.pc
%_libdir/pkgconfig/gtksourceview2-sharp.pc
%_libdir/pkgconfig/nautilusburn-sharp.pc
%_libdir/pkgconfig/rsvg2-sharp-2.0.pc
%_libdir/pkgconfig/vte-sharp-0.16.pc
%_libdir/pkgconfig/wnck-sharp-1.0.pc
%_libdir/pkgconfig/gnome-panel-sharp-2.24.pc
%_libdir/pkgconfig/gnome-print-sharp-2.18.pc
%_datadir/gnomedesktop-sharp
%_datadir/gtkhtml-sharp
%_datadir/gtksourceview2-sharp
%_datadir/nautilusburn-sharp
%_datadir/rsvg2-sharp
%_datadir/vte-sharp
%_datadir/wnck-sharp
%_datadir/gnome-panel-sharp
%_datadir/gnome-print-sharp





