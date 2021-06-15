Summary:	Yamagi Quake II client
Name:		yamagi-quake2
Version:	8.00
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://deponie.yamagi.org/quake2/quake2-%{version}.tar.xz
# Source0-md5:	e0c7fb6031e2cbf4396959b074ec7d72
URL:		https://www.yamagi.org/quake2/
BuildRequires:	OpenAL-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL2-devel
BuildRequires:	cmake >= 3.0
BuildRequires:	curl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		gamedir		%{_libdir}/%{name}

%description
Yamagi Quake II is an enhanced client for id Software's Quake II with
focus on offline and coop gameplay. Both the gameplay and the graphics
are unchanged, but many bugs in the last official release were fixed
and some nice to have features like widescreen support and a modern
OpenGL 3.2 renderer were added. Unlike most other Quake II source
ports Yamagi Quake II is fully 64-bit clean. It works perfectly on
modern processors and operating systems.

%prep
%setup -q -n quake2-%{version}

%build
mkdir -p build
cd build
%cmake .. \
	-DSYSTEMWIDE_SUPPORT=ON
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{gamedir}/baseq2}

cd build/release
install -p q2ded quake2 *.so $RPM_BUILD_ROOT%{gamedir}
install -p baseq2/*.so $RPM_BUILD_ROOT%{gamedir}/baseq2
ln -s %{gamedir}/quake2 $RPM_BUILD_ROOT%{_bindir}/yamagi-quake2
ln -s %{gamedir}/q2ded $RPM_BUILD_ROOT%{_bindir}/yamagi-q2ded

cd ../../stuff
install -p yq2.cfg $RPM_BUILD_ROOT%{gamedir}/baseq2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/*.md
%{_bindir}/yamagi-quake2
%{_bindir}/yamagi-q2ded
%dir %{gamedir}
%attr(755,root,root) %{gamedir}/quake2
%attr(755,root,root) %{gamedir}/q2ded
%attr(755,root,root) %{gamedir}/ref_gl1.so
%attr(755,root,root) %{gamedir}/ref_gl3.so
%attr(755,root,root) %{gamedir}/ref_soft.so
%dir %{gamedir}/baseq2
%attr(755,root,root) %{gamedir}/baseq2/game.so
%{gamedir}/baseq2/yq2.cfg
