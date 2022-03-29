"""Minimal setup file for chain_evaluate."""

from setuptools import setup, find_packages

setup(
    name='chain_evaluate',
    version='0.1.0',
    license='proprietary',
    description='Module Experiment',

    author='hsasaki',
    author_email='hsasaki@softmatters.net',
    url='None.com',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    entry_points={
        "console_scripts": [
          'evaluate_nw = evaluate_all:main'
        ]
    }
)