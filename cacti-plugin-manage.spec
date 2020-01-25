# TODO
# - bunch of bundled java jars (jta, sshtermapplet)
# - perl deps optional? required?
%define		plugin	manage
%define		php_min_version 5.0.0
Summary:	Plugin for Cacti - dashboard for Network Services
Summary(pl.UTF-8):	Wtyczka do Cacti - panel z usługami sieciowymi
Name:		cacti-plugin-%{plugin}
Version:	0.6.2
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://docs.cacti.net/_media/userplugin:%{plugin}-%{version}.zip
# Source0-md5:	70b64092a80114b4a9d36be0f1988d47
URL:		http://docs.cacti.net/userplugin:manage
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	unzip
Requires:	cacti >= 0.8.7g
Requires:	cacti(pia) >= 2.8
Requires:	cacti-plugin-settings >= 0.7
Requires:	php-common >= 4:%{php_min_version}
Suggests:	cacti-plugin-thold
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		cactidir		/usr/share/cacti
%define		plugindir		%{cactidir}/plugins/%{plugin}

%description
This Cacti plugin allows you to automatically view your network by
checking:
- TCP ports (all platforms which host TCP/IP services)
- Services and Processes (for Win32 only)

Up, down and reboot events:
- can be immediatly sent to you by email or "net send"
- are logged and available in Event Reporting

Features:
- Monitor TCP ports, Windows services and processes for multiple
  hosts.
- Multiples views.
- You can associate an image with your host.
- Let you create Groups and Sites.
- You can display only hosts in error.
- Use AJAX.
- Use overlib to display graphs.
- Blink hostnames when a threshold is breaked.
- You can set cycle time delay between groups.
- The time until the next graph change is displayed.
- You can click objects to access Reporting.
- Guest account can only view tab manage, not Reporting.
- Can set permissions on who can view.
- You can choose between SNMP, WMI (Vbs or Perl) and that I name
  "rrdtool" (it's the output from the poller).
- You can make themes for images.
- Alerts by sound.

%description -l pl.UTF-8
Ta wtyczka Cacti umożliwia automatyczny podgląd sieci poprzez
sprawdzanie:
- portów TCP (na wszystkich platformach z usługami TCP/IP)
- usługi i procesy (tylko Win32)

Informacje o zdarzeniach włączenia, wyłączenia i restartu:
- mogą być automatycznie przesłane pocztą lub przez sieć
- są logowane i dostępne przez raportowanie zdarzeń

Możliwości:
- monitorowanie na wielu hostach portów TCP, a pod Windows także usług
  i procesów;
- wiele widoków;
- można łączyć obrazki z hostami;
- można tworzyć grupy i serwisy;
- można wyświetlać tylko hosty z błędami;
- wykorzystanie AJAX;
- wykorzystanie biblioteki overlib do wyświetlania wykresów;
- migotanie nazw hostów po przekroczeniu określonego progu;
- można ustawić cykliczne opóźnienia między grupami;
- wyświetlany jest czas do następnej zmiany wykresu;
- do raportów można dostać się klikając na obiektach;
- osoby korzystające z konta gościa mogą oglądać tylko zakładkę
  zarządzania, nie raporty
- można ustawiać uprawnienia do widoków;
- można wybrać między SNMP, WMI (Vbs lub Perl) i czymś o nazwie
  "rrdtool" (wyjściem z pollera);
- można ustawiać motywy obrazków;
- dźwiękowe alarmy.

%prep
%setup -qc
mv %{plugin}/#INSTALL.txt INSTALL
mv %{plugin}/#readme-*.txt README

# bad os
rm %{plugin}/*.bat
rm %{plugin}/*.exe

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a %{plugin}/* $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL README
%{plugindir}
