#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File     : setup
# @Author   : LiuYan
# @Time     : 2021/4/16 10:07

import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'EcoSpace',
    version = '0.0.1',
    author = 'EcoSpace',
    author_email = 'getmail@ecospace.top',
    description = 'EcoSpace官方库',
    long_description = long_description,
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)