# coding: utf-8
import os
import re

from setuptools import setup, find_packages

module_file = open("refinitiv/data/__init__.py").read()
metadata = dict(re.findall(r'__([a-z]+)__\s*=\s*"([^"]+)"', module_file))

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="refinitiv-data",
    version=metadata["version"],
    description="Python package for retrieving data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://developers.refinitiv.com/en/api-catalog/refinitiv-data-platform/refinitiv-data-library-for-python",
    author="REFINITIV",
    author_email="",
    license="Apache 2.0",
    data_files=[("", ["LICENSE.md", "CHANGES.txt"])],
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests", "tests_*"]
    ),
    zip_safe=False,
    python_requires=">3.6",
    install_requires=[
        # https://pypi.org/project/appdirs/
        "appdirs>=1.4.3,<=1.4.4",
        # https://pypi.org/project/pyee/
        "pyee<=9.0.4",
        # https://pypi.org/project/httpx/
        "httpx>=0.18,<=0.23.0",
        # https://pypi.org/project/httpcore/
        "httpcore<=0.15.0",
        # https://pypi.org/project/mysql-connector-python/
        "mysql-connector-python<=8.0.31",
        # https://pypi.org/project/numpy/
        "numpy>=1.11.0,<=1.23.4",
        # https://pypi.org/project/pandas/
        "pandas>=1.3.5,<1.6.0",
        # https://pypi.org/project/python-dateutil/
        "python-dateutil<=2.8.2",
        # https://pypi.org/project/requests/
        "requests<=2.28.1",
        # https://pypi.org/project/scipy/
        "scipy<=1.9.3",
        # https://pypi.org/project/six/
        "six<=1.16.0",
        # https://pypi.org/project/tenacity/
        "tenacity>=8.0,<8.1.0",
        # https://pypi.org/project/watchdog/
        "watchdog>=0.10.2,<=2.1.9",
        # https://pypi.org/project/websocket-client/
        "websocket-client>=0.58.0,!=1.2.2,<=1.4.1",
        # https://pypi.org/project/pyhumps/
        "pyhumps~=3.0.2,<=3.8.0",
        # https://pypi.org/project/Jinja2/
        "jinja2>=3.0.3,<4.0.0",
    ],
)
