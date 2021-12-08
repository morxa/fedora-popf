%global commit a503867851ab991e943852c2c8ab2076b8553cff
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           popf
Version:        2011
Release:        %autorelease -s %{shortcommit}
Summary:        The POPF PDDL planner

License:        GPLv2+
URL:            https://nms.kcl.ac.uk/planning/software/popf.html
Source0:        https://github.com/aldukeman/popf2/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

Patch0:         popf.iterator-type-traits.patch
Patch1:         popf.vector-init.patch

BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  coin-or-Clp-devel
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gsl-devel

%description
POPF is forwards-chaining temporal planner. Its name derives from the fact that
it incorporates ideas from partial-order planning — during search, when
applying an action to a state, it seeks to introduce only the ordering
constraints needed to resolve threats, rather than insisting the new action
occurs after all of those already in the plan. Its implementation is built on
that for the planner COLIN, and it retains the ability to handle domains with
linear continuous numeric effects.

%prep
%autosetup -p1 -n popf2-%{commit}

%build
%cmake src
%cmake_build

%install
install -p -D %{_vpath_builddir}/popf2/popf3-clp %{buildroot}/%{_bindir}/popf


%files
%{_bindir}/popf
%doc README.md



%changelog
%autochangelog
