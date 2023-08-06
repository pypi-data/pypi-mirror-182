#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='nonebot_plugin_face2cartoonpic',
    version='0.0.2',
    author='ANGJustinl',
    author_email='angjustin@163.com',
    url='https://github.com/ANGJustinl/nonebot_plugin_face2cartoonpic',
    description=u'基于腾讯云合成图的以图绘图',
    packages=['nonebot_plugin_face2cartoonpic'],
    install_requires=['nonebot','pydantic','hmac','requests','urlextract'],
    entry_points={
        'console_scripts': [
            'get_pic=nonebot_plugin_face2cartoonpic:get_pic'
        ]
    }
)