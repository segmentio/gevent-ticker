from setuptools import setup
import os

setup(
    name = 'gevent_ticker',
    version = '0.0.1',
    packages=[
        'gevent_ticker'
    ],
    install_requires=[
        'gevent_timer>=0.1.0,<1.2.0'
    ]
)
