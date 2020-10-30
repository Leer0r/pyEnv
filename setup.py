from setuptools import setup, find_packages
from readme_renderer.markdown import render

long_description = ""
with open('README.md', encoding='utf-8') as file:
  long_description = file.read()

setup(
  name = "pyenv",
  version = "0.1.0",
  author="Leer0r",
  author_email="avedd72@gmail.com",
  license='MIT',
  description='Adaptation of the js module environ in python',
  url="https://github.com/Leer0r/pyEnv.git",
  download_url = 'https://github.com/Leer0r/pyEnv/archive/v_01.tar.gz',
  install_requires=[
    're',
    'os'
  ],
  python_requires='>=3.6',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3.6',
    "Programming Language :: Python :: 3.7",
    'Programming Language :: Python :: 3.8',
  ],
)