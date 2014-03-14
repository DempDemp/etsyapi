from setuptools import setup
import os

setup(
    name='etsyapi',
    version='0.2',
    description='etsy.com api wrapper',
    url='https://github.com/DempDemp/etsyapi',
    download_url = 'https://github.com/DempDemp/etsyapi/tarball/0.2',
    packages=['etsyapi'],
    keywords=['etsy', 'api', 'etsy.com'],
    license='BSD',
    maintainer='Demp',
    long_description=open(os.path.dirname(os.path.realpath(__file__)) + '/README.md').read(),
    install_requires=[
        "requests>=0.13.2",
        "requests-oauthlib>=0.4.0",
    ],
)