%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name anymatch

Summary:       Matches strings against anything
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       1.3.0
Release:       2%{?dist}
License:       ISC
URL:           https://github.com/es128/anymatch
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: nodejs010-runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Matches strings against configurable strings, globs, 
regular expressions, and/or functions

Javascript module to match a string against a regular expression, 
glob, string, or function that takes the string as an argument 
and returns a truthy or falsy value. The matcher can also be 
an array of any or all of these. Useful for allowing a very 
flexible user-defined config to define things like file paths.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Wed Jan 06 2016 Tomas Hrcka <thrcka@redhat.com> - 1.3.0-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 1.3.0-1
- Initial package
