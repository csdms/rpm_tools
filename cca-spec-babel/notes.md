# Notes on building cca-spec-babel

I set the QA_RPATHS environment variable (a bitmask) 
to get `cca-spec-babel` to build:
```
$ export QA_RPATHS=19 # 10 + 01 + 02
```
Fedora [really doesn't like rpaths](http://fedoraproject.org/wiki/RPath_Packaging_Draft).
However,
this is an issue that the maintainers may need to address,
so I'm allowing them.

For compatibility with CSDMS software,
cca-spec-babel must be built with Python 2.7,
which I've installed in
**/usr/local/**
to avoid conflicting with Python 2.6.6,
which is required on my CentOS 6.4 build machine.

GCC supplies the C, C++, F77 and F90 compilers.
