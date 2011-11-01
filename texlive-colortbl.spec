Name:		texlive-colortbl
Version:	v0.1
Release:	1
Summary:	Add colour to LaTeX tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colortbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Allows rows and columns to be coloured, and even individual
cells.

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
%{_texmfdistdir}/tex/latex/colortbl/colortbl.sty
%doc %{_texmfdistdir}/doc/latex/colortbl/README
%doc %{_texmfdistdir}/doc/latex/colortbl/colortbl-de.pdf
%doc %{_texmfdistdir}/doc/latex/colortbl/colortbl-de.tex
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
