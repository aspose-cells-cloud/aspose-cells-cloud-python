# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "asposecellscloud"
VERSION = "22.1"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Python Cloud SDK wraps Aspose.Cells REST API so you could seamlessly integrate Microsoft Excel® spreadsheet generation, manipulation, conversion & inspection features into your own Python applications.",
    author="Aspose Cloud",
    author_email="aspose.cloud@aspose.com",
    url="https://github.com/aspose-cells-cloud/aspose-cells-cloud-python",
    keywords=["aspose", "cells", "cloud"],
    install_requires=REQUIRES,
    packages=['asposecellscloud', 'asposecellscloud.apis', 'asposecellscloud.models'],
    include_package_data=True,
    long_description="Python Cloud SDK wraps Aspose.Cells REST API so you could seamlessly integrate Microsoft Excel® spreadsheet generation, manipulation, conversion & inspection features into your own Python applications.",
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
