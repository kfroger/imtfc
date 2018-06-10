from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="imtfc",
    version="0.0.1",
    description="In-Memory Time-based Function Caching for Python 3 ",
    long_description=long_description,
    url="https://github.com/thatguywiththatname/imtfc",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    keywords="in-memory cache caching time-based",
    packages=find_packages(exclude=["contrib", "docs", "tests", "examples"])
)
