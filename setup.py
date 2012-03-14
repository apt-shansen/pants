#!/usr/bin/env python

from distutils.core import setup

setup(
    name="pants",
    version="0.10.1",
    description="A lightweight framework for writing asynchronous network applications in Python.",
    author="ecdavis",
    author_email="ecdavis@wtfrak.com",
    url="http://pantsweb.org/",
    download_url="https://github.com/ecdavis/pants/tarball/pants-0.10.1",
    packages=["pants", "pants.contrib", "pants.http", "pants.util", "pants.web"],
    package_data={"pants.web": ["data/*.css", "data/*.png", "data/*.html"]},
    classifiers=[
        "Programming Language :: Python :: 2.6",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Server",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    scripts=[
        "bin/pants_dig.py",
        ],
    )
