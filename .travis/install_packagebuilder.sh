#! /bin/bash
svn export https://github.com/csdms/packagebuilder/trunk packagebuilder
cd packagebuilder
python setup.py install
