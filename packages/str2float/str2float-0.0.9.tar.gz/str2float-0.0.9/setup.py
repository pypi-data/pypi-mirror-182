import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="str2float",
    version="0.0.9",
    author="Hoang Yell",
    author_email="hoangyell@yellorn.com",
    description="Convert float string (decimal point or decimal comma) to float",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Yellorn/str2float",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
