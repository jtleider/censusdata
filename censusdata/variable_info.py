"""Functions for showing information about Census variables."""

from __future__ import absolute_import, division, print_function, unicode_literals

import requests
import os
import re
import json
from collections import OrderedDict

def censusvar(src, year, var):
	"""Download information on a list of variables from Census API.

	Args:
		src (str): Census data source: 'acs1' for ACS 1-year estimates, 'acs5' for ACS 5-year estimates, 'acs3' for
			ACS 3-year estimates, 'acsse' for ACS 1-year supplemental estimates, 'sf1' for SF1 data.
		year (int): Year of data.
		var (list of str): Names of Census variable.

	Returns:
		dict: Dictionary with keys 'concept' (overall concept the variable falls under), 'label' (variable label),
			and 'predicateType' (variable type).

	Examples::

		censusdata.censusvar('sf1', 2010, ['P001001']) # Returns information on the variable P0010001 from the 2010 Census SF1.
	"""
	assert src == 'acs1' or src == 'acs3' or src == 'acs5' or src == 'acsse' or src == 'sf1'
	ret = dict()
	for v in var:
		if src == 'acsse' or src == 'sf1' or v[0] == 'B':
			tabletype = ''
		elif v[0] == 'S':
			tabletype = 'subject/'
		elif v[:2] == 'DP':
			tabletype = 'profile/'
		elif v[:2] == 'CP':
			tabletype = 'cprofile/'
		elif v[0] == 'C':
			tabletype = ''
		else:
			raise ValueError(u'Unknown table type for variable {0}!'.format(v))
		if (src == 'acs1' or src == 'acs5' or src == 'acsse') and year >= 2010: presrc = 'acs/'
		elif src == 'acs3': presrc = 'acs/'
		elif src == 'sf1': presrc = 'dec/'
		else: presrc = ''
		r = requests.get('https://api.census.gov/data/{year}/{presrc}{src}/{tabletype}variables/{v}.json'.format(src=src, year=year, v=v, tabletype=tabletype, presrc=presrc))
		try:
			data = r.json()
		except:
			raise ValueError(u'Unexpected response (URL: {0.url}): {0.text} '.format(r))
		try:
			assert data['name'] == v
		except AssertionError:
			raise AssertionError(u'JSON variable information does not include key "name"', data)
		expectedKeys = ['group', 'label', 'limit', 'name',]
		try:
			assert [k for k in sorted(data.keys()) if k != 'attributes' and k != 'concept' and k != 'predicateType'] == expectedKeys
		except AssertionError:
			print(u'JSON variable information does not include expected keys ({0} and possibly attributes, concept, predicateType) or includes extra keys: '.format(expectedKeys), data)
		try: 
			ret[v] = [data.get('concept', ''), data['label'], data.get('predicateType', '')] # Concept, predicate type not provided for all years; default to empty if not provided
		except KeyError:
			raise KeyError(u'JSON variable information does not include expected keys: ', data)
	return ret

def censustable(src, year, table):
	"""Look up information on all variables in a table.

	Args:
		src (str): Census data source: 'acs1' for ACS 1-year estimates, 'acs5' for ACS 5-year estimates, 'acs3' for
			ACS 3-year estimates, 'acsse' for ACS 1-year supplemental estimates, 'sf1' for SF1 data.
		year (int): Year of data.
		table (str): Table name.

	Returns:
		OrderedDict: Dictionary of variables in table, with keys 'concept' (overall concept the variable falls under), 'label' (variable label),
			and 'predicateType' (variable type).

	Examples::

		censusdata.censustable('acs1', 2015, 'B23025') # Returns information on table B23025 (Employment Status for Population 16+ Years) from the ACS 2015 1-year estimates.
	"""
	assert src == 'acs1' or src == 'acs3' or src == 'acs5' or src == 'acsse' or src == 'sf1'
	if src == 'acsse' or src == 'sf1':
		tabletype = ''
	elif table[0] == 'B':
		tabletype = 'detail_'
	elif table[0] == 'S':
		tabletype = 'subject_'
	elif table[:2] == 'DP':
		tabletype = 'profile_'
	elif table[:2] == 'CP':
		tabletype = 'cprofile_'
	elif table[0] == 'C':
		tabletype = 'detail_'
	else:
		raise ValueError(u'Unknown table type for table {0}!'.format(table))
	topdir, filename = os.path.split(__file__)
	with open(os.path.join(topdir, 'variables', '{0}_{1}_{2}variables.json'.format(src, year, tabletype))) as infile:
		allvars = infile.read()
	allvars = json.loads(allvars)['variables']
	ret = OrderedDict()
	for k in sorted(allvars.keys()):
		if ((src != 'sf1' and k[:len(table)+1] == table+'_')
			or (src == 'sf1' and k[:len(table)] == table)): # SF1 variables do not include underscores after table names
			if 'predicateType' not in allvars[k]: allvars[k]['predicateType'] = ''
			ret[k] = {'label': allvars[k]['label'], 'concept': allvars[k]['concept'], 'predicateType': allvars[k]['predicateType']}
	if len(ret) == 0:
		raise ValueError(u'Table not found!')
	return ret

