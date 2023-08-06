from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent

setup(name="noliboskar", version="0.0.3",
      author="Oskar",
      author_email="example@example.com",
      license="MIT",
      description="My test package",
      long_description=(this_directory / "README.md").read_text(),
      long_description_content_type="text/markdown",
      packages=find_packages(exclude=("me")),
      #install_requires=["pygame>='3.4'"],
      include_package_data=True
)