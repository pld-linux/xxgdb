Summary:	An X Window System graphical interface for the GNU gdb debugger
Summary(es):	Interface X para el depurador gdb
Summary(pl):	Graficzny interfejs pod X Window do debuggera gdb
Summary(pt_BR):	Interface X para o depurador gdb
Summary(ru):	X-интерфейс к отладчику gdb
Summary(uk):	X-╕нтерфейс до в╕дладчика gdb
Name:		xxgdb
Version:	1.12
Release:	20
License:	MIT
Group:		Development/Debuggers
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/debuggers/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-sysv.patch
Patch2:		%{name}-compat21.patch
BuildRequires:	XFree86-devel
Requires:	gdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xxgdb is an X Window System graphical interface to the GNU gdb
debugger. Xxgdb provides visual feedback and supports a mouse
interface for the user who wants to perform debugging tasks like the
following: controlling program execution through breakpoints,
examining and traversing the function call stack, displaying values of
variables and data structures, and browsing source files and
functions.

%description -l es
xxgdb es una interface grАfica para el debugger de GNU. Tiene la
habilidad de enseЯar archivos fuente mientras se ejecutan, y
configurar "breakpoints", paso a paso, a travИs de los comandos - todo
con una interface grАfica X Window muy sencilla de usar.

%description -l pl
xxgdb to graficzny interfejs dla X Window System do debuggera GNU gdb.
xxgdb daje wizualny interfejs z obsЁug╠ myszy do takich zadaЯ jak:
kontrola wykonywania programu poprzez breakpointy, sprawdzanie i
przegl╠danie stosu, wy╤wietlanie zmiennych i struktur danych,
przegl╠danie plikСw ╪rСdЁowych i funkcji.

%description -l pt_BR
xxgdb И uma interface grАfica para o debugger da GNU. Ele tem a
habilidade de mostrar arquivos fonte enquanto eles sЦo executados,
configura "breakpoints", e passo a passo atravИs dos comandos - tudo
com uma interface grАfica X Window muito simples de se usar.

%description -l ru
xxgdb - это графический интерфейс к отладчику GNU Debugger (gdb).
Позволяет показывать исходные файлы по мере исполнения кода,
устанавливать точки отладочных остановов и исполнять команды по шагам
- все через простой в использовании графический интерфейс X Window.

%description -l uk
xxgdb - це граф╕чний ╕нтерфейс до в╕дладчика GNU Debugger (gdb).
Дозволя╓ показувати вих╕дн╕ файли в ход╕ виконання ╖х коду,
встановлювати точки в╕дладочних зупинок и виконувати команди по крокам
- все через простий у користуванн╕ граф╕чний ╕нтер╕ейс п╕д X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
xmkmf -a
%{__make} \
	CC=%{__cc} \
	CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	DEFGDB="-DGDB -DCREATE_IO_WINDOW"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Development,%{_pixmapsdir}}

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxgdb
%{_libdir}/X11/app-defaults/XDbx
%{_mandir}/man1/xxgdb.1x*
%{_applnkdir}/Development/xxgdb.desktop
%{_pixmapsdir}/*
