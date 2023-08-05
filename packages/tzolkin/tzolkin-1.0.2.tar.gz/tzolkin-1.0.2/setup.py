from setuptools import setup
from setuptools import find_packages

setup(
    name='tzolkin',
    version='1.0.2',
    packages=find_packages(),
    scripts=['bin/tzolk'],
    license='MIT license',
    long_description=open('README.md').read(),
    include_package_data=True,
)
