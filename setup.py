# tcm/setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="themecampmanager",
    version="0.1.3",
    author="Chris Filkins",
    author_email="christopher.filkins@gmail.com",
    description="Camp Manager Project for Theme Camps at Burning Man",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/filchyboy/tcm",
    keywords="learning tools",
    packages=find_packages() # 
)