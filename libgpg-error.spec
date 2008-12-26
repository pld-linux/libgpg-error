# TODO: package lisp files?
#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	Library libgpg-error
Summary(pl.UTF-8):	Biblioteka libgpg-error
Name:		libgpg-error
Version:	1.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	ftp://ftp.gnupg.org/gcrypt/libgpg-error/%{name}-%{version}.tar.bz2
# Source0-md5:	62c0d09d1e76c5b6da8fff92314c4665
Patch0:		%{name}-pl.po-update.patch
Patch1:		%{name}-gpg_error_config.patch
URL:		http://www.gnupg.org/related_software/libgpg-error/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9.6
BuildRequires:	gettext-devel >= 0.15
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

%description -l pl.UTF-8
libgpg-error jest biblioteką definiującą wartości błędów wspólne dla
komponentów GnuPG. Są wśród nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przyszłości.

%package devel
Summary:	Header files for libgpg-error
Summary(pl.UTF-8):	Pliki nagłówkowe dla libgpg-error
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

This package contains the header files needed to develop programs that
use these libgpg-error.

%description devel -l pl.UTF-8
libgpg-error jest biblioteką definiującą wartości błędów wspólne dla
komponentów GnuPG. Są wśród nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przyszłości.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libgpg-error.

%package static
Summary:	Static version of libgpg-error library
Summary(pl.UTF-8):	Statyczna wersja biblioteki libgpg-error
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgpg-error is a library that defines common error values for all
GnuPG components. Among these are GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon and possibly more in the future.

This package contains the static libgpg-error libraries.

%description static -l pl.UTF-8
libgpg-error jest biblioteką definiującą wartości błędów wspólne dla
komponentów GnuPG. Są wśród nich GPG, GPGSM, GPGME, GPG-Agent,
libgcrypt, pinentry, SmartCard Daemon i inne - w przyszłości.

Pakiet zawiera statyczne biblioteki libgpg-error.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f po/stamp-po

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_lib}
mv -f $RPM_BUILD_ROOT%{_libdir}/libgpg-error.so.* $RPM_BUILD_ROOT/%{_lib}
ln -sf /%{_lib}/$(basename $RPM_BUILD_ROOT/%{_lib}/libgpg-error.so.*.*.*) \
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
%attr(755,root,root) %ghost /%{_lib}/libgpg-error.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gpg-error-config
%attr(755,root,root) %{_libdir}/libgpg-error.so
%{_libdir}/libgpg-error.la
%{_includedir}/gpg-error.h
%{_aclocaldir}/gpg-error.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgpg-error.a
%endif

#%files... lisp or -n lisp-%{name} ???
#%defattr(644,root,root,755)
#%{_datadir}/common-lisp/gpg-error*
