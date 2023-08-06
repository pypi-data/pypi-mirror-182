from io import open
from setuptools import setup

version = "0.0.2"

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="check_password",
    version=version,

    author="pavelgs",
    author_email="p6282813@yandex.ru",

    description="lib for check password, email or date for validate",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/pavelglazunov/-check-password-",

    license="Apache License, Version 2.0, see LICENSE file",

    packages=["check_password"]
)