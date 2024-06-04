from setuptools import setup, find_packages

setup (
    name='javton',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    description='A simple library to integrate JavaScript interpreter with Python',
    author='mehranalam',
    author_email='mehraxxn@gmail.com',
    url='https://github.com/mehranalam/javton'
)