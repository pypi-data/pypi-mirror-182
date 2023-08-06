from setuptools import setup

setup(
	name="DanDFG-First-Package",
	version="0.2.0",
	author="Daniel DFG",
	author_email="danieldfgro2000@gmail.com",
	packages=["my_own_package"],
	package_dir={"": "src/"},
	include_package_data=True,
	description="My first package"
)
