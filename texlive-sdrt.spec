# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sdrt
# catalog-date 2009-07-05 17:22:22 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-sdrt
Version:	1.0
Release:	7
Summary:	Macros for Segmented Discourse Representation Theory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sdrt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 755833
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 719495
- texlive-sdrt
- texlive-sdrt
- texlive-sdrt
- texlive-sdrt

