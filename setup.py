#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

# This is to workaround error: Operation not permitted
# http://stackoverflow.com/questions/7719380/python-setup-py-sdist-error-operation-not-permitted

del os.link

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pyetcd', 'ply', 'click'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='etcdb',
    version='1.0.2',
    description="PEP 249 compatible driver for Etcd",
    long_description=readme + '\n\n' + history,
    author="Box TechOps Database Team",
    author_email='oss@box.com',
    url='https://github.com/box/etcdb',
    packages=find_packages(),
    package_dir={'etcdb':
                 'etcdb'},
    entry_points={
        'console_scripts': [
            'etcdb=etcdb.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='etcdb',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
