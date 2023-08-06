from setuptools import setup
setup(
    name="Tedi-first-package",
    version="0.1.0",
    author="Toader-Gavril Farcasanu",
    author_email="farcasanu_t@yahoo.com",
    packages=["my_own_package"],
    package_dir={"":"src\\"},
    include_package_data=True,
    description="my_first_package"

)