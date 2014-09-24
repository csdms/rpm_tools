# Notes

There already exists a CentOS base package called `babel`,
holding a collection of tools for internationalizing Python applications.
However,
we're planning to install the CSDMS software stack 
to the custom location **/usr/local/csdms**,
which isn't on any standard path.
This may avert a conflict.

I set the QA_RPATHS environment variable 
to get `babel` to build:

   $ export QA_RPATHS=$[ 0x0001|0x0010 ]

Fedora really [doesn't like rpaths](http://fedoraproject.org/wiki/RPath_Packaging_Draft).
However,
this is an issue that the maintainers of Babel may need to address,
so I'm allowing them.

For the Java dependency,
I used the Oracle Java SDK v1.7.0_67, 
installed in the default location.

For compatibility with CSDMS software,
Babel must be built with Python 2.7.
