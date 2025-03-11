#
%define		module	pysnmp
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module
#
Summary:	SNMP engine for Python
Summary(pl.UTF-8):	Obsługa SNMP dla Pythona
Name:		python-%{module}
Version:	4.2.5
Release:	14
License:	BSD-like
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/pysnmp/pysnmp-%{version}.tar.gz
# Source0-md5:	1f75d3e392a050e84348904fc1be3212
URL:		http://pysnmp.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:2.3
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
Requires:	python-Crypto
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

%package -n python3-%{module}
Summary:	SNMP engine for Python
Summary(pl.UTF-8):	Obsługa SNMP dla Pythona
Group:		Libraries/Python

%description -n python3-%{module}
This is a set of tools required by the Structure of Management
Information (SMI v.1 & v.2) to be used in Python programming
environment. Primarily, they are SNMP engine and MIB compiler.

%description -n python3-%{module} -l pl.UTF-8
Zestaw narzędzi pozwalających pisać w Pythonie programy korzystające z
protokołu SNMP. Zawiera procedury służące do zarządzania obiektami MIB
(Management Information Base), opisanych przez normy SMI (Structure of
Management Information) v1 i v2.

%package doc
Summary:	Documentation for Python pysnmp module
Summary(pl.UTF-8):	Dokumentacja do modułu Pythona pysnmp
Group:		Libraries/Python

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

%package -n python3-%{module}-examples
Summary:	Example programs for Python pysnmp module
Summary(pl.UTF-8):	Programy przykładowe do modułu Pythona pysnmp
Group:		Libraries/Python
Requires:	python3-%{module} = %{version}-%{release}

%description -n python3-%{module}-examples
This package contains example programs for Python pysnmp module.

%description -n python3-%{module}-examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy do modułu Pythona pysnmp.

%prep
%setup -q -n %{module}-%{version}

%{__sed} -i -e '1s,/usr/bin/env python,%{__python},' \
	tools/libsmi2pysnmp

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}}

%if %{with python2}
%py_install

find $RPM_BUILD_ROOT%{py_sitescriptdir} -type f -name "*.py" '!' -path '*/v4/smi/mibs/*' | xargs rm

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%py3_install

cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/python3-%{module}-%{version}
%endif

install tools/libsmi2pysnmp $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README CHANGES TODO docs/mibs/*
%attr(755,root,root) %{_bindir}/*
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/pysnmp-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README CHANGES TODO docs/mibs/*
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/pysnmp-*.egg-info
%endif

%files doc
%defattr(644,root,root,755)
%doc docs/*

%if %{with python2}
%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
%endif

%if %{with python3}
%files -n python3-%{module}-examples
%defattr(644,root,root,755)
%{_examplesdir}/python3-%{module}-%{version}
%endif
