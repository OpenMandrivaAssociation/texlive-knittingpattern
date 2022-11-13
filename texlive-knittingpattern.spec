Name:		texlive-knittingpattern
Version:	17205
Release:	1
Summary:	Create knitting patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/knittingpattern
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knittingpattern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knittingpattern.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The class provides a simple, effective method for knitters to
produce high-quality, attractive patterns using LaTeX. It does
this by providing commands to handle as much of the layout of
the document as possible, leaving the author free to
concentrate on the pattern.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/knittingpattern/knittingpattern.cls
%doc %{_texmfdistdir}/doc/latex/knittingpattern/README
%doc %{_texmfdistdir}/doc/latex/knittingpattern/introduction.pdf
%doc %{_texmfdistdir}/doc/latex/knittingpattern/introduction.tex
%doc %{_texmfdistdir}/doc/latex/knittingpattern/lion.png
%doc %{_texmfdistdir}/doc/latex/knittingpattern/template.pdf
%doc %{_texmfdistdir}/doc/latex/knittingpattern/template.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
