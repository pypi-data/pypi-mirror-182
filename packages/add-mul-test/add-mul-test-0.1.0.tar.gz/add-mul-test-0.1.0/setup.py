from setuptools import setup, find_packages

# To use consistent encoding

from codecs import open
from os import path

# Directory containing this file

HERE = path.abspath(path.dirname(__file__))

# This call to setup() does all the work
setup(
    name="add-mul-test",
    version="0.1.0",
    description="Demo library",
    long_description=None,
    author="saramcts",
    author_email=None,
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["add_mul"],
    include_package_data=True,
    install_requires=["numpy"]
)


