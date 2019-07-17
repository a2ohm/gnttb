import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gnttb-a2ohm",
    version="1",
    author="Antoine",
    author_email="antoine@2ohm.fr",
    description="A Greek New Testament toolbox",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a2ohm/gnttb",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
