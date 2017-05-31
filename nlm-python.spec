Name:					 nlm-python-shared
Version:       3.4.6
Release:       1%{?dist}
Summary:       Summary goes here
Group:         Group/goes/here
License:       GPL
URL:           Not required
Vendor:        Company you work for, probably
Distribution:  Group for specific distribution

Source:        %{name}-%{version}.tgz
BuildRoot:     %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
Requires:      /bin/bash, /bin/date
BuildArch:     noarch

%description
Description of the package goes here.

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 file-in-source %{buildroot}/path/to/target/server/file-in-source

%pre
# Pre-install steps go here.

%post
# Post-install steps go here.

%preun
# Steps prior to uninstall go here.

%postun
# Steps after uninstall go here.

%clean
%{__rm} -rf %{buildroot}

%files
%doc README
%defattr(-,root,root,0755)
/list/files/here

%changelog

* Date username 
- Date format is `date +"%a %b %d %Y`. Comments go here.