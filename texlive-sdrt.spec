Name:		texlive-sdrt
Version:	15878
Release:	2
Summary:	Macros for Segmented Discourse Representation Theory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sdrt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides macros to produce the 'Box notation' of
SDRT (and DRT), to draw trees representing discourse relations,
and finally to have an easy access to various mathematical
symbols used in that theory, mostly with automatic mathematics
mode, so they work the same in formulae and in text.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sdrt/sdrt.sty
%doc %{_texmfdistdir}/doc/latex/sdrt/README
%doc %{_texmfdistdir}/doc/latex/sdrt/sdrt-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sdrt/sdrt-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
