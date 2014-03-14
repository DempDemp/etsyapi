from distutils.core import setup

setup(
    name='etsyapi',
    version='0.2',
    packages=['etsyapi',],
    license='BSD',
    long_description=open('README.md').read(),
    install_requires=[
        "requests >= 0.13.2",
        "requests-oauthlib >= 0.4.0",
    ],
)