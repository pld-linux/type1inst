Summary:	Type 1 font install utility
Name:		type1inst
Version:	0.6.1
Release:	3
Copyright:	GPL
Group:		Utilities/Font
Source:		ftp://sunsite.unc.edu/pub/Linux/X11/xutils/%{name}-%{version}.tar.gz
URL:		http://goblet.anu.edu.au/~m9305357/type1inst.html
Requires:	groff
BuildArch:	noarch
BuildRoot:	/tmp/%{name}-%{version}-root

%description
type1inst is a utility which scans Type 1 PostScript font files and
generates automatically the fonts.scale file which the X Window System uses
to pick up fonts in the current directory and/or the Fontmap file which
Ghostscript uses to map file names to font names. It can also generate
simple font sample sheets which show what your fonts look like.

type1inst is a Perl script so you will need to have that  installed on your
system. The pfbtops utility (which comes as part of GNU groff) is also
required.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install t1embed type1inst $RPM_BUILD_ROOT/usr/bin
install type1inst.man $RPM_BUILD_ROOT/usr/man/man1/type1inst.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /usr/bin/*
/usr/man/man1/*

%changelog
* Sun Sep  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.6.1-3]
- fixed %attr for %doc.

* Wed May  6 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.6.1-2]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added -q %setup parameter,
- added using %%{name} macro in Buildroot and Source field,

* Fri Apr 10 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
- chaned summary,
- removed COPING from %doc (copyright stantment is in Copyright field),
- Buildroot changed to /tmp/type1inst-%%{PACKAGE_VERSION}-root,
- added URL field,
- added %%{PACKAGE_VERSION} to Source url,
- replaced "mkdir -p" with "install -d" in %install,
- added %attr macros in %files (allows building package from
  non-root account).

* Mon Dec 29 1997 Joel Young <jyoung@erols.com>
- rebuilt with version 0.6

* Tue Dec 12 1997 Peter Soos <sp@osb.hu>
- Moved to noarc architecture
- Now we use BuildRoot
