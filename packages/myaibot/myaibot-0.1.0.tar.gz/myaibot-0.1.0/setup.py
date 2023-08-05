"""
setup.py - A script for building and distributing the myaibot package.
@author: Hamid Ali Syed
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='myaibot',  # the name of your package
    version='0.1.0',  # the version of your package
    description='A myaibot using the OpenAI GPT-3 model',  # a short description of your package
    author='Hamid Ali Syed',  # the author of your package
    author_email='hamidsyed37@gmail.com',  # the author's email address
    url="https://github.com/syedhamidali/myaibot",
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    install_requires=['openai'],  # any dependencies your package requires
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
    'console_scripts': [
        'myaibot=myaibot:main'
        ]
    }
)
