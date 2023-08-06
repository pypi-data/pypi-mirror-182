import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mwbot",
    version="0.0.4",
    author="GuGuMur",
    author_email="2221533105@qq.com",
    description="为PRTS和ArcaeaCNWiki提供编辑功能的mediawiki api库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GuGuMur/mwbot",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
)