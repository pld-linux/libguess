Summary:	A high-speed character set detection library
Summary(pl.UTF-8):	Biblioteka do szybkiego rozpoznawania zestawu znaków
Name:		libguess
Version:	1.1
Release:	1
License:	BSD
Group:		Libraries
Source0:	http://distfiles.atheme.org/%{name}-%{version}.tar.bz2
# Source0-md5:	9a17e973bc03814170b4ed03172348dc
URL:		http://www.atheme.org/project/libguess
BuildRequires:	libmowgli-devel >= 0.9.50
BuildRequires:	pkgconfig
Requires:	libmowgli >= 0.9.50
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libguess is a high-speed character set detection library. It has two
functions:
- to determine encoding,
- to validate UTF-8 encoding.

%description -l pl.UTF-8
libguess to biblioteka do szybkiego rozpoznawania zestawu znaków. Ma
dwie funkcje:
- do określania kodowania,
- do sprawdzania poprawności kodowania UTF-8.

%package devel
Summary:	Header files for libguess library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libguess
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libguess library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libguess.

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
%doc COPYING README
%attr(755,root,root) %{_libdir}/libguess.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libguess.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguess.so
%{_includedir}/libguess
%{_pkgconfigdir}/libguess.pc
