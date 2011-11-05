# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/colortbl
# catalog-date 2009-09-27 09:39:14 +0200
# catalog-license lppl
# catalog-version v0.1
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
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
