%global tl_name picture
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.0
Release:	%{tl_revision}.1
Summary:	Dimens for picture macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/picture
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/picture.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/picture.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/picture.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
There are macro and environment arguments that expect numbers that will
internally be multiplied by \unitlength. This package extends the syntax
of these arguments, so that dimensions with calculation support may be
used for these arguments.