def printtable(table, moe=False):
	"""Pretty print information on a Census table (such as produced by `censustable`).

	Args:
		table (OrderedDict): Table information from censustable.
		moe (bool, optional): Display margins of error.

	Returns:
		None.

	Examples::

		censusdata.printtable(censusdata.censustable('acs5', 2015, 'B19013'))
	"""
	print(u'{0:12} | {1:30.30} | {2:56} | {3:5}'.format('Variable', 'Table', 'Label', 'Type'))
	print(u'-'*115)
	for k in table.keys():
		if not moe and k[-1] == 'M': continue # don't clutter output with margins of error
		label = table[k]['label']
		label = '!! '*label.count('!!') + label.replace('!!', ' ')
		print(u'{0:12} | {1:30.30} | {2:56.56} | {3:5}'.format(k, table[k]['concept'], label, table[k]['predicateType']))
	print(u'-'*115)
	return None

def search(src, year, field, criterion, tabletype='detail'):
	"""Search Census variables.

	Args:
		src (str): Census data source: 'acs1' for ACS 1-year estimates, 'acs5' for ACS 5-year estimates, 'acs3' for
			ACS 3-year estimates, 'acsse' for ACS 1-year supplemental estimates, 'sf1' for SF1 data.
		year (int): Year of data.
		field (str): Field in which to search.
		criterion (str or function): Search criterion. Either string to search for, or a function which will be passed the value of field and return
			True if a match and False otherwise.
		tabletype (str, optional): Type of table from which variables are drawn (only applicable to ACS data). Options are 'detail' (detail tables),
			'subject' (subject tables), 'profile' (data profile tables), 'cprofile' (comparison profile tables).

	Returns:
		list: List of 3-tuples containing variable names, concepts, and labels matching the search criterion.

	Examples::

		# Search for ACS 2011-2015 5-year estimate variables where the concept includes the text 'unweighted sample'.
		censusdata.search('acs5', 2015, 'concept', 'unweighted sample') 
		# Search for ACS 2011-2015 5-year estimate variables where the specific variable label includes the text 'unemploy'.
		censusdata.search('acs5', 2015, 'label', 'unemploy') 
		# Search for ACS 2011-2015 5-year estimate variables where the concept includes the text 'unweighted sample' and the text 'housing'.
		censusdata.search('acs5', 2015, 'concept', lambda value: re.search('unweighted sample', value, re.IGNORECASE) and re.search('housing', value, re.IGNORECASE))
	"""

	if hasattr(criterion, '__call__'): match = criterion
	else: match = lambda value: re.search(criterion, value, re.IGNORECASE)

	try:
		assert tabletype == 'detail' or tabletype == 'subject' or tabletype == 'profile' or tabletype == 'cprofile'
	except AssertionError:
		raise ValueError(u'Unknown table type {0}!'.format(tabletype))
	topdir, filename = os.path.split(__file__)
	variable_filename = '{0}_{1}_{2}_variables.json'.format(src, year, tabletype)
	if src == 'sf1' or src == 'acsse': variable_filename = '{0}_{1}_variables.json'.format(src, year)
	with open(os.path.join(topdir, 'variables', variable_filename)) as infile:
		allvars = infile.read()
	allvars = json.loads(allvars)['variables']
	return [(k, allvars[k].get('concept'), allvars[k].get('label')) for k in sorted(allvars.keys()) if match(allvars[k].get(field, ''))]

