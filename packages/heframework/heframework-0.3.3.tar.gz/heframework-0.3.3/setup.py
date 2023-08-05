#!/usr/bin/env python

from distutils.core import setup

setup(name='heframework',
      version='0.3.3',
      description='本次更新：修复src不存在的严重漏洞',
      author='heStudio',
      author_email='hestudio@hestudio.org',
      url='https://gitee.com/hestudio-framework/main-windows/',
      packages=["heframework","heframework.src"],
     )

