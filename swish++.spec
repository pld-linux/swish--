%include        /usr/lib/rpm/macros.perl
Summary:	Simple Web Indexing System for Humans
Summary(pl):	Prosty system indeksowania stron WWW
Name:		swish++
Version:	5.9.5
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://homepage.mac.com/pauljlucas/software/%{name}-%{version}.tar.gz
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

%description -l pl
SWISH++ jest bazuj�cym na Uniksie systemem indeksowania oraz silnikiem
wyszukiwarki (typowo u�ywanym do indeksowania oraz przeszukiwania
plik�w na stronach www).

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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
%doc www_example/* Changes Email* README
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man?/*