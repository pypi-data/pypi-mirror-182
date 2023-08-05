# coding: utf-8

from setuptools import setup, find_packages
from os import path


NAME = "ucb-client"
VERSION = "22.6.12"
BASE_PATH = path.abspath(path.dirname(__file__))
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
REQUIRES = [
    "certifi>=2017.4.17",
    "python-dateutil>=2.1",
    "six>=1.10",
    "urllib3>=1.23"
]
with open(path.join(BASE_PATH, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name=NAME,
    version=VERSION,
    description="Unity Cloud Build",
    author_email="artemartsoul@gmail.com",
    url="https://github.com/Cookieees/ucb-client",
    keywords=["Swagger", "Unity Cloud Build", "UCB"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description=long_description,
)