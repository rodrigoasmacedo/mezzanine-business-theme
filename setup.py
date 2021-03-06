#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from business_theme import __version__ as version

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_requires = [
    'mezzanine >= 3.1',
]
    
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='mezzanine-business-theme',
    version=version,
    description="""Starter business theme for Mezzanine CMS""",
    long_description=readme,
    author='Dmitry Falk',
    author_email='dfalk5@gmail.com',
    url='https://github.com/dfalk/mezzanine-business-theme',
    packages=[
        'business_theme',
        'business_theme.templatetags',
    ],
    include_package_data=True,
    install_requires=install_requires,
    license="BSD",
    zip_safe=False,
    keywords='mezzanine business theme',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)