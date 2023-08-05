
from setuptools import setup,find_packages
DESCRIPTION = 'TMGM Risk Used -- Bowen Yan'


setup(
    name = "pytmgmOps",
    version = "0.0.2",
    author = "Bowen Yan (TMGM Risk)",

    description = DESCRIPTION,
    install_requires=['sqlalchemy', 'snowflake-connector-python', 'snowflake-sqlalchemy','pandas','pyathena','mysql-connector-python==8.0.28'],
    py_modules=["pytmgmOps"],
    package_dir = {"": "src"},
    packages = find_packages(where="src"),
    
)