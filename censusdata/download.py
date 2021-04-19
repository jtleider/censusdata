"""Functions for downloading data and lists of geographies from the Census API."""

from __future__ import absolute_import, division, print_function, unicode_literals

from . import censusgeo
import pandas as pd
from collections import OrderedDict
import requests

def _download(src, year, params, baseurl = 'https://api.census.gov/data/', endpt = ''):
	"""Request data from Census API. Returns data in ordered dictionary. Called by `geographies()` and `download()`.

	Args:
		src (str): Census data source: 'acs1' for ACS 1-year estimates, 'acs5' for ACS 5-year estimates, 'acs3' for
			ACS 3-year estimates, 'acsse' for ACS 1-year supplemental estimates, 'sf1' for SF1 data.
		year (int): Year of data.
		params (dict): Download parameters.
		baseurl (str, optional): Base URL for download.
		endpt (str, optional): Allows override of whether old or new API endpoint is used. Specify
			'old' for old, 'new' for new, '' to use default. This option generally shouldn't
			need to be specified but can be helpful if download problems are encountered.
	"""
	if src[:4] == 'acs1' or src[:4] == 'acs5' or src[:5] == 'acsse':
		if endpt == 'new': presrc = 'acs/'
		elif endpt == 'old': presrc = ''
		elif endpt == '': presrc = 'acs/' if year >= 2010 else ''
	elif src[:4] == 'acs3':
		presrc = 'acs/'
	elif src[:3] == 'sf1':
		if endpt == 'new' or endpt == '': presrc = 'dec/'
		if endpt == 'old': presrc = ''
	else: presrc = ''
	url = baseurl + str(year) + '/' + presrc + src + '?' + '&'.join('='.join(param) for param in params.items())
	r = requests.get(url)
	try:
		data = r.json()
	except:
		raise ValueError('Unexpected response (URL: {0.url}): {0.text} '.format(r))
	rdata = OrderedDict()
	for j in range(len(data[0])):
		rdata[data[0][j]] = [data[i][j] for i in range(1, len(data))]
	return rdata

def geographies(within, src, year, key=None, endpt=''):
	"""List geographies within a given geography, e.g., counties within a state.

	Args:
		within (censusgeo): Geography within which to list geographies.
		src (str): Census data source: 'acs1' for ACS 1-year estimates, 'acs5' for ACS 5-year estimates, 'acs3' for
			ACS 3-year estimates, 'acsse' for ACS 1-year supplemental estimates, 'sf1' for SF1 data.
		year (int): Year of data.
		key (str, optional): Census API key.
		endpt (str, optional): Allows override of whether old or new API endpoint is used. Specify
			'old' for old, 'new' for new, '' to use default. This option generally shouldn't
			need to be specified but can be helpful if download problems are encountered.

	Returns:
		dict: Dictionary with names as keys and `censusgeo` objects as values.

	Examples::

		# Pull data on all state geographies from the ACS 2011-2015 5-year estimates.
		censusdata.geographies(censusdata.censusgeo([('state', '*')]), 'acs5', 2015)
	"""
	georequest = within.request()
	params = {'get': 'NAME'}
	params.update(georequest)
	if key is not None: params.update({'key': key})
	geo = _download(src, year, params, endpt=endpt)
	name = geo['NAME']
	del geo['NAME']
	return {name[i]: censusgeo([(key, geo[key][i]) for key in geo]) for i in range(len(name))}

def download(src, year, geo, var, key=None, tabletype='detail', endpt=''):
	"""Download data from Census API.

	Args:
		src (str): Census data source: 'acs1' for ACS 1-year estimates, 'acs5' for ACS 5-year estimates, 'acs3' for
			ACS 3-year estimates, 'acsse' for ACS 1-year supplemental estimates, 'sf1' for SF1 data.
		year (int): Year of data.
		geo (censusgeo): Geographies for which to download data.
		var (list of str): Census variables to download.
		key (str, optional): Census API key.
		tabletype (str, optional): Type of table from which variables are drawn (only applicable to ACS data). Options are 'detail' (detail tables),
			'subject' (subject tables), 'profile' (data profile tables), 'cprofile' (comparison profile tables).
		endpt (str, optional): Allows override of whether old or new API endpoint is used. Specify
			'old' for old, 'new' for new, '' to use default. This option generally shouldn't
			need to be specified but can be helpful if download problems are encountered.

	Returns:
		pandas.DataFrame: Data frame with columns corresponding to designated variables, and row index of censusgeo objects representing Census geographies.

	Raises:
		ValueError: If unknown tabletype is specified.

	Examples::

		# Download ACS 2011-2015 5-year estimates for Oakland city, California on population size, median age, and median household income.
		censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '06'), ('place', '53000')]), ['B01001_001E', 'B01002_001E', 'B19013_001E'])
	"""
	try:
		assert tabletype == 'detail' or tabletype == 'subject' or tabletype == 'profile' or tabletype == 'cprofile'
	except AssertionError:
		raise ValueError('Unknown table type {0}!'.format(tabletype))
	if tabletype == 'detail':
		tabletype = ''
	else:
		tabletype = '/' + tabletype
	georequest = geo.request()
	data = OrderedDict()
	chunk_size = 49
	for var_chunk in [var[i:(i+chunk_size)] for i in range(0, len(var), chunk_size)]:
		params = {'get': ','.join(['NAME']+var_chunk)}
		params.update(georequest)
		if key is not None: params.update({'key': key})
		data.update(_download(src + tabletype, year, params, endpt=endpt))
	geodata = data.copy()
	for key in list(geodata.keys()):
		if key in var:
			del geodata[key]
			try:
				data[key] = [int(d) if d is not None else None for d in data[key]]
			except ValueError:
				try:
					data[key] = [float(d) if d is not None else None for d in data[key]]
				except ValueError:
					data[key] = [d for d in data[key]]
		else:
			del data[key]
	geoindex = [censusgeo([(key, geodata[key][i]) for key in geodata if key != 'NAME'], geodata['NAME'][i]) for i in range(len(geodata['NAME']))]
	return pd.DataFrame(data, geoindex)

