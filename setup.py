"""Setup file for weather-app-tkinter"""

import os.path
from setuptools import setup

# The directory containing this file
THIS = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(THIS, "README.md")) as fid:
	README = fid.read()

setup (
	name = "weather-app-tkinter",
	version="1.0.0",
	description="Show the weather information of different cities",
	long_description=README,
	long_description_content_type="text/markdown",
	url="https://github.com/sam0132nodier/weather-app-tkinter",
	author="Sam Nodier",
	author_email="sam0132nodier@gmail.com",
	license="MIT",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Lnaguage :: Python :: 3",
	],
	packages=["weatherapp"],
	include_package_data=True,
	install_requires=[
		"tkinter", "PIL", "requests", "time", "io",
	],
	entry_points={"console_scripts": ["weatherapp=weatherapp.__main__:main"]},
)
