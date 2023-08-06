from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='simpledatatable',
  version='0.1',
  description='This package allows flet developers to easily import SQL, CSV, Excel or Json tables into flet\'s DataTable.',
  url='',  
  author='Stan Mathers',
  author_email='sabagamgebeli@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='table', 
  packages=find_packages(),
  install_requires=['sqlalchemy', 'pandas', 'openpyxl'] 
)