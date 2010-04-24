%define		svnrev		1108995
%define		_kdever		4.4.2
%define		_qtver		4.6.2

Summary:	Web development tools for KDE4
Summary(es.UTF-8):	Uno editor WEB para KDE4
Summary(pl.UTF-8):	Narzędzia do tworzenia WWW dla KDE4
Summary(pt_BR.UTF-8):	Um editor web para o KDE4
Name:		quanta
Version:	3.9.0
Release:	0.%{svnrev}.1
Epoch:		2
License:	GPL
Group:		X11/Development/Tools
# get it via: svn co svn://anonsvn.kde.org/home/kde/trunk/extragear/sdk/quanta
Source0:	%{name}-%{svnrev}.tar.bz2
# Source0-md5:	a3950e0168151b51719d43c6b8ebf4da	
URL:		http://www.kde.org/
BuildRequires:	Qt3Support-devel >= %{_qtver}
BuildRequires:	QtCore-devel >= %{_qtver}
BuildRequires:	QtGui-devel >= %{_qtver}
BuildRequires:	QtXml-devel >= %{_qtver}
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{_kdever}
BuildRequires:	kde4-kdevplatform-devel >= 0.9.98
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	phonon-devel >= 4.3.80
BuildRequires:	qt4-build >= %{_qtver}
BuildRequires:	qt4-qmake >= %{_qtver}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	tidy-devel
Requires:	kde4-kdebase >= %{_kdever}
# Applications required for full functionality:
Suggests:	kde4-kdesdk-kompare
Suggests:	kde4-kdewebdev-kfilereplace
Suggests:	kde4-kdewebdev-kimagemapeditor
Suggests:	kde4-kdewebdev-klinkstatus
Suggests:	kde4-kdevelop-plugin-css
Suggests:	kde4-kdevelop-plugin-php
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Quanta Plus is a web development tool for the K Desktop Environment.
Quanta is designed for quick web development and is rapidly becoming a
mature editor with a number of great features.

%description -l es.UTF-8
Quanta Plus és una herramienta de desarrollo web para KDE4. Es
projetado para rapido desarrollo web e es casi pronto com excelent
quantidad de caracteristicas.

%description -l pl.UTF-8
Quanta Plus to narzędzie do tworzenia WWW dla środowiska KDE4. Służy do
szybkiego tworzenia stron i staje się dojrzałym edytorem z wieloma
przydatnymi możliwościami.

%description -l pt_BR.UTF-8
O Quanta Plus é uma ferramenta para desenvolvimento web para o KDE4.
É projetado para desenvolvimento web rápido e está rapidamente se
tornando um editor maduro com um bom número de excelentes
características.

%prep
%setup -q -n %{name}-%{svnrev}

%build
install -d build
cd build
%cmake \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DSYSCONF_INSTALL_DIR=%{_sysconfdir} \
	-LIBTIDY_INCLUDE_DIR=%{_includedir} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/quanta
%attr(755,root,root) %{_libdir}/kde4/kcm_kdev_usertoolbars.so
%attr(755,root,root) %{_libdir}/kde4/libkdevcreatequantaproject.so
%attr(755,root,root) %{_libdir}/kde4/libkdevhtmlpreview.so
%attr(755,root,root) %{_libdir}/kde4/libkdevquantacore.so
%attr(755,root,root) %{_libdir}/kde4/libkdevquantafilestree.so
%attr(755,root,root) %{_libdir}/kde4/libkdevstructuretree.so
%attr(755,root,root) %{_libdir}/kde4/libkdevtemplatestree.so
%attr(755,root,root) %{_libdir}/kde4/libkdevusertoolbars.so
%attr(755,root,root) %{_libdir}/libkdevquanta.so*
%{_datadir}/apps/kdevcreatequantaproject
%dir %{_datadir}/apps/kdevhtmlpreview
%{_datadir}/apps/kdevhtmlpreview/kdevhtmlpreview.rc
%{_datadir}/apps/kdevplatform/profiles/quanta
%{_datadir}/apps/kdevquantacore
%{_datadir}/apps/kdevquantafilestree
%dir %{_datadir}/apps/kdevstructuretree
%{_datadir}/apps/kdevstructuretree/kdevstructuretree.rc
%dir %{_datadir}/apps/kdevtemplatestree
%{_datadir}/apps/kdevtemplatestree/kdevtemplatestree.rc
%{_datadir}/apps/kdevusertoolbars
%{_datadir}/apps/quanta
%{_datadir}/config.kcfg/quanta.kcfg
%{_datadir}/kde4/services/kcm_kdev_usertoolbars.desktop
%{_datadir}/kde4/services/kdevcreatequantaproject.desktop
%{_datadir}/kde4/services/kdevhtmlpreview.desktop
%{_datadir}/kde4/services/kdevquantacore.desktop
%{_datadir}/kde4/services/kdevquantafilestree.desktop
%{_datadir}/kde4/services/kdevstructuretree.desktop
%{_datadir}/kde4/services/kdevtemplatestree.desktop
%{_datadir}/kde4/services/kdevusertoolbars.desktop
%{_datadir}/kde4/servicetypes/kdevplatformquanta.desktop
%{_desktopdir}//kde4/quanta.desktop
%{_iconsdir}/[!l]*/*/apps/quanta.png
