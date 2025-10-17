from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "example_module",
        ["example_module.py"]
    )
]
setup(
    ext_modules = cythonize(ext_modules)
)