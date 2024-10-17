Name:		texlive-tempora
Version:	39596
Release:	2
Summary:	Greek and Cyrillic to accompany Times
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tempora
License:	gpl2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tempora.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tempora.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package, derived from TemporaLGCUni by Alexej Kryukov, is
meant as a companion to Times text font packages, providing
Greek and Cyrillic in matching weights and styles. OpenType and
Type1 fonts are provided, with LaTeX support files giving
essentially complete LGR coverage of monotonic, polytonic and
ancient Greek, and almost full T2A coverage of Cyrillic.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/tempora
%{_texmfdistdir}/fonts/vf/public/tempora
%{_texmfdistdir}/fonts/type1/public/tempora
%{_texmfdistdir}/fonts/tfm/public/tempora
%{_texmfdistdir}/fonts/opentype/public/tempora
%{_texmfdistdir}/fonts/map/dvips/tempora
%{_texmfdistdir}/fonts/enc/dvips/tempora
%{_texmfdistdir}/fonts/afm/public/tempora
%doc %{_texmfdistdir}/doc/fonts/tempora

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
