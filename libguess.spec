Summary:	A high-speed character set detection library
Name:		libguess
Version:	1.1
Release:	1
License:	Other
Group:		Applications/System
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.bz2
# Source0-md5:	9a17e973bc03814170b4ed03172348dc
URL:		http://www.atheme.org/project/libguess
BuildRequires:	libmowgli-devel >= 0.9.50
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A high-speed character set detection library

libguess has two functions:

libguess_determine_encoding(const char *inbuf, int length, const char
- *region); This detects a character set. Returns an appropriate
  charset name that can be passed to iconv_open(). Region is the name of
  the language or region that the data is related to, e.g. 'Baltic' for
  the Baltic states, or 'Japanese' for Japan.

libguess_validate_utf8(const char *inbuf, int length); This employs
libguess's DFA-based character set validation rules to ensure that a
string is pure UTF-8. GLib's UTF-8 validation functions are broken,
for example.

%package devel
Summary:	Header files and development documentation for libguess
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libguess
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
Header files and development documentation for libguess.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libguess.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguess.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libguess.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguess.so
%{_includedir}/libguess
%{_pkgconfigdir}/libguess.pc
