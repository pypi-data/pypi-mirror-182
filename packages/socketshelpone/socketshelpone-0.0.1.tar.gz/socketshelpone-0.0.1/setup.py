from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'socketshelpone'
LONG_DESCRIPTION = 'A package to perform yup balle arithmetic operations'

# Setting up
setup(
    name="socketshelpone",
    version=VERSION,
    author="samADI",
    author_email="adityaharikumar3@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['socketshelpone', 'samADI', 'adi', 'python tutorial'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)