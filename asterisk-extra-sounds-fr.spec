%undefine __find_provides
%undefine __find_requires

Summary:	France sound files for the Asterisk PBX and telephony application and toolkit
Name:		asterisk-extra-sounds-fr
Version:	1.4.11
Release:	%mkrel 1
License:	Public Domain
Group:		System/Servers
URL:		http://www.asterisk.org/
#for I in alaw g722 g729 gsm siren7 siren14 sln16 ulaw wav ; do wget -c http://downloads.asterisk.org/pub/telephony/sounds/releases/asterisk-extra-sounds-fr-$I-1.4.9.tar.gz -P SOURCES ; done
Source0:	http://ftp.digium.com/pub/telephony/sounds/%{name}-alaw-%{version}.tar.gz
Source1:	http://ftp.digium.com/pub/telephony/sounds/%{name}-g722-%{version}.tar.gz
Source2:	http://ftp.digium.com/pub/telephony/sounds/%{name}-g729-%{version}.tar.gz
Source3:	http://ftp.digium.com/pub/telephony/sounds/%{name}-gsm-%{version}.tar.gz
Source4:	http://ftp.digium.com/pub/telephony/sounds/%{name}-siren7-%{version}.tar.gz
Source5:	http://ftp.digium.com/pub/telephony/sounds/%{name}-siren14-%{version}.tar.gz
Source6:	http://ftp.digium.com/pub/telephony/sounds/%{name}-sln16-%{version}.tar.gz
Source7:	http://ftp.digium.com/pub/telephony/sounds/%{name}-ulaw-%{version}.tar.gz
Source8:	http://ftp.digium.com/pub/telephony/sounds/%{name}-wav-%{version}.tar.gz
Requires:	asterisk
Provides:	asterisk-extra-sounds = %{version}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Asterisk is an Open Source PBX and telephony development platform that can both
replace a conventional PBX and act as a platform for developing custom
telephony applications for delivering dynamic content over a telephone
similarly to how one can deliver dynamic content through a web browser using
CGI and a web server.
 
Asterisk talks to a variety of telephony hardware including BRI, PRI, POTS, and
IP telephony clients using the Inter-Asterisk eXchange protocol (e.g. gnophone
or miniphone).

This package contains freely usable recorded sounds that were meant to be used
with Asterisk in the following formats: a-Law, G.722, G.729, GSM, Siren7, 
Siren14, sln16, mu-Law, WAV

%prep

%setup -q -c -T -n asterisk-extra-sounds-%{version} -a0 -a1 -a2 -a3 -a4 -a5 -a6 -a7 -a8

# fix dir perms
find . -type d | xargs chmod 755
    
# fix file perms
find . -type f | xargs chmod 644

# clean up CVS stuff
for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -r $i; fi >&/dev/null
done

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}/var/lib/asterisk/sounds/fr

find . -maxdepth 1 -not -iname . -exec cp -aRf {} %{buildroot}/var/lib/asterisk/sounds/fr \;

# cleanup
rm -f %{buildroot}/var/lib/asterisk/sounds/*-asterisk-extra-*-%{version}

# make a file list
find %{buildroot}/var/lib/asterisk/sounds/fr -type f | sed -e "s|%{buildroot}||" | sed -e 's/^/%attr(0644,root,root) /' >> %{name}.filelist

%clean
rm -rf %{buildroot}

%files -f %{name}.filelist
%defattr(-,root, root)
%doc *-asterisk-extra-*-%{version}


%changelog
* Sat Jul 10 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.11-1mdv2011.0
+ Revision: 550232
- 1.4.11

* Wed Jan 06 2010 Lonyai Gergely <aleph@mandriva.org> 1.4.10-1mdv2010.1
+ Revision: 486661
- 1.4.10

* Thu Aug 13 2009 Lonyai Gergely <aleph@mandriva.org> 1.4.9-1mdv2010.0
+ Revision: 416112
- initial release: 1.4.9
- create asterisk-extra-sounds-fr

