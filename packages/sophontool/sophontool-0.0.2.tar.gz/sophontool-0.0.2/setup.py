#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

from importlib.metadata import entry_points

setup(
    name='sophontool',
    version='0.0.2',
    author='yifei.gao, wangyang.zuo',
    author_email='yifei.gao@sophgo.com, wangyang.zuo@sophon.com',
    description='tools for sophon',
    packages=['stool'],
    entry_points={ 'console_scripts': ['stool = stool.main:main'] },
    scripts=['stool/main.py'],
    install_requires=["requests","tqdm","pycrypto"]
)
# pipzwyqwerty123