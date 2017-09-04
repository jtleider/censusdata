"""Functions for showing information about Census variables."""

from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import os
import re
import json
from collections import OrderedDict

def censusvar(src, year, var):
	"""Download information on a list of variables from Census API."""
	assert src == 'acs1' or src == 'acs3' or src == 'acs5' or src == 'acsse'
	ret = dict()
	for v in var:
		if src == 'acsse' or v[0] == 'B':
			tabletype = ''
		elif v[0] == 'S':
			tabletype = 'subject/'
		elif v[:2] == 'DP':
			tabletype = 'profile/'
		elif v[:2] == 'CP':
			tabletype = 'cprofile/'
		else:
			print(u'Unknown table type for variable {0}!'.format(v))
			raise ValueError
		r = requests.get('https://api.census.gov/data/{1}/{0}/{3}variables/{2}.json'.format(src, year, v, tabletype))
		try:
			data = r.json()
		except:
			print(u'Unexpected response (URL: {0.url}): {0.text} '.format(r))
			raise ValueError
		try:
			assert data['name'] == v
		except AssertionError:
			print(u'JSON variable information does not include key "name"', data)
			raise
		try:
			assert len(data.keys()) == 7
		except AssertionError:
			print(u'JSON variable information includes unexpected number of keys ({0}, instead of 7): '.format(len(data.keys())), data)
		if 'predicateType' not in data: data['predicateType'] = ''
		try: 
			ret[v] = [data['concept'], data['label'], data['predicateType']]
		except KeyError:
			print(u'JSON variable information does not include expected keys: ', data)
			raise
	return ret

def censustable(src, year, table):
	"""Show information on all variables in a table."""
	assert src == 'acs1' or src == 'acs3' or src == 'acs5' or src == 'acsse'
	if src == 'acsse':
		tabletype = ''
	elif table[0] == 'B':
		tabletype = 'detail_'
	elif table[0] == 'S':
		tabletype = 'subject_'
	elif table[:2] == 'DP':
		tabletype = 'profile_'
	elif table[:2] == 'CP':
		tabletype = 'cprofile_'
	else:
		print(u'Unknown table type for table {0}!'.format(table))
		raise ValueError
	topdir, filename = os.path.split(__file__)
	with open(os.path.join(topdir, 'variables', '{0}_{1}_{2}variables.json'.format(src, year, tabletype))) as infile:
		allvars = infile.read()
	allvars = json.loads(allvars)['variables']
	ret = OrderedDict()
	for k in sorted(allvars.keys()):
		if '_'.join(k.split('_')[:-1]) == table:
			if 'predicateType' not in allvars[k]: allvars[k]['predicateType'] = ''
			ret[k] = {'label': allvars[k]['label'], 'concept': allvars[k]['concept'], 'predicateType': allvars[k]['predicateType']}
	if len(ret) == 0:
		print(u'Table not found!')
		raise ValueError
	return ret

def printtable(table, moe=False):
	"""Pretty print information on a Census table (such as produced by censustable)."""
	print(u'{0:20} | {1:40.40} | {2:160} | {3:10}'.format('Variable', 'Table', 'Label', 'Type'))
	print(u'-'*239)
	for k in table.keys():
		if not moe and k[-1] == 'M': continue # don't clutter output with margins of error
		label = table[k]['label']
		label = '!! '*label.count('!!') + label.replace('!!', ' ')
		print(u'{0:20} | {1:40.40} | {2:160.160} | {3:10}'.format(k, table[k]['concept'], label, table[k]['predicateType']))
	print(u'-'*239)

def search(src, year, field, criterion, tabletype='detail'):
	"""Search Census variables."""
	try:
		assert tabletype == 'detail' or tabletype == 'subject' or tabletype == 'profile' or tabletype == 'cprofile'
	except AssertionError:
		print(u'Unknown table type {0}!'.format(tabletype))
		raise ValueError
	topdir, filename = os.path.split(__file__)
	with open(os.path.join(topdir, 'variables', '{0}_{1}_{2}_variables.json'.format(src, year, tabletype))) as infile:
		allvars = infile.read()
	allvars = json.loads(allvars)['variables']
	return [(k, allvars[k]['concept'], allvars[k]['label']) for k in sorted(allvars.keys()) if re.search(criterion, allvars[k][field], re.IGNORECASE)]

