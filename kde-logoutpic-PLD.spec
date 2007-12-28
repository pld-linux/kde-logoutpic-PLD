Summary:	PLD logoutpic for KDE
Summary(pl.UTF-8):	Obrazek okna wylogowania "PLD" dla KDE
Name:		kde-logoutpic-PLD
Version:	0.3
Release:	2
License:	GPL
Group:		Themes
Source0:	%{name}.png
Requires:	kdebase-desktop
Provides:	kde-logoutpic
Obsoletes:	kde-logoutpic-KDEGirl
Obsoletes:	kde-logoutpic-default
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PLD logoutpic for KDE.

%description -l pl.UTF-8
Obrazek okna wylogowania "PLD" dla KDE.

%prep
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/ksmserver/pics

install %{SOURCE0} \
	$RPM_BUILD_ROOT%{_datadir}/apps/ksmserver/pics/shutdownkonq.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/ksmserver/pics/shutdownkonq.png
