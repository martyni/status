from setuptools import setup
with open('requirements.txt') as requirements:
   setup(
      name		= 'status',
      version		= '3.8',
      packages 		= ['status'],
      package_dir	= {'': '.'},
      author		= 'askmartyn',
      description	= 'Simple service that reads json status file',
      install_requires	= [ req for req in requirements.readlines()]
   )
