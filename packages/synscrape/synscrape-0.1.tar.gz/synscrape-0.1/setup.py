from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1'
DESCRIPTION = 'Request package'
LONG_DESCRIPTION = 'Shortcut to sending requests. This is a persionalized package'

# Setting up
setup(
    name="synscrape",
    version=VERSION,
    author="synfosec",
    author_email="<thesyndikit@proton.me>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['requests'],
    keywords=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
