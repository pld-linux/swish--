%include        /usr/lib/rpm/macros.perl
Summary:	Simple Web Indexing System for Humans
Summary(pl):	Prosty system indeksowania stron WWW
Name:		swish++
Version:	5.7
Release:	1
License:	GPL
Group:		Applications/Text
Group(cs):	Aplikace/Text
Group(da):	Programmer/Tekst
Group(de):	Applikationen/Text
Group(es):	Aplicaciones/Texto
Group(fr):	Applications/Texte
Group(is):	Forrit/Texti
Group(it):	Applicazioni/Testo
Group(ja):	¥¢¥×¥ê¥±¡¼¥·¥ç¥ó/¥Æ¥­¥¹¥È
Group(no):	Applikasjoner/Tekst
Group(pl):	Aplikacje/Tekst
Group(pt):	Aplicações/Texto
Group(ru):	ðÒÉÌÏÖÅÎÉÑ/ôÅËÓÔÏ×ÙÅ ÕÔÉÌÉÔÙ
Group(sl):	Programi/Besedilo
Group(sv):	Tillämpningar/Text
Group(uk):	ðÒÉËÌÁÄÎ¦ ðÒÏÇÒÁÍÉ/ôÅËÓÔÏ×¦ ÕÔÉÌ¦ÔÉ
Source0:	http://homepage.mac.com/pauljlucas/software/%{name}-%{version}.tar.gz
Patch0:		%{name}-debian.patch
URL:		http://homepage.mac.com/pauljlucas/software/swish/
BuildRequires:	libstdc++-devel
BuildRequires:  rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-modules >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SWISH++ is a Unix-based file indexing and searching engine (typically
used to index and search files on web sites).

%description -l pl
SWISH++ jest bazuj±cym na Uniksie systemem indeksowania oraz silnikiem
wyszukiwarki (typowo u¿ywanym do indeksowania oraz przeszukiwania
plików na stronach www).

%prep
%setup -q
%patch0 -p1

%build
%{__make} CC="%{__cxx}" CXX="%{__cxx}" OPTIM="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	I_OWNER="" \
	I_GROUP=""

gzip -9nf www_example/* Changes Email* README

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc */*.gz *.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}
%{_mandir}/man?/*
