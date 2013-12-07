# revision 29803
# category Package
# catalog-ctan /macros/latex/contrib/colortbl
# catalog-date 2012-02-14 10:56:36 +0100
# catalog-license lppl
# catalog-version v1.0a
Name:		texlive-colortbl
Version:	v1.0a
Release:	3
Summary:	Add colour to LaTeX tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colortbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows rows and columns to be coloured, and even
individual cells.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/colortbl/colortbl.sty
%doc %{_texmfdistdir}/doc/latex/colortbl/README
%doc %{_texmfdistdir}/doc/latex/colortbl/colortbl-DE.pdf
%doc %{_texmfdistdir}/doc/latex/colortbl/colortbl-DE.tex
%doc %{_texmfdistdir}/doc/latex/colortbl/colortbl.pdf
#- source
%doc %{_texmfdistdir}/source/latex/colortbl/colortbl.dtx
%doc %{_texmfdistdir}/source/latex/colortbl/colortbl.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
