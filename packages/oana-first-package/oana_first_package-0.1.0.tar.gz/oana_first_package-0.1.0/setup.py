from setuptools import setup
setup(
    name="oana_first_package",
    version="0.1.0",
    author="Oana Iliescu",
    authot_email="oanail@yahoo.com",
    packages=["my_own_package"],
    package_dir={"":"src\\"},
    include_package_data=True,
    description="my_first_package"
)