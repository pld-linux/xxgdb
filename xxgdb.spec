Summary:	An X Window System graphical interface for the GNU gdb debugger.
Name:		xxgdb
Version:	1.12
Release:	10
Copyright:	MIT
Group:		Development/Debuggers
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/debuggers/%{name}-%{version}.tar.gz
Source1:	xxgdb.wmconfig
Patch0:		xxgdb-1.08-glibc.patch
Patch1:		xxgdb-1.12-sysv.patch
Patch2:		xxgdb-1.12-compat21.patch
BuildRoot:	/tmp/%{name}-root
Requires:	gdb

%define		_prefix		/usr/X11R6
%define		_mandir		/usr/X11R6/man

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
make CXXDEBUGFLAGS="$RPM_OPT_FLAGS" \
	CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make install install.man DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/etc/X11/wmconfig
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/xxgdb

strip --strip-unneeded $RPM_BUILD_ROOT%{_bindir}/xxgdb

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/xxgdb.1x

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xxgdb
%config /usr/X11R6/lib/X11/app-defaults/XDbx
%{_mandir}/man1/xxgdb.1x.gz
/etc/X11/wmconfig/xxgdb
