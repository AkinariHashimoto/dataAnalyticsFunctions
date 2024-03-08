from setuptools import setup, find_packages

setup(name="dataAnalyticsFunctions",
	version="0.1",
	description="analytics functions",
	url="https://github.com/AkinariHashimoto/dataAnalyticsFunctions",
	packages=find_packages(),
	entry_points="""
	[console_scripts]
	functions = function.function:main
	""",
	)