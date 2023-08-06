from setuptools import setup
setup(
    name="iulia-balan-own-package",
    version="0.1.0",
    author="Iulia Balan",
    author_email="denisabalan732@yahoo.com",
    packages=["my_own_package"],
    package_dir={"":"src/"},
    include_package_data=True,
    description="my_first_package"

)

