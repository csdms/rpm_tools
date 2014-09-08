# Note

The file **dependencies.txt** lists the minimum set of packages 
needed to build an RPM of a CSDMS tool
on a RHEL-based Linux distribution (e.g., Fedora, CentOS).
Packages required for a specific tool
are listed in a file of the same name
in the model's directory
(e.g., **babel/dependencies.txt**).

The file **dependencies_debian.txt** lists _all_ packages 
required for Debian-based distributions (e.g., Ubuntu).
This list is primarily used for integration testing
with [Travis CI](https://travis-ci.com/).

The file **macros.cmake**,
containing the definition of the `%cmake` macro
used by `rpmbuild`,
is provided here because
it's not included in the CMake package
on the Ubuntu 12.04 LTS virtual machine
used by Travis CI.
