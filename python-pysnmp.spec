%include	/usr/lib/rpm/macros.python

%define		module	pysnmp

Summary:	Python SNMP Toolkit
Summary(pl):	Narz�dzia SNMP dla Pythona
Name:		python-%{module}
Version:	1.6.5
Release:	3
License:	BSD-like
Group:		Libraries/Python
Source0:	ftp://ftp.glas.net/users/ilya/tools/pysnmp/%{module}-%{version}.tar.gz
# Source0-md5:	1410ff9824f07dafe441510d9a8fc92d
URL:		http://pysnmp.sourceforge.net/
BuildRequires:	rpm-pythonprov
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a set of tools required by the Structure of Management
Information (SMI v.1 & v.2) to be used in Python programming
environment. Primarily, they are SNMP engine and MIB compiler.

%description -l pl
Zestaw narz�dzi pozwalaj�cych pisa� w Pythonie programy korzystaj�ce z
protoko�u SNMP. Zawiera procedury s�u��ce do zarz�dzania obiektami MIB
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc html README CHANGES LICENSE
%{py_sitedir}/%{module}/*py[co]
%{_examplesdir}/%{name}