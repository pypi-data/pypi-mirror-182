from setuptools import setup
setup(
    name="ana-tanase-own-package",
    version="0.2.0",
    author="Ana Tanase",
    author_email="tanase_ana253@yahoo.com",
    packages=["my_own_package"],
    package_dir={"": "src\\"},
    include_package_data=True,
    description="my_first_package"
)