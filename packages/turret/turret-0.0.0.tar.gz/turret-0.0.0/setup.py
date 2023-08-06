from setuptools import setup, find_packages
import os.path

def read(rel_path):
   here = os.path.abspath(os.path.dirname(__file__))
   with open(os.path.join(here, rel_path), 'r') as fp:
      return fp.read()

def get_version(rel_path):
   for line in read(rel_path).splitlines():
      if line.startswith('__version__'):
         delim = '"' if '"' in line else "'"
         return line.split(delim)[1]
   else:
      raise RuntimeError("Unable to find version string.")

# README.md
# with open('README.md', 'r', encoding='utf-8') as readme_file:
#     readme = readme_file.read()

setup(
   name='turret',
   packages=find_packages(),
   version=get_version('turret/__init__.py'),
   description='Turret',
   author='Nawaf Alqari',
   author_email='nawafalqari13@gmail.com',
#  keywords=['pyon', 'pyonr', 'json', 'pythonobjectnation', 'python object nation'],
#  long_description=readme,
#  long_description_content_type='text/markdown',
   project_urls={
      'Documentation': 'https://github.com/iibl/turret#readme',
      'Bug Tracker': 'https://github.com/iibl/turret/issues',
      'Source Code': 'https://github.com/iibl/turret/',
      'Discord': 'https://discord.gg/cpvynqk4XT'
   },
   license='MIT',
   url='https://github.com/iibl/turret/',
   classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
   ],
)
