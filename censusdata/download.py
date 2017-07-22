"""Functions for downloading data and lists of geographies from the Census API."""

from . import censusgeo
import pandas as pd
from collections import OrderedDict
import requests

def _download(src, year, params, baseurl = 'http://api.census.gov/data/'):
	"""Request data from Census API. Returns data in ordered dictionary. Called by geographies() and download()."""
	url = baseurl + str(year) + '/' + src + '?' + '&'.join('='.join(param) for param in params.items())
	r = requests.get(url)
	try:
		data = r.json()
	except:
		print('Unexpected response (URL: {0.url}): {0.text} '.format(r))
		raise ValueError
	rdata = OrderedDict()
	for j in range(len(data[0])):
		rdata[data[0][j]] = [data[i][j] for i in range(1, len(data))]
	return rdata

def geographies(within, src, year, key=None):
	"""List geographies within a given geography, e.g., counties within a state.

	Args:
		within (censusgeo): Geography within which to list geographies.
		src (str): Census data source.
		year (str): Year of data.
		key (str, optional): Census API key.

	Returns:
		Dictionary with names as keys and censusgeo objects as values.

	Examples:
		
	"""
	georequest = within.request()
	params = {'get': 'NAME'}
	params.update(georequest)
	if key is not None: params.update({'key': key})
	geo = _download(src, year, params)
	name = geo['NAME']
	del geo['NAME']
	return {name[i]: censusgeo([(key, geo[key][i]) for key in geo]) for i in range(len(name))}

def download(src, year, geo, var, key=None, tabletype='detail'):
	"""Download data from Census API.

	Args:
		src (str): Census data source.
		year (str): Year of data.
		var (list of str): Census variables to download.
		key (str, optional): Census API key.
		tabletype (str, optional): Type of table from which variables are drawn. Options are 'detail' (detail tables), 'subject' (subject tables), 'profile' (data profile tables), 'cprofile' (comparison profile tables).

	Returns:
		pandas.DataFrame with columns corresponding to designated variables, and row index of censusgeo objects representing Census geographies.

	Raises:
		ValueError: If unknown tabletype is specified.

	Examples:
		
	"""
	try:
		assert tabletype == 'detail' or tabletype == 'subject' or tabletype == 'profile' or tabletype == 'cprofile'
	except AssertionError:
		print('Unknown table type {0}!'.format(tabletype))
		raise ValueError
	if tabletype == 'detail':
		tabletype = ''
	else:
		tabletype = '/' + tabletype
	georequest = geo.request()
	params = {'get': ','.join(['NAME']+var)}
	params.update(georequest)
	if key is not None: params.update({'key': key})
	data = _download(src + tabletype, year, params)
	geodata = data.copy()
	for key in list(geodata.keys()):
		if key in var:
			del geodata[key]
			try:
				data[key] = [int(d) for d in data[key]]
			except ValueError:
				try:
					data[key] = [float(d) for d in data[key]]
				except ValueError:
					data[key] = [d for d in data[key]]
		else:
			del data[key]
	geoindex = [censusgeo([(key, geodata[key][i]) for key in geodata if key != 'NAME'], geodata['NAME'][i]) for i in range(len(geodata['NAME']))]
	return pd.DataFrame(data, geoindex)

