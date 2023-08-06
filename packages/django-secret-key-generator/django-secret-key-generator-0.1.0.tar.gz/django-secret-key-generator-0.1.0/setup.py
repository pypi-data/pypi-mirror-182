from distutils.core import setup
from setuptools import find_packages

setup (
    name='django-secret-key-generator',
    version='0.1.0',
    author='Arshad Shah',
    scripts=['key_generator.py'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A secure secret key generator for django',
    long_description=open('README.md').read(),
    install_requires=[''],
    url='',
    author_email='shaharshad57@gmail.com'
)