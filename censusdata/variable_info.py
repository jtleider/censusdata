"""Functions for showing information about Census variables."""

import requests
import os
import re
import json
from collections import OrderedDict

def censusvar(src, year, var):
	"""Download information on a list of variables from Census API."""
	ret = dict()
	for v in var:
		if v[0] == 'B':
			tabletype = ''
		elif v[0] == 'S':
			tabletype = 'subject/'
		elif v[:2] == 'DP':
			tabletype = 'profile/'
		elif v[:2] == 'CP':
			tabletype = 'cprofile/'
		else:
			print('Unknown table type for variable {0}!'.format(v))
			raise ValueError
		r = requests.get('http://api.census.gov/data/{1}/{0}/{3}variables/{2}.json'.format(src, year, v, tabletype))
		try:
			data = r.json()
		except:
			print('Unexpected response (URL: {0.url}): {0.text} '.format(r))
			raise ValueError
		try:
			assert data['name'] == v
		except AssertionError:
			print('JSON variable information does not include key "name"', data)
			raise
		try:
			assert len(data.keys()) == 4
		except AssertionError:
			print('JSON variable information includes unexpected number of keys ({0}, instead of 4): '.format(len(data.keys())), data)
		try: 
			ret[v] = [data['concept'], data['label'], data['predicateType']]
		except KeyError:
			print('JSON variable information does not include expected keys: ', data)
			raise
	return ret

def censustable(src, year, table):
	"""Show information on all variables in a table."""
	if table[0] == 'B':
		tabletype = 'detail'
	elif table[0] == 'S':
		tabletype = 'subject'
	elif table[:2] == 'DP':
		tabletype = 'profile'
	elif table[:2] == 'CP':
		tabletype = 'cprofile'
	else:
		print('Unknown table type for table {0}!'.format(table))
		raise ValueError
	topdir, filename = os.path.split(__file__)
	with open(os.path.join(topdir, 'variables', '{0}_{1}_{2}_variables.json'.format(src, year, tabletype))) as infile:
		allvars = infile.read()
	allvars = json.loads(allvars)['variables']
	ret = OrderedDict()
	for k in sorted(allvars.keys()):
		if '_'.join(k.split('_')[:-1]) == table:
			ret[k] = allvars[k]
	if len(ret) == 0:
		print('Table not found!')
		raise ValueError
	return ret

def printtable(table, moe=False):
	"""Pretty print information on a Census table (such as produced by censustable)."""
	print('{0:20} | {1:40.40} | {2:160} | {3:10}'.format('Variable', 'Table', 'Label', 'Type'))
	print('-'*239)
	for k in table.keys():
		if not moe and k[-1] == 'M': continue # don't clutter output with margins of error
		label = table[k]['label']
		label = '!! '*label.count('!!') + label.replace('!!', ' ')
		print('{0:20} | {1:40.40} | {2:160.160} | {3:10}'.format(k, table[k]['concept'], label, table[k]['predicateType']))
	print('-'*239)

def search(src, year, field, criterion, tabletype='detail'):
	"""Search Census variables."""
	try:
		assert tabletype == 'detail' or tabletype == 'subject' or tabletype == 'profile' or tabletype == 'cprofile'
	except AssertionError:
		print('Unknown table type {0}!'.format(tabletype))
		raise ValueError
	topdir, filename = os.path.split(__file__)
	with open(os.path.join(topdir, 'variables', '{0}_{1}_{2}_variables.json'.format(src, year, tabletype))) as infile:
		allvars = infile.read()
	allvars = json.loads(allvars)['variables']
	return [(k, allvars[k]['concept'], allvars[k]['label']) for k in sorted(allvars.keys()) if re.search(criterion, allvars[k][field], re.IGNORECASE)]

