%define gtk_sharp 2.12.2
%define gnome_sharp 2.24.0
%define monodir %{_prefix}/lib/mono

Summary:	C# language bindings for GNOME desktop
Name:		gnome-desktop-sharp
Version:	2.26.0
Release:	11
License:	LGPLv2
Group:		System/Libraries
Url:		http://www.mono-project.com/Main_Page
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%name/%{name}-%{version}.tar.bz2
Patch0:		gnome-desktop-sharp-2.26.0-new-libgnomedesktop-major.patch
BuildRequires:	mono-devel
BuildRequires:	gtk-sharp2-devel >= %{gtk_sharp}
BuildRequires:	gtk-sharp2 >= %{gtk_sharp}
BuildRequires:	glade-sharp2 >= %{gtk_sharp}
BuildRequires:	gnome-sharp2-devel >= %{gnome_sharp}
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libgtkhtml-3.14)
BuildRequires:	pkgconfig(vte)
BuildRequires:	pkgconfig(libpanelapplet-2.0)
BuildRequires:	pkgconfig(libgnomeprintui-2.2)
BuildRequires:	pkgconfig(gnome-desktop-2.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
Conflicts:	gnome-sharp2 < 2.19.90

%description
This contains C# language bindings for some of the GNOME desktop libraries.

%package devel
Summary:	C# language binding for the GNOME desktop - devel files
Group:		Development/Other
Requires:	%{name} = %{version}
Requires:	gtkhtml-sharp = %{version}
Requires:	vte-sharp = %{version}
Requires:	rsvg-sharp = %{version}
Requires:	wnck-sharp = %{version}
Requires:	gtksourceview-sharp2 = %{version}
Requires:	gnome-panel-sharp = %{version}
Requires:	gnome-print-sharp = %{version}
Conflicts:	gnome-desktop-sharp < 2.20.1-2

%description devel
This is a C# language binding for the GNOME desktop. It contains all
files that are needed to build against %{name}.

%package -n gnome-print-sharp
Group:		System/Libraries
Summary:	C# language binding for the GNOME print library

%description -n gnome-print-sharp
This contains the C# language binding for the GNOME print library.

%package -n gnome-panel-sharp
Group:		System/Libraries
Summary:	C# language binding for the GNOME panel

%description -n gnome-panel-sharp
This contains the C# language binding for the GNOME panel.

%package -n vte-sharp
Group:		System/Libraries
Summary:	C# language binding for VTE
Conflicts:	gnome-desktop-sharp < 2.20.1-2

%description -n vte-sharp
This contains the C# language binding for the VTE library.

%package -n rsvg-sharp
Group:		System/Libraries
Summary:	C# language binding for librsvg
Conflicts:	gnome-desktop-sharp < 2.20.1-2

%description -n rsvg-sharp
This contains the C# language binding for the librsvg library.

%package -n wnck-sharp
Group:		System/Libraries
Summary:	C# language binding for libwnck
Conflicts:	gnome-desktop-sharp < 2.20.1-2

%description -n wnck-sharp
This contains the C# language binding for the libwnck library.

%package -n gtkhtml-sharp
Group:		System/Libraries
Summary:	C# language binding for gtkhtml
Conflicts:	gnome-desktop-sharp < 2.20.1-2

%description -n gtkhtml-sharp
This contains the C# language binding for the gtkhtml library.

%package -n gtksourceview-sharp2
Group:		System/Libraries
Summary:	C# language binding for gtksourceview 2
Conflicts:	gnome-desktop-sharp < 2.20.1-2

%description -n gtksourceview-sharp2
This contains the C# language binding for the gtksourceview 2 library.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x --disable-static
make

%install
%makeinstall_std

%files
%doc README NEWS  HACKING AUTHORS
%{monodir}/gac/gnomedesktop-sharp
%{monodir}/gnomedesktop-sharp-2.20

%files -n gnome-print-sharp
%{monodir}/gac/gnome-print-sharp
%{monodir}/gnome-print-sharp-2.18

%files -n gnome-panel-sharp
%{monodir}/gac/gnome-panel-sharp
%{_libdir}/libgnomepanelsharpglue-2.so
%{monodir}/gnome-panel-sharp-2.24

%files -n vte-sharp
%{monodir}/gac/vte-sharp
%{_libdir}/libvtesharpglue-2.so
%{monodir}/vte-sharp-0.16

%files -n rsvg-sharp
%{monodir}/gac/rsvg2-sharp
%{monodir}/rsvg2-sharp-2.0

%files -n wnck-sharp
%{monodir}/gac/wnck-sharp
%{monodir}/wnck-sharp-2.20
%{_libdir}/libwncksharpglue-2.so

%files -n gtksourceview-sharp2
%{monodir}/gac/gtksourceview2-sharp
%{monodir}/gtksourceview2-sharp-2.0
%{_libdir}/libgtksourceview2sharpglue-2.so

%files -n gtkhtml-sharp
%{monodir}/gac/gtkhtml-sharp
%{monodir}/gtkhtml-sharp-3.14
%{_libdir}/libgtkhtmlsharpglue-2.so

%files devel
%doc ChangeLog
%{_libdir}/pkgconfig/gnome-desktop-sharp-2.0.pc
%{_libdir}/pkgconfig/gtkhtml-sharp-3.14.pc
%{_libdir}/pkgconfig/gtksourceview2-sharp.pc
%{_libdir}/pkgconfig/rsvg2-sharp-2.0.pc
%{_libdir}/pkgconfig/vte-sharp-0.16.pc
%{_libdir}/pkgconfig/wnck-sharp-1.0.pc
%{_libdir}/pkgconfig/gnome-panel-sharp-2.24.pc
%{_libdir}/pkgconfig/gnome-print-sharp-2.18.pc
%{_datadir}/gnomedesktop-sharp
%{_datadir}/gtkhtml-sharp
%{_datadir}/gtksourceview2-sharp
%{_datadir}/rsvg2-sharp
%{_datadir}/vte-sharp
%{_datadir}/wnck-sharp
%{_datadir}/gnome-panel-sharp
%{_datadir}/gnome-print-sharp

%changelog
* Thu Dec 15 2011 Götz Waschk <waschk@mandriva.org> 2.26.0-7mdv2012.0
+ Revision: 741537
- fix build deps
- rebuild for gtk+ packaging breakage

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.26.0-6
+ Revision: 664864
- mass rebuild

* Wed Jan 13 2010 Götz Waschk <waschk@mandriva.org> 2.26.0-5mdv2011.0
+ Revision: 490502
- patch for new libgnome-desktop

* Wed Jun 10 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-4mdv2010.0
+ Revision: 384680
- drop patch
- rebuild for new vte

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-3mdv2010.0
+ Revision: 382168
- new libvte major

* Thu Mar 12 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-2mdv2009.1
+ Revision: 354236
- disable nautilus-burn binding

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.26.0-1mdv2009.1
+ Revision: 347357
- new version
- drop patch

* Thu Jan 01 2009 Götz Waschk <waschk@mandriva.org> 2.24.0-3mdv2009.1
+ Revision: 323215
- new libgnome-desktop major

* Thu Nov 06 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-2mdv2009.1
+ Revision: 300172
- patch for new gnome-desktop major

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.24.0-1mdv2009.0
+ Revision: 282726
- new version
- bump deps

* Fri Sep 05 2008 Frederic Crozat <fcrozat@mandriva.com> 2.23.90-3mdv2009.0
+ Revision: 281214
- Add conflicts to ease upgrade from 2008.1

* Mon Aug 25 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-2mdv2009.0
+ Revision: 275842
- fix gnome panel dll mapping

* Thu Aug 21 2008 Götz Waschk <waschk@mandriva.org> 2.23.90-1mdv2009.0
+ Revision: 274514
- new version
- update build deps
- update file list
- add gnome-panel and gnome-print bindings

* Tue Aug 19 2008 Götz Waschk <waschk@mandriva.org> 2.20.1-4mdv2009.0
+ Revision: 273800
- rebuild

* Wed Jul 23 2008 Götz Waschk <waschk@mandriva.org> 2.20.1-3mdv2009.0
+ Revision: 242154
- patch for new libgnome-desktop

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.20.1-2mdv2009.0
+ Revision: 192446
- split package
- update buildrequires

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.20.1-1mdv2008.1
+ Revision: 183687
- new version

* Wed Mar 05 2008 Götz Waschk <waschk@mandriva.org> 2.20.0-1mdv2008.1
+ Revision: 179908
- fix buildrequires
- new version
- bump deps
- update file list
- drop patch

* Mon Jan 28 2008 Götz Waschk <waschk@mandriva.org> 2.19.1-1mdv2008.1
+ Revision: 159557
- new version
- drop patch 0

* Fri Jan 25 2008 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.1
+ Revision: 157888
- import gnome-desktop-sharp


* Fri Jan 25 2008 Götz Waschk <waschk@mandriva.org> 2.19.0-1mdv2008.1
- initial package
