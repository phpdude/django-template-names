#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='django-template-names',
    version=".".join(map(str, __import__("template_names").__version__)),
    description='Django templates names list automatic helper',
    author='Alexandr I. Shurigin',
    author_email='ya@helldude.ru',
    maintainer='Alexandr I. Shurigin',
    maintainer_email='ya@helldude.ru',
    url='https://github.com/phpdude/django-template-names',
    packages=find_packages(),
    classifiers=[
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ]
)
