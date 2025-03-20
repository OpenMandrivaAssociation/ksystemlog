#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
Summary:	System log viewer tool for KDE4
Name:		plasma6-ksystemlog
Version:	24.12.3
Release:	%{?git:0.%{git}.}2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
%if 0%{?git:1}
Source0:	https://invent.kde.org/system/ksystemlog/-/archive/%{gitbranch}/ksystemlog-%{gitbranchd}.tar.bz2#/ksystemlog-%{git}.tar.bz2
%else
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/ksystemlog-%{version}.tar.xz
%endif
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6PrintSupport)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6Core5Compat)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	cmake(KF6XmlGui)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6WidgetsAddons)
BuildRequires:	cmake(KF6ItemViews)
BuildRequires:	cmake(KF6IconThemes)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Archive)
BuildRequires:	cmake(KF6DocTools)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Completion)
BuildRequires:	cmake(KF6TextWidgets)

%description
This program is developed for being used by beginner users, which don't know
how to find information about their Linux system, and how the log files are
in their computer. But it is also designed for advanced users, who want to
quickly see problems occuring on their server.

KSystemLog has the following features :
- View all the main log of your system, by selecting them directly in a menu
- Auto display new lines logged in bold
- Tabbed view to allow displaying several logs at the same time
- Saving in a file and copying to clipboard the selected log lines are also
  implemented (and email to your friends)
- It can parse the following log files of your system:
  - X.org (or Xfree) logs
  - System logs (using the Syslog parser of KSystemLog)
  - Kernel logs
  - Daemons logs
  - Cron logs
  - Boot logs
  - Authentication logs
  - Cups logs
  - ACPID logs

%files -f ksystemlog.lang
%{_bindir}/ksystemlog
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/org.kde.ksystemlog.appdata.xml
%{_datadir}/qlogging-categories6/ksystemlog.categories

#------------------------------------------------------------------------

%prep
%autosetup -p1 -n ksystemlog-%{?git:%{gitbranchd}}%{!?git:%{version}}
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang ksystemlog --with-html
