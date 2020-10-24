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
  description='Portage de la fonctionnalité env de JS sur python',
  py_module=["pyenv"],
  package_dir={"":'src'},
  url="https://github.com/Leer0r/pyEnv.git",
  install_requires=[
    're'
  ],
  python_requires='>=3.7',
  classifiers=[
    "Programming Language :: Python :: 3",
    "Development Status :: 4 - Beta",
    "Programming Language :: Python :: 3.7",
  ],
)