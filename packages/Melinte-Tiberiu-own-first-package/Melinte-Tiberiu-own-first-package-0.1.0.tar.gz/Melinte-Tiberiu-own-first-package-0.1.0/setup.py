from setuptools import setup

setup(
    name="Melinte-Tiberiu-own-first-package",
    version="0.1.0",
    author="Melinte Tiberiu",
    author_email="melintetiberiu@yahoo.com",
    packages=["my_own_package"],
    package_dir={"": "src\\"},
    include_package_data=True,
    description="This my first package"
)
