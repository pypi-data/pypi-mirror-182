#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="simple_piptest",
    version="0.0.3",
    author="shzhang",
    author_email="zhangshunhong.pku@gmail.com",
    description="simple example for uploading to pypi",
    long_description="test for uploading to PyPI",
    long_description_content_type="text/markdown",
    url="https://github.com/to_be_posted.github.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
