Summary:	System log viewer tool for KDE4
Name:		ksystemlog
Version:	21.03.90
Release:	1
Epoch:		2
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	http://download.kde.org/%{ftpdir}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake(ECM)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5PrintSupport)
BuildRequires:	pkgconfig(Qt5Concurrent)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	cmake(KF5XmlGui)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5ItemViews)
BuildRequires:	cmake(KF5IconThemes)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Archive)
BuildRequires:	cmake(KF5DocTools)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Completion)
BuildRequires:	cmake(KF5TextWidgets)

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

%files -f %{name}.lang
%{_bindir}/ksystemlog
%{_datadir}/applications/*.desktop
%{_datadir}/kxmlgui5/ksystemlog
%{_datadir}/metainfo/org.kde.ksystemlog.appdata.xml
%{_datadir}/qlogging-categories5/ksystemlog.categories

#------------------------------------------------------------------------

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang %{name} --with-html
