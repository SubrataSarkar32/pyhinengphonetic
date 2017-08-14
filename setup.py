#!/usr/bin/env python

try:
    from setuptools import setup

    from pyhinengphonetic import __version__

    setup(name='pyhinengphonetic',
          version=__version__,
          description='Python implementation to convert hindi to phonetic',
          long_description=open('README.rst', 'rt').read(),
          author='Subrata Sarkar',
          author_email='subrotosarkar32@gmail.com',
          url='https://bitbucket.org/SubrataSarkar32/pyhinengphonetic/',
          packages=['pyhinengphonetic','pyhinengphonetic.utils'],
          package_data = {'pyhinengphonetic': ['*.rst', 'resources/*.json','utils/resources/*.json']},
          include_package_data = True,
          install_requires=["simplejson >= 3.0.0",'pyttsx >=1.1'],
          license='GNU GPL v3 or later',
          zip_safe=True,
          classifiers=[
            'Development Status :: 3 - Alpha',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 2.5',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            ]
          )

except ImportError:
    print 'Install setuptools'
