Name:		texlive-colortbl
Version:	64015
Release:	2
Summary:	Add colour to LaTeX tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colortbl
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/colortbl
%doc %{_texmfdistdir}/doc/latex/colortbl
#- source
%doc %{_texmfdistdir}/source/latex/colortbl

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
