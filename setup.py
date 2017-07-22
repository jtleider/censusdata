from distutils.core import setup

setup(
	name='CensusData',
	version='0.1',
	description='Download data from U.S. Census API',
	long_description=open('README.rst').read(),
	url='',
	author='Julien Leider',
	license='MIT',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Intended Audience :: Science/Research',
		'Topic :: Scientific/Engineering',
		'License :: OSI Approved :: MIT License',
		'Programming Language :: Python :: 3',
	],
	keywords='census',
	packages=['censusdata',],
	install_requires=['pandas', 'requests',],
	python_requires='>=3',
	package_data={
		'variables': ['acs1_2015_cprofile_variables.json', 'acs1_2015_detail_variables.json', 'acs1_2015_profile_variables.json',
			'acs1_2015_subject_variables.json', 'acs5_2015_cprofile_variables.json', 'acs5_2015_detail_variables.json',
			'acs5_2015_profile_variables.json', 'acs5_2015_subject_variables.json',]
	}
)

