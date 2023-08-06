#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 
    'numpy',
    'frozendict'
]

test_requirements = [ ]

setup(
    author="Andrew Nam",
    author_email='andrewnam95@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A simple probabilistic modeling framework with discrete variables.",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='discrete_probabilistic_model',
    name='discrete_probabilistic_model',
    packages=find_packages(include=['discrete_probabilistic_model', 'discrete_probabilistic_model.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/andrewnam/discrete_probabilistic_model',
    version='0.1.01',
    zip_safe=False,
)
