from distutils.core import setup

setup(
	name='CensusData',
	version='0.1',
	description='Download data from U.S. Census API',
	long_description=open('README.rst').read(),
	url='https://github.com/jtleider/censusdata',
	author='Julien Leider',
	author_email='jtleider@gmail.com',
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
		'censusdata': ['variables/*.json',],
	}
)

