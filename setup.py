import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

VERSION = '0.1.01'
PACKAGE_NAME = 'pyraster'
AUTHOR = 'Bashir Kazimi'
AUTHOR_EMAIL = 'kazimibashir907@gmail.com'
URL = 'https://github.com/bashirkazimi/pyraster'

LICENSE = 'Apache License 2.0'
DESCRIPTION = 'Python tools for processing raster and vector data for deep learning applications. GDAL needs to be installed already.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
]

setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )