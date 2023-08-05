from setuptools import setup
from setuptools import find_packages

setup(
    name='tzolkin',
    version='1.0.3',
    packages=find_packages(),
    package_data={
        'tzolkin': ['tzolkin/command.grammar'],
    },
    scripts=['bin/tzolk'],
    license='MIT license',
    long_description=open('README.md').read(),
)
