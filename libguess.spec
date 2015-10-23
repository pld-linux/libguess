Summary:	A high-speed character set detection library
Summary(pl.UTF-8):	Biblioteka do szybkiego rozpoznawania zestawu znaków
Name:		libguess
Version:	1.2
Release:	1
License:	BSD
Group:		Libraries
# code developed at https://github.com/atheme/libguess (no releases tagged)
Source0:	http://rabbit.dereferenced.org/~nenolod/distfiles/%{name}-%{version}.tar.bz2
# Source0-md5:	7633fbfbeb75b1ded7f33cca3d8d4762
URL:		http://atheme.org/projects/libguess.html
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
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

%{__sed} -i -e '/^\.SILENT/d' buildsys.mk.in

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
%attr(755,root,root) %{_libdir}/libguess.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libguess.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libguess.so
%{_includedir}/libguess
%{_pkgconfigdir}/libguess.pc
