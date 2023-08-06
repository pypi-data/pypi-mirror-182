from distutils.core import setup
from setuptools import find_packages

with open('README.md') as f:
    readme = f.read()

setup (
    name='django-secret-key-generator',
    version='0.3.0',
    author='Arshad Shah',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A secure secret key generator for django',
    long_description=readme,
    long_description_content_type='text/markdown',
    install_requires=[''],
    url='https://github.com/arshad-shah/django_key',
    author_email='shaharshad57@gmail.com'
)