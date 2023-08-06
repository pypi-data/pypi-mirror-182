from setuptools import setup

setup(
    name="alex-moldovan-first-package",
    version="0.1.0",
    author="Alex Moldovan",
    author_email="alex_moldovan1@yahoo.com",
    packages=["my_own_package"],
    package_dir={"": "src\\"},
    include_package_data=True,
    description="my_first_package"
)
