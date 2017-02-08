#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from thumbor_text_filter import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'colorama',
    'preggy',
    'ipdb',
    'coveralls',
    'numpy',
]

setup(
    name='thumbor_text_filter',
    version=__version__,
    description='Text filter for thumbor.',
    long_description='''
Text filter for thumbor.
''',
    keywords='thumbor filter',
    author='Wongnai.com',
    author_email='tanapoln@wongnai.com',
    url='',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pillow',
    ],
    extras_require={
        'tests': tests_require,
    }
)