import os, sys
import pybind11
from pybind11 import get_cmake_dir
from pybind11.setup_helpers import Pybind11Extension, build_ext

from distutils.core import setup, Extension
from distutils import sysconfig
__version__ = '0.0.2'
# cpp_args = ['-std=c++11', '-stdlib=libc++', '-mmacosx-version-min=10.7']

ext_modules = [
    Extension(
    'testing202212',
        ['src/funcs.cpp', 'src/wrap.cpp'],
        include_dirs=[pybind11.get_include()],
    language='c++',
    # extra_compile_args = cpp_args,
    define_macros = [('VERSION_INFO', __version__)]
    ),
]

setup(
    name='testing202212',
    version=__version__,
    author='smi',
    author_email='smi@miryusupov.com',
    url="",
    description='testing 2022_',
    long_description="",
    ext_modules=ext_modules,
)