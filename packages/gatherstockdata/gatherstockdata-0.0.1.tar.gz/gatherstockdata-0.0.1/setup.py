from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


# Setting up
setup(
    author="Lucas Rimfrost",
    author_email="lucas.rimfrost@gmail.com",
    name="gatherstockdata",
    version="0.0.1",
    description="Gather Stock data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pandas', 'mplfinance', 'requests', 'bs4'],
    py_modules=['gatherstockdata'],
    package_dir={'': 'src'},
    classifiers=[
            "Programming Language :: Python :: 3.9",
            "Programming Language :: Python :: 3.10",
            "Programming Language :: Python :: 3.11",
            "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
            "Operating System :: OS Independent",
    ],
    extras_require={
        'dev': [
            "pytest>=3.7",
        ],
    },
)
