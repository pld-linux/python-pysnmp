%include /usr/lib/rpm/macros.python

%define  module  pysnmp

Summary:	Python SNMP Toolkit
Summary(pl):	Narzędzia SNMP dla Pythona
Name:		python-%{module}
Version:	1.6.5
Release:	2
License:	BSD-style
Group:		Libraries/Python
Source0:	ftp://ftp.glas.net/users/ilya/tools/pysnmp/%{module}-%{version}.tar.gz
URL:		http://pysnmp.sourceforge.net/
BuildRequires:	rpm-pythonprov
%requires_eq    python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of tools required by the Structure of Management
Information (SMI v.1 & v.2) to be used in Python programming
environment. Primarily, they are SNMP engine and MIB compiler.

%description -l pl
Zestaw narzędzi pozwalających pisać w Pythonie programy korzystające z
protokołu SNMP. Zawiera procedury służące do zarządzania obiektami MIB
(Management Information Base), opisanych przez normy SMI (Structure of
Management Information) v1 i v2.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}
install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9fn README CHANGES LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html *.gz
%{py_sitedir}/%{module}/*py[co]
%{_examplesdir}/%{name}
