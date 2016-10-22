"""
Boehm-Berarducci encoding for some types
"""

from codecs import open
from os import path
from setuptools import find_packages
from setuptools import setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='boehmberarducci',
    version='0.0.1',
    description='Boehm-Berarducci encoding for some types',
    long_description=long_description,
    url='https://github.com/rcalsaverini/boehm-berarducci',
    author='Rafael S. Calsaverini',
    author_email='rafael.calsaverini@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='types boehm-berarducci encodings',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=[],
    setup_requires=['pytest-runner'],
    extras_require={
        'dev': ['check-manifest'],
        'test': ['pytest'],
    },
)
