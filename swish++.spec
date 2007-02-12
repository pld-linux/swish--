%include	/usr/lib/rpm/macros.perl
Summary:	Simple Web Indexing System for Humans
Summary(pl.UTF-8):	Prosty system indeksowania stron WWW
Name:		swish++
Version:	6.0.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://homepage.mac.com/pauljlucas/software/%{name}-%{version}.tar.gz
# Source0-md5:	3a81a1ca59addd6198f89e680bc77bff
Patch0:		%{name}-debian.patch
Patch1:		%{name}-splitmailbox.patch
URL:		http://homepage.mac.com/pauljlucas/software/swish/
BuildRequires:	libstdc++-devel
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-modules >= 5.6
Obsoletes:	aspseek
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWISH++ is a Unix-based file indexing and searching engine (typically
used to index and search files on web sites).

%description -l pl.UTF-8
SWISH++ jest bazującym na Uniksie systemem indeksowania oraz silnikiem
wyszukiwarki (typowo używanym do indeksowania oraz przeszukiwania
plików na stronach WWW).

%prep
%setup -q
%patch0 -p1
#%patch1 -p1

%build
%{__make} CC="%{__cxx}" CXX="%{__cxx}" OPTIM="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	I_OWNER="" \
	I_GROUP=""

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc www_example/* BUGS Changes README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man?/*
