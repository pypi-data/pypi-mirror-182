from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='keyclock_test_phase1',
  version='0.0.2',
  description='A very basic Login Authentication',
  long_description=open('README.txt').read(),
  url='',  
  author='jap dave',
  author_email='japdave1515@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='mykeyclock', 
  packages=find_packages(),
  install_requires=['requests'] 
)