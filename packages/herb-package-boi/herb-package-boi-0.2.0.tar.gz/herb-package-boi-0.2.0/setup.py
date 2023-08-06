from setuptools import setup
setup(
    name="herb-package-boi",
    version="0.2.0",
    author="Fetz Herbert",
    author_email="fetz.martin.herbert.ovb@gmail.com",
    packages=["my_own_package"],
    package_dir={"":"src\\"},
    include_package_data=True,
    description="my_first_package"
)