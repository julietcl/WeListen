"""WeListen website python package configuration."""

from setuptools import setup

setup(
    name='welisten',
    version='0.1.0',
    packages=['welisten'],
    include_package_data=True,
    install_requires=[
        'flask',
        'arrow',
        'sh',
    ],
)
