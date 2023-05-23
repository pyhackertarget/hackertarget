#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(name='hackertarget',
      version='2.0',
      description='Hacker Target',
      url='https://github.com/ismailtasdelen/hackertarget',
      author='İSMAİL TAŞDELEN',
      author_email='pentestdatabase@gmail.com',
      license='MIT',
      packages=['source'],
      install_requires=['requests==2.31.0'],
      python_requires=">=3",
      zip_safe=False)
