from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='InvoiceGen',
  version='0.0.1',
  description='A Very Powerfull free PDF Invoice Gen',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Khushal Jethava',
  author_email='Khushaljethava14@outlook.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Invoice Generator', 
  packages=find_packages(),
  install_requires=[''] 
)