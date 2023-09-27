from setuptools import setup, find_packages

setup(
    name='piehydra',
    version='0.0.1',
    description='wrapper for hydra-thc (bruteforcing tool)',
    author='plusleft',
    packages=["piehydra"],
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
)