# revision 17205
# category Package
# catalog-ctan /macros/latex/contrib/knittingpattern
# catalog-date 2010-03-09 13:13:30 +0100
# catalog-license lppl1.3
# catalog-version undef
Name:		texlive-knittingpattern
Version:	20100309
Release:	10
Summary:	Create knitting patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/knittingpattern
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knittingpattern.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/knittingpattern.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20100309-2
+ Revision: 752990
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20100309-1
+ Revision: 718779
- texlive-knittingpattern
- texlive-knittingpattern
- texlive-knittingpattern
- texlive-knittingpattern

