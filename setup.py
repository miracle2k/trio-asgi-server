#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys

from setuptools import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


def get_long_description():
    """
    Return the README.
    """
    return open('README.md', 'r').read()


def get_packages(package):
    """
    Return root package and all sub-packages.
    """
    return [dirpath
            for dirpath, dirnames, filenames in os.walk(package)
            if os.path.exists(os.path.join(dirpath, '__init__.py'))]


setup(
    name='trio-asgi-server',
    version=get_version('trio_asgi'),
    url='https://github.com/miracle2k/trio-asgi-server',
    license='BSD',
    description='A trio-based ASGI server.',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    author='Michael Elsdoerfer',
    author_email='michael@elsdoerfer.com',
    packages=get_packages('trio_asgi'),
    install_requires=[
        'click',
        'trio-protocol',
        'uvicorn',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    # entry_points="""
    # [console_scripts]
    # uvicorn=uvicorn.main:main
    # """
)
