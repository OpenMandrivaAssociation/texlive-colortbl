%global tl_name colortbl
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0l
Release:	%{tl_revision}.1
Summary:	Add colour to LaTeX tables
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colortbl
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colortbl.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows rows and columns to be coloured, and even individual
cells.

