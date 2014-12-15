#!/usr/bin/env python

from os.path import exists
from setuptools import setup

setup(name='into',
      version='0.1.0',
      description='Data migration utilities',
      url='http://github.com/ContinuumIO/into/',
      author='Matthew Rocklin',
      author_email='mrocklin@continuum.io',
      license='BSD',
      keywords='into data conversion hdf5 sql',
      packages=['into'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)
