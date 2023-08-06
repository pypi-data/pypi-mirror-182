from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.5'
DESCRIPTION = 'Text to binary'
LONG_DESCRIPTION = 'Converts ASCII text to binary with ease'

# Setting up
setup(
    name="synfinary",
    version=VERSION,
    author="synfosec",
    author_email="<NULLNULLNULL@NULL.NULL>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
