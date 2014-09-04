# Notes

I set two environment variables 
to get `babel` to build:

```
$ export JAVAPREFIX=/usr/lib/jvm/java-1.7.0-openjdk.x86_64
$ export QA_RPATHS=$[ 0x0001|0x0010 ]
```

It's difficult to detect Java in a cross-platform manner,
which is why I'm passing to the user the responsibility of locating
the Java install directory.
I'm using OpenJDK.

Fedora really [doesn't like rpaths](http://fedoraproject.org/wiki/RPath_Packaging_Draft).
However,
this is an issue that the maintainers of Babel may need to address,
so I'm allowing them.
