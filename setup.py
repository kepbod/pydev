#!/usr/bin/env python3

from setuptools import setup, find_packages
from pydev.version import __version__


setup(name='pydev',
      version=__version__,
      description='Test python development environment',
      author='Xiao-Ou Zhang',
      author_email='kepbod@gmail.com',
      url='https://github.com/kepbod/pydev',
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ],
      keywords='development',
      packages=find_packages(),
      install_requires=[
          'pybedtools',
      ],
      )
