import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="consolekit2",
    version=0.01,
    author="darkdarcool30",
    author_email="dr2009544@moreland.org",
    description="For all of your console needs!",
    long_description="Long description coming soon!!",
    long_description_content_type="text/markdown",
    url="https://github.com/darkdarcool/Console",
    packages=["consolekit2"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
