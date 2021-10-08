#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Standard IO library for OCaml
Summary(pl.UTF-8):	Biblioteka standardowego we/wy dla OCamla
Name:		ocaml-stdio
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/stdio/releases
Source0:	https://github.com/janestreet/stdio/archive/v%{version}/stdio-%{version}.tar.gz
# Source0-md5:	ee81f65acbab0ac762181aa6ceb926b1
URL:		https://github.com/janestreet/stdio
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune-devel >= 2.0.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Stdio provides input/output functions for OCaml. It re-exports the
buffered channels of the stdlib distributed with OCaml but with some
improvements.

This package contains files needed to run bytecode executables using
stdio library.

%description -l pl.UTF-8
Stdio udostępnia funkcje wejścia/wyjścia dla OCamla. Re-eksportuje
buforowane kanały z stdlib rozprowadzanej wraz OCamlem, ale z kilkoma
usprawnieniami.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki stdio.

%package devel
Summary:	Standard IO library for OCaml - development part
Summary(pl.UTF-8):	Biblioteka standardowego we/wy dla OCamla - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ocaml-base-devel >= 0.14
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
stdio library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki stdio.

%prep
%setup -q -n stdio-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/stdio/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/stdio

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.org
%dir %{_libdir}/ocaml/stdio
%{_libdir}/ocaml/stdio/META
%{_libdir}/ocaml/stdio/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/stdio/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/stdio/*.cmi
%{_libdir}/ocaml/stdio/*.cmt
%{_libdir}/ocaml/stdio/*.cmti
%{_libdir}/ocaml/stdio/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/stdio/*.a
%{_libdir}/ocaml/stdio/*.cmx
%{_libdir}/ocaml/stdio/*.cmxa
%endif
%{_libdir}/ocaml/stdio/dune-package
%{_libdir}/ocaml/stdio/opam
