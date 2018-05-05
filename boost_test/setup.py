from distutils.core import setup
from distutils.extension import Extension

ext_instance = Extension(
    'hello',
    sources=['hello.cpp'],
    libraries=['boost_python-py27'],
)

setup(
    name='hello-world',
    version='0.1',
    ext_modules=[ext_instance])