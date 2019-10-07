import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datamaker-test-v1-alexbroley",
    version="0.0.1",
    author="Alex Broley",
    author_email="alex.broley@gmail.com",
    description="A package for generating random tabluar datasets. Designed to output to SQL, CSV or JSON.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tekkabroley/DataGenerator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
