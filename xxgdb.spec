Summary: An X Window System graphical interface for the GNU gdb debugger.
Name: xxgdb
Version: 1.12
Release: 10
Copyright: MIT
Group: Development/Debuggers
Source: ftp://sunsite.unc.edu/pub/Linux/devel/debuggers/xxgdb-1.12.tar.gz
Source1: xxgdb.wmconfig
Patch: xxgdb-1.08-glibc.patch
Patch1: xxgdb-1.12-sysv.patch
Patch2: xxgdb-1.12-compat21.patch
BuildRoot: /var/tmp/%{name}-root
Requires: gdb

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
%setup -q -n xxgdb-1.12
%patch0 -p1
%patch1 -p1
%patch2 -p1 -b .compat21

%build
xmkmf
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install install.man

( cd $RPM_BUILD_ROOT
  mkdir -p ./etc/X11/wmconfig
  install -m 644 $RPM_SOURCE_DIR/xxgdb.wmconfig ./etc/X11/wmconfig/xxgdb
)

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/X11R6/bin/xxgdb
%config /usr/X11R6/lib/X11/app-defaults/XDbx
/usr/X11R6/man/man1/xxgdb.1x
/etc/X11/wmconfig/xxgdb
