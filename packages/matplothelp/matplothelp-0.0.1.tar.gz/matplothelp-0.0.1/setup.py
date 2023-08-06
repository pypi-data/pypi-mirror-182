from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'matplothelp'
LONG_DESCRIPTION = 'A package to perform yup balle arithmetic operations'

# Setting up
setup(
    name="matplothelp",
    version=VERSION,
    author="samADI",
    author_email="adityaharikumar3@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['matplothelp', 'samADI', 'adi', 'python tutorial'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)