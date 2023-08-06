
from setuptools import setup
setup(
    name= "gsdolea-my-own- package",
    version= "0.2.0",
    author= "geo dolea",
    author_email="gsdolea@gmail.com",
    packages=["my_own_package"],
    package_dir= {"": "src/"},
    include_package_data= True,
    description= "my_first_package"
)
