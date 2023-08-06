#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Modulos AG",
    author_email='contact@modulos.ai',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="The databits Python package",
    entry_points={
        'console_scripts': [
            'databits=databits.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='databits',
    name='databits',
    packages=find_packages(include=['databits', 'databits.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Modulos/databits',
    version='0.1.0',
    zip_safe=False,
)
