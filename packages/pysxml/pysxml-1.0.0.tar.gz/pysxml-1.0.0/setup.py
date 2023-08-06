from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / ".exported.md").read_text()

setup(
    name="pysxml",
    version="1.0.0",
    description="Generate XML and HTML using an SXML-like syntax",
    license="BSD",
    url="https://codeberg.org/antero/pysxml",
    author="Antero",
    py_modules=["pysxml"],
    long_description=long_description,
    long_description_content_type="text/markdown")
