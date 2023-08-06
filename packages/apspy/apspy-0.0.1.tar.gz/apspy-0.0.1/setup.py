from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = "fetching crypto's data"

# Setting up
setup(
    name="apspy",
    version=VERSION,
    author="itsAP16",
    author_email="alexspiridigliozzi@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)