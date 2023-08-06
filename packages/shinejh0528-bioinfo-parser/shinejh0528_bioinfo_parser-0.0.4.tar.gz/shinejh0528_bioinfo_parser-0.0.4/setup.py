import setuptools

with open("readme.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="shinejh0528_bioinfo_parser", # Replace with your own username
	version="0.0.4",
	author="Jonghwan Shin",
	author_email="shinejh0528@gmail.com",
	description="Bioinfomatics parser",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/Shin-jongwhan/python_pypi/tree/main/bioinfo_parser",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)
