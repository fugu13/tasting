import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tasting",
    version="0.0.1",
    author="Russell Duhon",
    author_email="fugu13@gmail.com",
    description="A code-driven QA reporting library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fugu13/tasting",
    packages=setuptools.find_packages(),
    install_requires=[
        "attrs"
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Framework :: Pytest"
    ],
)