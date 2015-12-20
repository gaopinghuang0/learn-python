#!/usr/bin/python

# This script compiles our extension into the build/lib.* subdirectory
# run it:
# python setup.py build
# then:
# python setup.py install

from distutils.core import setup, Extension

MOD = 'Extest'
setup(name=MOD, ext_modules=[Extension(MOD, sources=['Extest2.c'])])