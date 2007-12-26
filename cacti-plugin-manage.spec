%define		namesrc	manage
%include	/usr/lib/rpm/macros.perl
Summary:	Plugin for Cacti - dashboard for Network Services
Summary(pl.UTF-8):	Wtyczka do Cacti -
Name:		cacti-plugin-manage
Version:	0.5.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://gilles.boulon.free.fr/manage/%{namesrc}-%{version}.zip
# Source0-md5:	baa4298d38b914590a10794d2ccf07d1
URL:		http://forums.cacti.net/about13827.html
BuildRequires:	rpm-perlprov
Requires:	cacti
Requires:	cacti-plugin-thold
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		webcactipluginroot /usr/share/cacti/plugins/%{namesrc}

%description
Plugin for Cacti - This plugin allows you to automatically view your
network by checking :
- TCP Ports (all platforms which host TCP/IP services)
- Services and Processes (for Win32 only)

Up, down and reboot events :
- can be immediatly sent to you by email or "net send"
- are logged and available in Event Reporting

Features:
- Monitor TCP ports, windows services and processes for
- multiple hosts.
- Multiples views.
- You can associate an image with your host.
- Let you create Groups and Sites.
- You can display only hosts in error.
- Use AJAX.
- Use overlib to display graphs.
- Blink hostnames when a threshold is breaked. Use tresholds.
- You can set cycle time delay between groups.
- The time until the next graph change is displayed.
- You can click objects to access Reporting.
- Guest account can only view tab manage, not Reporting.
- Can set permissions on who can view.
- You can choose between SNMP, WMI (Vbs or Perl) and that i name
- "rrdtool" (it's the output from the poller).
- You can make themes for images. Alerts by sound.

%description -l pl.UTF-8
Wtyczka do Cacti -

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{webcactipluginroot}
cp -a * $RPM_BUILD_ROOT%{webcactipluginroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{webcactipluginroot}
