Summary:	Library libgpg-error
Summary(pl):	Biblioteka libgpg-error
Name:		libgpg-error
Version:	1.1
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.gz
# Source0-md5:	ee23cdd5fbbb1483676647a8e091ff8e
Patch0:		%{name}-pl.po-update.patch
URL:		http://www.gnupg.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake >= 1:1.7.6
BuildRequires:	gettext-devel >= 0.12.1
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

%description -l pl
libgpg-error jest bibliotek± definiuj±c± warto¶ci b³êdów wspólne dla
komponentów GnuPG. S± w¶ród nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przysz³o¶ci.

%package devel
Summary:	Header files for libgpg-error
Summary(pl):	Pliki nag³ówkowe dla libgpg-error
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

This package contains the header files needed to develop programs that
use these libgpg-error.

%description devel -l pl
libgpg-error jest bibliotek± definiuj±c± warto¶ci b³êdów wspólne dla
komponentów GnuPG. S± w¶ród nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przysz³o¶ci.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libgpg-error.

%package static
Summary:	Static version of libgpg-error library
Summary(pl):	Statyczna wersja biblioteki libgpg-error
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

This package contains the static libgpg-error libraries.

%description static -l pl
libgpg-error jest bibliotek± definiuj±c± warto¶ci b³êdów wspólne dla
komponentów GnuPG. S± w¶ród nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przysz³o¶ci.

Pakiet zawiera statyczne biblioteki libgpg-error.

%prep
%setup -q
%patch0 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libgpg-error.so.*.*.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(cd $RPM_BUILD_ROOT/%{_lib}; echo libgpg-error.so.*.*.*) \
	$RPM_BUILD_ROOT%{_libdir}/libgpg-error.so

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS
%attr(755,root,root) %{_bindir}/gpg-error
%attr(755,root,root) /%{_lib}/libgpg-error.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpg-error-config
%attr(755,root,root) %{_libdir}/libgpg-error.so
%{_libdir}/libgpg-error.la
%{_includedir}/*.h
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libgpg-error.a
