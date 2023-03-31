Name:		texlive-picture
Version:	54867
Release:	2
Summary:	Dimens for picture macros
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/picture
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/picture.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/picture.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/picture.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
There are macro and environment arguments that expect numbers
that will internally be multiplied by \unitlength. This package
extends the syntax of these arguments, so that dimensions with
calculation support may be used for these arguments.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/picture
%{_texmfdistdir}/tex/latex/picture
%doc %{_texmfdistdir}/doc/latex/picture

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
