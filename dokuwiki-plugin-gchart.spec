%define		plugin		gchart
Summary:	Google Chart Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	20081209
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dev.splitbrain.org/download/snapshots/gchart-plugin-latest.tgz
# Source0-md5:	cfa58e4bc6b06e388ceca8713f5f10b2
Source1:	dokuwiki-find-lang.sh
URL:		http://www.dokuwiki.org/plugin:gchart
Requires:	dokuwiki >= 20080505
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Allows to embed simple chart graphics using the Google Chart API.

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{CREDITS,changelog}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/*.php
%{plugindir}/conf
