from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='simpledatatable',
  version='0.3',
  description='This package allows flet developers to easily import SQL, CSV, Excel or Json tables into flet\'s DataTable.',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='',  
  author='Stan Mathers',
  author_email='sabagamgebeli@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='table', 
  packages=find_packages(),
  install_requires=['sqlalchemy', 'pandas', 'openpyxl'] 
)