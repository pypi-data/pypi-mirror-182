#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages


setup(
    author="Roberto J. Homs Puron",
    author_email='rhoms@cells.es',
    license="GPLv3",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.7',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
    ],
    description="Library and Tango DS for Alba Electrometer first version",
    entry_points={
        'console_scripts': [
            'PyAlbaEM=albaem.tango.server:main',

        ]
    },
    install_requires=['pytango'],
    long_description="Library and Tango DS for Alba Electrometer first "
                     "version",
    include_package_data=True,
    keywords='alba, electrometer, beamline, albaem',
    name='albaem',
    packages=find_packages(),
    package_data={},
    python_requires='>=3.7',
    setup_requires=[],
    extras_require={},
    url='https://github.com/ALBA-Synchrotron/AlbaEm',
    version='1.1.0',
    zip_safe=True
)
