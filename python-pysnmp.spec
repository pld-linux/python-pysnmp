#
%define		module	pysnmp
#
Summary:	SNMP engine for Python
Summary(pl.UTF-8):	Obsługa SNMP dla Pythona
Name:		python-%{module}
Version:	4.1.5a
Release:	2
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pysnmp/%{module}-%{version}.tar.gz
# Source0-md5:	7527bec317a3cf2c3d8c9cdaa28baa71
URL:		http://pysnmp.sourceforge.net/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-pyasn1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of tools required by the Structure of Management
Information (SMI v.1 & v.2) to be used in Python programming
environment. Primarily, they are SNMP engine and MIB compiler.

%description -l pl.UTF-8
Zestaw narzędzi pozwalających pisać w Pythonie programy korzystające z
protokołu SNMP. Zawiera procedury służące do zarządzania obiektami MIB
(Management Information Base), opisanych przez normy SMI (Structure of
Management Information) v1 i v2.

%package doc
Summary:	Documentation for Python pysnmp module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona pysnmp
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Python pysnmp module.

%description doc -l pl.UTF-8
Ten pakiet zwiera dokumentację do modułu Pythona pysnmp.

%package examples
Summary:	Example programs for Python pysnmp module
Summary(pl.UTF-8):	Programy przykładowe do modułu Pythona pysnmp
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pysnmp module.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy do modułu Pythona pysnmp.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" '!' -path '*/v4/smi/mibs/*' | xargs rm

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install tools/libsmi2pysnmp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES TODO docs/mibs/*
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/pysnmp-*.egg-info

%files doc
%defattr(644,root,root,755)
%doc docs/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
