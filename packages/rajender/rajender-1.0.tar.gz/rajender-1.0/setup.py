import setuptools
from pathlib import Path
setuptools.setup(
    name="rajender",
    version=1.0,
    longdescription=Path("README.md").read_text(),
    packages=setuptools.find_packages(exclude= ["tests","data"])
)