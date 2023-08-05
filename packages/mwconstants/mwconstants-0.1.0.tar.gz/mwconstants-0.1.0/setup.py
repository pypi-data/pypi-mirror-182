import codecs
import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = "0.1.0"
DESCRIPTION = "Various data and utilities for processing wikitext."

# Dev dependencies
EXTRAS_REQUIRE = {
    "tests": ["pytest>=6.2.5"],
}

EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"]

# Setting up
setup(
    name="mwconstants",
    version=VERSION,
    author="geohci (Isaac Johnson)",
    author_email="<isaac@wikimedia.org>",
    url="https://gitlab.wikimedia.org/repos/research/mwconstants",
    license="MIT License",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=["requests"],
    keywords=["python", "wikitext", "wiki"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    zip_safe=False,
)
