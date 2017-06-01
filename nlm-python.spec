%define _upvers 3.4.6

Name:					 nlm-python
Version:       %{upvers}
Release:       1%{?dist}
Summary:       A built version of Python
License:       Python Software License (PSF)
Vendor:        U.S. National Library of Medicine

Source:        Python-%{version}.tgz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
Requires:      /bin/bash, /bin/date
BuildArch:     noarch

%description
A build version of Python

%prep
%setup -q

%build
%configure
 --prefix /usr/nlm/apps/python \
 --enable-shared \
 --enable-ipv6 \
 --with-computed-gotos=yes \
 --with-system-ffi \
 --with-system-expat \
 --with-loadable-sqlite-extensions

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
