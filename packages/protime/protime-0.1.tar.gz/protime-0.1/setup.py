from setuptools import setup, find_packages

setup(

	name 		= 'protime',
	version 	= '0.1',
	description = 'Shortens Writing Waiting Time Using Symbols (1s, 1m, 1h, 1d, 1w)',
	author   	= 'Abdulrahman Abouldahab',
	packages 	= find_packages(),
	scripts		= ['protime/protime.py'],
	zip_safe 	= False

)