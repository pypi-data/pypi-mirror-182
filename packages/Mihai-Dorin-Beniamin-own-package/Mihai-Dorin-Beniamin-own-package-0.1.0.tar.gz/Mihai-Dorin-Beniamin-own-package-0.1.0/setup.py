from setuptools import setup
setup(
    name="Mihai-Dorin-Beniamin-own-package",
    version="0.1.0",
    author="Mihai Dorin",
    author_email="mihaidorin9727@yahoo.com",
    packages=["my_own_package"],
    package_dir={"":"src\\"},
    include_package_data=True,# ne spune daca libraria noastra
    description="my_frist_package"

)

