import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="gesture-recognizer",
	version="0.2.2",
	author="capjedi",
	author_email="calee14@s.sfusd.edu",
	license='MIT',
	description="A basic gesture recognizer module for a hackathon.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/calee14/gesture-recognizer",
	install_requires=[
          'opencv-python',
          'numpy',],
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
