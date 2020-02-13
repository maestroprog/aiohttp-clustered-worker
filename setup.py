import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='aiohttp-clustered-worker',
    version='0.1',
    author="Ruslan Yarullin",
    author_email="maestroprog@gmail.com",
    description="Clustered worker library for AIOHTTP package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/maestroprog/aiohttp-clustered-worker/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
