# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "com_csaa_claims_ai_assignment"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion==2.0.0",
    "swagger-ui-bundle==0.0.2",
    "python_dateutil==2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="AiClaimAssignmentAPI",
    author_email="DLDataServices@csaa.com",
    url="",
    keywords=["OpenAPI", "AiClaimAssignmentAPI"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['com_csaa_claims_ai_assignment=com_csaa_claims_ai_assignment.__main__:main']},
    long_description="""\
    Claims assignment using AI
    """
)

