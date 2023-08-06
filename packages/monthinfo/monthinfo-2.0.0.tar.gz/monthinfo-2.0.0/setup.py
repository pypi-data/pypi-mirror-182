# create setup.py for package

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="monthinfo",
    version="2.0.0",
    author="Marco Ostaska",
    author_email="marcoan@ymail.com",
    description="A collection of utility functions for working with a given month",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_github_username/monthinfo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
