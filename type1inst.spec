Summary:	Type 1 font install utility
Summary(pl):	Narzêdzie instalacyjne czcionek Type 1
Name:		type1inst
Version:	0.6.1
Release:	4
License:	GPL
Group:		Applications
Source0:	ftp://sunsite.unc.edu/pub/Linux/X11/xutils/%{name}-%{version}.tar.gz
Patch0:		%{name}-chmod.patch
URL:		http://goblet.anu.edu.au/~m9305357/type1inst.html
Requires:	groff
Requires:	perl
Requires:	fileutils
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
type1inst is a utility which scans Type 1 PostScript font files and
generates automatically the fonts.scale file which the X Window System
uses to pick up fonts in the current directory and/or the Fontmap file
which Ghostscript uses to map file names to font names. It can also
generate simple font sample sheets which show what your fonts look
like.

type1inst is a Perl script so you will need to have that installed on
your system. The pfbtops utility (which comes as part of GNU groff) is
also required.

%description -l pl
type1inst jest programem, który skanuje pliki czcionek PostScript Type
1 i tworzy plik fonts.scale i/lub plik Fontmap na u¿ytek X Window
System i Ghostscript. Potrafi równie¿ wygenerowaæ proste przyk³ady
zainstalowanych czcionek.

type1inst jest skryptem Perla, wiêc musisz mieæ go zainstalowanego
je¶li chcesz u¿ywaæ type1inst. Wymagane jest równie¿ narzêdzie pfbtops
(które znajduje siê w pakiecie GNU groff).

%prep
%setup -q
%patch -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install t1embed type1inst $RPM_BUILD_ROOT%{_bindir}
install type1inst.man $RPM_BUILD_ROOT%{_mandir}/man1/type1inst.1

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
