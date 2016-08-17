"""
SRU_utils
SRU Package
-----------
python SRU_utils
Link
`````
* Source
  https://github.com/ben-garside/
"""
from distutils.core import setup

version = "0.1.1"

setup(
    name="sru_utils",
    version=version,
    author="Benjamin Garside",
    author_email="abgarside<at>gmail<dot>com",
    packages=[
        "sru_utils",
        "sru_utils.routes",
        "sru_utils.conf",
        "sru_utils.helpers",
        "sru_utils.controllers"
        ],
    include_package_data=True,
    url="http://github.com/ben-garside/sru_utils/dist/{}/".format(version),

    # license="LICENSE.txt",
    description="utils SRU package",
    # long_description=open("README.md").read(),
    # Dependent packages (distributions)
    dependency_links=[
        "git+https://github.com/ben-garside/utils_shim"
    ],
    install_requires=[
        "voluptuous",
        "aiohttp"
    ],
)