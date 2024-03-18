
from setuptools import setup, find_packages

setup(
    name='dataprocprofiler',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    description='A Python package for profiling and visualizing data processing performance.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourgithub/dataprocprofiler',
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
    ],
