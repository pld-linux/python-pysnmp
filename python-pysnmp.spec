
%define		module	pysnmp

Summary:	SNMP engine for Python
Summary(pl):	Obs³uga SNMP dla Pythona
Name:		python-%{module}
Version:	4.1.5a
Release:	1
License:	BSD-like
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/pysnmp/%{module}-%{version}.tar.gz
# Source0-md5:	7527bec317a3cf2c3d8c9cdaa28baa71
URL:		http://pysnmp.sourceforge.net/
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python-modules
Requires:	python-pyasn1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of tools required by the Structure of Management
Information (SMI v.1 & v.2) to be used in Python programming
environment. Primarily, they are SNMP engine and MIB compiler.

%description -l pl
Zestaw narzêdzi pozwalaj±cych pisaæ w Pythonie programy korzystaj±ce z
protoko³u SNMP. Zawiera procedury s³u¿±ce do zarz±dzania obiektami MIB
(Management Information Base), opisanych przez normy SMI (Structure of
Management Information) v1 i v2.

%package doc
Summary:	Documentation for Python pysnmp module
Summary(pl):	Dokumentacja do modu³u Pythona pysnmp
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
This package contains documentation files for Python pysnmp module.

%description doc -l pl
Ten pakiet zwiera dokumentacjê do modu³u Pythona pysnmp.

%package examples
Summary:	Example programs for Python pysnmp module
Summary(pl):	Programy przyk³adowe do modu³u Pythona pysnmp
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for Python pysnmp module.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy do modu³u Pythona pysnmp.

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
%{py_sitescriptdir}/%{module}/*
%attr(755,root,root) %{_bindir}/*

%files doc
%defattr(644,root,root,755)
%doc docs/*

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
