from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="stardate-goddard",
    version="0.0.1",
    author="Ryein Goddard",
    author_email="ryein@live.com",
    description="Converts date time strings into Star Trek TNG star dates.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Goddard/stardate",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
)
