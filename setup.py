#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup_requirements = ['pytest-runner', 'boto3']

test_requirements = ['pytest', ]

setup(
    author="Simon McCartney",
    author_email='simon@mccartney.ie',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    description="wrapper for terraform to streamline setup & multi-environment repos",
    entry_points='''
        [console_scripts]
        tfw=tfw:cli
    ''',
    install_requires=['click', 'boto3'],
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tfw',
    name='tfw',
    packages=find_packages(include=['tfw']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/simonmcc/tfw',
    version='0.1.0',
    zip_safe=False,
)
