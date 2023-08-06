from setuptools import setup, find_packages
import os

VERSION = '1.0'
DESCRIPTION = "A simple example package"

# Setting up
setup(
    name="publish example",
    version=VERSION,
    author="handsome victor 666",
    author_email="handsomevictor0054@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['numpy'],  # add any additional packages that
)
