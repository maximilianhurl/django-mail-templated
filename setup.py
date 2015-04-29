from setuptools import setup, find_packages
import os
import platform

DESCRIPTION = 'Send emails with Django template system'

LONG_DESCRIPTION = None
try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    pass

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Framework :: Django',
]

setup(
    name='max-django-mail-templated',
    version='0.2.2',
    packages=['mail_templated'],
    author='Artem Rizhov, Max hurl',
    author_email='artem.rizhov@gmail.com',
    url='https://github.com/maximilianhurl/django-mail-templated',
    license='MIT',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms=['any'],
    classifiers=CLASSIFIERS,
)
