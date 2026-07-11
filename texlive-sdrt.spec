%global tl_name sdrt
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Macros for Segmented Discourse Representation Theory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sdrt
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sdrt.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros to produce the 'Box notation' of SDRT (and
DRT), to draw trees representing discourse relations, and finally to
have an easy access to various mathematical symbols used in that theory,
mostly with automatic mathematics mode, so they work the same in
formulae and in text.

