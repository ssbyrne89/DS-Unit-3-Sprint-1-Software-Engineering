# setup.py file

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="DS-3-1", # the name that you will install via pip
    version="1.0.1",
    author="Sean",
    author_email="your@email.com",
    description="created for practice",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/ssbyrne89/DS-Unit-3-Sprint-1-Software-Engineering",
    #keywords="",
    packages=['APP'] # ["my_lambdata"]
)