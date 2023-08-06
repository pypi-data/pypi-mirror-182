import io
import os
import re
import setuptools
from setuptools import setup

scriptFolder = os.path.dirname(os.path.realpath(__file__))
os.chdir(scriptFolder)


# Find version info from module (without importing the module):

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="getfilepath",
    version="0.0.1",
    author="Balaji Santhanam",
    author_email="sribalaji2112@gmail.com",
    description="""We can use the GetFileAccess module to find out where the files are located in memory and return a file path for a given filename. We will also return a count of the given filename in memory.
This function will count how many given external files are in your memory and return it.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://sribalaji.rf.gd",
    project_urls={
        "Bug Tracker": "https://github.com/SriBalaji2112/GetFileName",
    },
    license='MIT',
    keywords="file getfilepath Get File Path filesearch file search name",
    classifiers=[
        "Programming Language :: Python :: 3",
        'Development Status :: 4 - Beta',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    package_dir={'':"getfilepath"},
    packages=find_packages("getfilepath"),
    python_requires=">=3.9",
)