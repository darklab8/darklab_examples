from setuptools import setup, Extension
from cffi import FFI
module1 = Extension(
    'demo',
    sources=['fizz_c/demo.c']
)
setup(
    name='PackageName',
    version='1.0',
    description='This is a demo package',
    ext_modules=[module1]
)
