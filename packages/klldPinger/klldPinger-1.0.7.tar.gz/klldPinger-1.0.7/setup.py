import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name="klldPinger",
    version="1.0.7",
    author="klld",
    description="Async Tool For Uploading URL's To klldPinger",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://pinger.klld.tk/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'aiohttp'
      ],
)
