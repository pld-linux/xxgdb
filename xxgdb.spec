Summary:	An X Window System graphical interface for the GNU gdb debugger
Summary(pl):	Graficzny interfejs pod X Window do debuggera gdb
Name:		xxgdb
Version:	1.12
Release:	10
License:	MIT
Group:		Development/Debuggers
Group(de):	Entwicklung/Debugger
Group(pl):	Programowanie/Odpluskwiacze
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/debuggers/%{name}-%{version}.tar.gz
Source1:	%{name}.wmconfig
Patch0:		%{name}-1.08-glibc.patch
Patch1:		%{name}-1.12-sysv.patch
Patch2:		%{name}-1.12-compat21.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gdb

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xxgdb is an X Window System graphical interface to the GNU gdb debugger.
Xxgdb provides visual feedback and supports a mouse interface for the
user who wants to perform debugging tasks like the following:  controlling
program execution through breakpoints, examining and traversing the
function call stack, displaying values of variables and data structures,
and browsing source files and functions.

Install the xxgdb package if you'd like to use a graphical interface with
the GNU gdb debugger.  You'll also need to have the gdb package installed.

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1

%build
xmkmf
%{__make} CXXDEBUGFLAGS="%{rpmcflags}" \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/xxgdb

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxgdb
%config /usr/X11R6/lib/X11/app-defaults/XDbx
%{_mandir}/man1/xxgdb.1x*
/etc/X11/wmconfig/xxgdb
