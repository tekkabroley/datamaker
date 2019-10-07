import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datamaker-test-v1-alexbroley",
    version="0.0.1",
    author="Alex Broley",
    author_email="alex.broley@gmail.com",
    description="A package for generating tabluar datasets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tekkabroley/datamaker_pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
