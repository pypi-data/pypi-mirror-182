import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urbitob",
    version="0.0.4",
    author="~ranren-ranlen",
    description="A python implementation of urbit-ob",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    url = "https://github.com/evening/urbit-pob",
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    install_requires=["mmh3==3.0"]
)
