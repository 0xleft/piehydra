from setuptools import setup, find_packages

setup(
    name='pyhydra',
    version='0.0.1',
    description='wrapper for hydra-thc',
    author='plusleft',
    packages=["pyhydra"],
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
)