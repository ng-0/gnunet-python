#!/bin/env/python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="gnunet",
    version="0.0",

    packages=['gnunet'],
    install_requires=['dbus-python'],
    # We require PyGObject (pygobject) but would have to
    # pass a URL to pip3 for that, as it is not on pypi.

    # Maybe this should just be GNUnet eV.
    author="ng0",
    author_email="ng0@gnunet.org",
    description="Python bindings for GNUnet",
    license="GNU GPLv3+",
    keywords="GNUnet binding p2p",
    url="https://gnunet.org",
    long_description="""GNUnet is an alternative network stack for building secure, decentralized and privacy-preserving distributed applications. Our goal is to replace the old insecure Internet protocol stack. Starting from an application for secure publication of files, it has grown to include all kinds of basic protocol components and applications towards the creation of a GNU internet.

GNUnet is an official GNU package.

This Python module provides Python bindings to GNUnet.""",

    classifiers=['Development Status :: 3 - Alpha',
                 'Intended Audience :: Developers',
		 'License :: OSI Approved :: GNU General Public License (GPL)',
		 'Operating System :: OS Independent',
		 'Operating System :: MacOS :: MacOS X',
		 'Operating System :: Microsoft :: Windows',
		 'Operating System :: POSIX'],

    platforms=['windows', 'Linux', 'MacOS X', 'Solaris', 'FreeBSD'],

)
