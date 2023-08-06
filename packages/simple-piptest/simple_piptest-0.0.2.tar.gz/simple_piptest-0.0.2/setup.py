import setuptools

setuptools.setup(
    name="simple_piptest",
    version="0.0.2",
    author="moumoubaimifan",
    author_email="example@example.com",
    description="simple example for uploading to pypi",
    long_description="test for uploading to PyPI",
    long_description_content_type="text/markdown",
    url="https://github.com/JustDoPython/justdopython.github.io",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
