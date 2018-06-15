import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="imtfc",
    version="0.0.4",
    author="Simon J",
    description="In-Memory Time-based Function Caching for Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thatguywiththatname/imtfc",
    packages=setuptools.find_packages(exclude=["contrib", "docs", "tests", "examples"]),
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ]
)
