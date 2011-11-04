# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sdrt
# catalog-date 2009-07-05 17:22:22 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-sdrt
Version:	1.0
Release:	1
Summary:	Macros for Segmented Discourse Representation Theory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sdrt
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package provides macros to produce the 'Box notation' of
SDRT (and DRT), to draw trees representing discourse relations,
and finally to have an easy access to various mathematical
symbols used in that theory, mostly with automatic mathematics
mode, so they work the same in formulae and in text.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sdrt/sdrt.sty
%doc %{_texmfdistdir}/doc/latex/sdrt/README
%doc %{_texmfdistdir}/doc/latex/sdrt/sdrt-doc.pdf
%doc %{_texmfdistdir}/doc/latex/sdrt/sdrt-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
