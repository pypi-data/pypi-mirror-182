#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from codecs import open
from os import path
import re

# Get the long description from the README file
with open(path.join('README.rst'), encoding='utf-8') as f:
    long_description = f.read()


def load_version():
    version_file = "pywallet_lts/_version.py"
    version_line = open(version_file).read().rstrip()
    vre = re.compile(r'__version__ = "([^"]+)"')
    matches = vre.findall(version_line)

    if matches and len(matches) > 0:
        return matches[0]
    else:
        raise RuntimeError(
            "Cannot find version string in {version_file}.".format(
                version_file=version_file))


version = load_version()

setup(
    name='pywallet_lts',
    version=version,
    description="Simple BIP32 (HD) wallet creation for BTC, BTG, BCH, LTC, DASH, USDT, QTUM and DOGE",
    long_description=long_description,
    author='Lts',
    author_email='nail.velichko2016@yandex.ru',
    license='MIT License',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",

        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.10",
    ],
    platforms=['any'],
    keywords='bitcoin, wallet, litecoin, hd-wallet, dogecoin, dashcoin, python',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'demo', 'demos', 'examples']),
    package_data={'': ['AUTHORS', 'LICENSE']},
    install_requires=[
        'base58>=2.1.1',
        'ecdsa>=0.18.0',
        'six>=1.16.0',
        'crypto-crypto-two1>=0.0.3',
        'pycryptodome>=3.16.0',
    ]
)
