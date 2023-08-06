from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Mathexs',
  version='0.0.2',
  description='More functions added',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Adem Rebahi',
  author_email='ademlp2012@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Functions, Advenced, Drawer_Shaper', 
  packages=find_packages(),
  install_requires=[''] 
)