#! /usr/bin/python
#
# See README for usage instructions.

# We must use setuptools, not distutils, because we need to use the
# namespace_packages option for the "google" package.
#from ez_setup import use_setuptools
#use_setuptools()

from setuptools import setup, Extension
#from distutils.spawn import find_executable
import sys
import os
#import subprocess

setup(
    ext_modules=[Extension('podpb',
sources=['podpb.c','addressbook.pb.cc'], libraries=['protobuf'])],
    )

