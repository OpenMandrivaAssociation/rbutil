%define Werror_cflags %nil

Summary:	Rockbox (rbutil) firmware for mp3 players 
Name:		rbutil
Version:	1.2.11
Release:	3
License:	GPLv2
Group:		System/Configuration/Hardware
URL:		https://www.rockbox.org/
Source:		http://download.rockbox.org/rbutil/source/%{name}_%{version}-src.tar.bz2
BuildRequires:	qt4-devel 
BuildRequires:	usb1-devel
Patch0:		werror_sec.patch
 

%description
Rockbox (rbutil) is an open source firmware for mp3 players, written from
scratch. It runs on a wide range of players:

* Apple: 1st through 5.5th generation iPod, iPod Mini and 1st generation iPod
Nano
(not the Shuffle, 2nd/3rd/4th gen Nano, Classic or Touch)
* Archos: Jukebox 5000, 6000, Studio, Recorder, FM Recorder, Recorder V2 and
Ondio
* Cowon: iAudio X5, X5V, X5L, M5, M5L, M3 and M3L
* iriver: iHP100 series, H100 series, H300 series and H10 series
* Olympus: M:Robe 100
* SanDisk: Sansa c200 series, e200 series and e200R series (not the AMS models)
* Toshiba: Gigabeat X and F series (not the S series) 

%prep
%setup -q -n %{name}_%{version}
%patch0 -p0

%build
cd rbutil/rbutilqt
lrelease rbutilqt.pro

%qmake_qt4
%make

%install
# menu 
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=RockBox
Comment=Firmware for mp3 players
Exec=rbutil
Icon=%{name}.png
Terminal=false
Type=Application
StartupNotify=true
Categories=System;Hardware;X-MandrivaLinux-System-Configuration-Hardware;
EOF

#icon
install -m 644 rbutil/rbutilqt/icons/%{name}.png -D %{buildroot}%{_iconsdir}/%{name}.png
install -m 755 rbutil/rbutilqt/RockboxUtility -D %{buildroot}%{_bindir}/%{name}


%files 
%{_bindir}/rbutil
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/%{name}.png


%changelog
* Fri Dec 09 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.2.11-1
+ Revision: 739380
- BR fix
- imported package rbutil

