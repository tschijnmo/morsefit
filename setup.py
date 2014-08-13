#!/usr/bin/env python

from distutils.core import setup

setup(
        name='morsefit',
        version='0.1',
        description='Fit ab-initio PES to Morse potential',
        author='Tschijnmo TSCHAU',
        author_email='tschijnmotschau@gmail.com',
        url='https://github.com/tschijnmo/morsefit',
        packages=['morsefit'],
        scripts=['scripts/morsefit', 'scripts/readPES']
        )

