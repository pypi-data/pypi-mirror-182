import codecs
import os
import sys
try:
    from setuptools import setup, find_packages, find_namespace_packages
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "BMKR"
# PACKAGES = ['BMKR']
PACKAGES = find_namespace_packages()
DESCRIPTION = "this is a test for package by myself upload to pypi"
LONG_DESCRIPTION = "this is a test for package by myself upload to pypi"
KEYWORDS = "keyword"
AUTHOR = "renjunyi"
AUTHOR_EMAIL = "2998345156@qq.com"
URL = "https://github.com/lichanghong/wenyali.git"
VERSION = "1.0.3"
LICENSE = "MIT"
setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    package_data={'':['*.txt'],'':['*.dat']},
    include_package_data=True,
    zip_safe=True,
)