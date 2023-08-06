from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='keyclock_dhruvanshu1775',
  version='0.0.2',
  description='A very basic app',
  long_description=open('README.txt').read(),
  url='',  
  author='dhruv p',
  author_email='dhruvanshu.p@latitudetechnolabs.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='mykeyclock', 
  packages=find_packages(),
  install_requires=[''] 
)