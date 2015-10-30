# -*- coding: utf-8 -*-
from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='ansible-docgenerator',
    version='0.1.0',
    author=u'Christo Crampton',
    install_requires=required,
    py_modules = ['docgen'],
    url='https://github.com/toast38coza/Ansible-DocGen',
    license='MIT licence',
    description='Simple tool for generating ansible role documentation',
    long_description=open('README.md').read(),
)
