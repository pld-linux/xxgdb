Summary:	An X Window System graphical interface for the GNU gdb debugger
Summary(es.UTF-8):   Interface X para el depurador gdb
Summary(pl.UTF-8):   Graficzny interfejs pod X Window do debuggera gdb
Summary(pt_BR.UTF-8):   Interface X para o depurador gdb
Summary(ru.UTF-8):   X-интерфейс к отладчику gdb
Summary(uk.UTF-8):   X-інтерфейс до відладчика gdb
Name:		xxgdb
Version:	1.12
Release:	20
License:	MIT
Group:		Development/Debuggers
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/debuggers/%{name}-%{version}.tar.gz
# Source0-md5:	d7e447aeb9cab29a90d9d65f8f9a306c
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-glibc.patch
Patch1:		%{name}-sysv.patch
Patch2:		%{name}-compat21.patch
BuildRequires:	XFree86-devel
Requires:	gdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Xxgdb is an X Window System graphical interface to the GNU gdb
debugger. Xxgdb provides visual feedback and supports a mouse
interface for the user who wants to perform debugging tasks like the
following: controlling program execution through breakpoints,
examining and traversing the function call stack, displaying values of
variables and data structures, and browsing source files and
functions.

%description -l es.UTF-8
xxgdb es una interface gráfica para el debugger de GNU. Tiene la
habilidad de enseñar archivos fuente mientras se ejecutan, y
configurar "breakpoints", paso a paso, a través de los comandos - todo
con una interface gráfica X Window muy sencilla de usar.

%description -l pl.UTF-8
xxgdb to graficzny interfejs dla X Window System do debuggera GNU gdb.
xxgdb daje wizualny interfejs z obsługą myszy do takich zadań jak:
kontrola wykonywania programu poprzez breakpointy, sprawdzanie i
przeglądanie stosu, wyświetlanie zmiennych i struktur danych,
przeglądanie plików źródłowych i funkcji.

%description -l pt_BR.UTF-8
xxgdb é uma interface gráfica para o debugger da GNU. Ele tem a
habilidade de mostrar arquivos fonte enquanto eles são executados,
configura "breakpoints", e passo a passo através dos comandos - tudo
com uma interface gráfica X Window muito simples de se usar.

%description -l ru.UTF-8
xxgdb - это графический интерфейс к отладчику GNU Debugger (gdb).
Позволяет показывать исходные файлы по мере исполнения кода,
устанавливать точки отладочных остановов и исполнять команды по шагам
- все через простой в использовании графический интерфейс X Window.

%description -l uk.UTF-8
xxgdb - це графічний інтерфейс до відладчика GNU Debugger (gdb).
Дозволяє показувати вихідні файли в ході виконання їх коду,
встановлювати точки відладочних зупинок и виконувати команди по крокам
- все через простий у користуванні графічний інтеріейс під X Window.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
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
