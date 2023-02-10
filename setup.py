from setuptools import setup
from pygarth.__version__ import __version__


requirements = [
    # package requirements go here
]

setup(
    name="PyGARTH",
    version=__version__,
    description="Automatic regression testing harness in Python.",
    license="MIT",
    author="Ryan Christensen",
    author_email="ryan.john.christensen12@gmail.com",
    url="https://github.com/ChristensenCode/PyGARTH ",
    packages=["pygarth"],
    entry_points={"console_scripts": ["pygarth=pygarth.cli:cli"]},
    install_requires=requirements,
    keywords="pygarth",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
