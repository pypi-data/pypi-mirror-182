from setuptools import setup

setup(
    name="Horia's-first-package",
    version="0.1.0",
    author="Litan Horia",
    author_email="horialitan@yahoo.com",
    packages=["my_own_package"],
    package_dir={"":"src\\"},
    include_package_data=True,
    description="My first package - Horia"
)