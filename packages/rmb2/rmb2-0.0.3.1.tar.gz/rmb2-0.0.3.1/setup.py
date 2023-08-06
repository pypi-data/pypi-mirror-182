# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages

with open("README.rst", "r", encoding='utf-8') as f:
  long_description = f.read()

setup(name='rmb2',  # 包名
      version='0.0.3.1',  # 版本号
      description='rmb is a Python RMB translation library',
      long_description=long_description,
      author='PyDa5',
      author_email='1174446068@qq.com',
      install_requires=[],
      packages=find_packages(),
      )