# Notes on building Babel

There already exists a CentOS base package called `babel`,
holding a collection of tools for internationalizing Python applications.
However,
since we're planning to install the CSDMS software stack 
to the custom location **/usr/local/csdms**,
which isn't on any standard path,
a conflict may be averted.

I set the QA_RPATHS environment variable (a bitmask) 
to get `babel` to build:
```
$ export QA_RPATHS=19 # 10 + 01 + 02
```
Fedora [really doesn't like rpaths](http://fedoraproject.org/wiki/RPath_Packaging_Draft).
However,
this is an issue that the maintainers of Babel may need to address,
so I'm allowing them.

For the Java dependency,
I used the Oracle Java SDK v1.7.0_67, 
installed in the default location, 
**/usr/java/default**.

For compatibility with CSDMS software,
Babel must be built with Python 2.7,
which I've installed in
**/usr/local/**
to avoid conflicting with Python 2.6.6,
which is required on my CentOS 6.4 build machine.

GCC supplied the C, C++, F77 and F90 compilers.
