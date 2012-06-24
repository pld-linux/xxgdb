Summary:	An X Window System graphical interface for the GNU gdb debugger
Summary(es):	Interface X para el depurador gdb
Summary(pl):	Graficzny interfejs pod X Window do debuggera gdb
Summary(pt_BR):	Interface X para o depurador gdb
Summary(ru):	X-��������� � ��������� gdb
Summary(uk):	X-��������� �� צ�������� gdb
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
xxgdb es una interface gr�fica para el debugger de GNU. Tiene la
habilidad de ense�ar archivos fuente mientras se ejecutan, y
configurar "breakpoints", paso a paso, a trav�s de los comandos - todo
con una interface gr�fica X Window muy sencilla de usar.

%description -l pl
xxgdb to graficzny interfejs dla X Window System do debuggera GNU gdb.
xxgdb daje wizualny interfejs z obs�ug� myszy do takich zada� jak:
kontrola wykonywania programu poprzez breakpointy, sprawdzanie i
przegl�danie stosu, wy�wietlanie zmiennych i struktur danych,
przegl�danie plik�w �r�d�owych i funkcji.

%description -l pt_BR
xxgdb � uma interface gr�fica para o debugger da GNU. Ele tem a
habilidade de mostrar arquivos fonte enquanto eles s�o executados,
configura "breakpoints", e passo a passo atrav�s dos comandos - tudo
com uma interface gr�fica X Window muito simples de se usar.

%description -l ru
xxgdb - ��� ����������� ��������� � ��������� GNU Debugger (gdb).
��������� ���������� �������� ����� �� ���� ���������� ����,
������������� ����� ���������� ��������� � ��������� ������� �� �����
- ��� ����� ������� � ������������� ����������� ��������� X Window.

%description -l uk
xxgdb - �� ���Ʀ���� ��������� �� צ�������� GNU Debugger (gdb).
������Ѥ ���������� ��Ȧ�Φ ����� � ��Ħ ��������� �� ����,
������������� ����� צ��������� ������� � ���������� ������� �� ������
- ��� ����� ������� � ����������Φ ���Ʀ���� ����Ҧ��� Ц� X Window.

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
