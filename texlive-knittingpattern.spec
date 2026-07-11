%global tl_name knittingpattern
%global tl_revision 17205

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Create knitting patterns
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/knittingpattern
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knittingpattern.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/knittingpattern.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The class provides a simple, effective method for knitters to produce
high-quality, attractive patterns using LaTeX. It does this by providing
commands to handle as much of the layout of the document as possible,
leaving the author free to concentrate on the pattern.

