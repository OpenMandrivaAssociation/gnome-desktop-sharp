%define name gnome-desktop-sharp
%define version 2.19.1
%define release %mkrel 1
%define gtk_sharp 2.11.0
%define gnome_sharp 2.19.90
%define monodir %_prefix/lib/mono

Summary: C# language bindings for GNOME desktop
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch1: gnome-desktop-sharp-2.19.0-dllmap.patch
License: LGPLv2
Group: System/Libraries
Url: http://www.mono-project.com/Main_Page
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel >= %{gtk_sharp}
BuildRequires:	gtk-sharp2 >= %{gtk_sharp}
BuildRequires:	glade-sharp2 >= %{gtk_sharp}
BuildRequires:	librsvg-devel >= 2.18.2
BuildRequires:	libgtkhtml-3.14-devel >= 3.16.0
BuildRequires:	vte-devel >= 0.16.9
BuildRequires:	libnautilus-cd-burner-devel >= 2.20.0
BuildRequires:	gnome-desktop-devel
BuildRequires:	libwnck-devel >= 2.20.0
BuildRequires:	gnome-sharp2 >= %{gnome_sharp}
Conflicts: gnome-sharp2 < 2.19.90

%description
This contains C# language bindings for some of the GNOME desktop libraries.

%prep
%setup -q
%patch1 -p1
autoconf

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
%_libdir/libvtesharpglue-2.so
%monodir/gac/gnomedesktop-sharp
%monodir/gac/gtkhtml-sharp
%monodir/gac/nautilusburn-sharp
%monodir/gac/rsvg2-sharp
%monodir/gac/vte-sharp
%monodir/gac/wnck-sharp
%monodir/gnomedesktop-sharp-2.20
%monodir/gtkhtml-sharp-3.14
%monodir/nautilusburn-sharp-2.20
%monodir/rsvg2-sharp-2.0
%monodir/vte-sharp-0.16
%monodir/wnck-sharp-2.20
%_libdir/pkgconfig/gnome-desktop-sharp-2.0.pc
%_libdir/pkgconfig/gtkhtml-sharp-3.14.pc
%_libdir/pkgconfig/nautilusburn-sharp.pc
%_libdir/pkgconfig/rsvg2-sharp-2.0.pc
%_libdir/pkgconfig/vte-sharp-0.16.pc
%_libdir/pkgconfig/wnck-sharp-1.0.pc
%_datadir/gnomedesktop-sharp
%_datadir/gtkhtml-sharp
%_datadir/nautilusburn-sharp
%_datadir/rsvg2-sharp
%_datadir/vte-sharp
%_datadir/wnck-sharp




