#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ 'typer', 'rich', 'numpy', 'matplotlib']

test_requirements = [ ]

setup(
    author="Bo Kern",
    author_email='kern@campus.tu-berlin.de',
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
    description="An implementation of sequence alignment on the basis of cross-correlation technique",
    install_requires=requirements,
    license="MIT license",
    long_description_content_type="text/markdown",
    long_description=readme,
    include_package_data=True,
    keywords='sequence_alignment_by_cross_correlation',
    name='sequence_alignment_by_cross_correlation',
    packages=find_packages(include=['sequence_alignment_by_cross_correlation', 'sequence_alignment_by_cross_correlation.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kuhjuice/sequence_alignment_by_cross_correlation',
    version='0.1.0',
    zip_safe=False,
    
)
