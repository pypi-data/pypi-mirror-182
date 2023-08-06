from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='hidemypasspls',
  version='0.0.10',
  description='Basic commands made advanced.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  author='deaphie',
  author_email='deaphopxz@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='basic', 
  packages=find_packages(),
  install_requires=['getch==1.0'] 
)