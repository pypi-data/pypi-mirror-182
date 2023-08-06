from setuptools import setup
setup(
    name="Lavinia-Mihalache_own_package",
    version="0.1.0",
    author="Lavinia Mihalache",
    author_email="mihalache_mihaela_lavinia@yahoo.com",
    packages=["my_own_package"],
    package_dir={"":"src/"},
    include_package_data=True,
    description="my_first_package"

)