from __future__ import absolute_import, division, print_function, unicode_literals

class censusgeo:
	"""Class for representing Census geographies.

	Args:
		geo (tuple of 2-tuples of strings): Tuple of 2-tuples of the form (geographic component, identifier), where geographic component is a string (e.g., 'state') and
			identifier is either a numeric code (e.g., '01') or a wildcard ('*'). These identify the geography in question.
		name (str, optional): Name of geography (e.g., 'Alabama').

	Examples::

		censusgeo([('state', '06'), ('place', '53000')], 'Oakland city, California') # Represents the Census geography for Oakland city, California.
		censusgeo([('state', '17'), ('county', '031')]) # Represents the Census geography for Cook County, Illinois.
	"""

	#: dict: Census summary level codes for different types of geography
	sumleveldict = {
		'us': '010',
		'region': '020',
		'division': '030',
		'state': '040',
		'state> county': '050',
		'state> county> county subdivision': '060',
		'state> county> county subdivision> subminor civil division': '067',
		'state> county> county subdivision> place/remainder (or part)': '070',
		'state> county> county subdivision> place > tract (or part)': '080',
		'state> county> tract> block': '101',
		'state> county> tract': '140',
		'state> county> tract> block group': '150',
		'state> place> county (or part)': '155',
		'state> place': '160',
		'state> consolidated city': '170',
		'state> consolidated city> place (or part)': '172',
		'state> alaska native regional corporation': '230',
		'american indian area/alaska native area/hawaiian home land': '250',
		'american indian area/alaska native area/hawaiian home land> tribal subdivision/remainder': '251',
		'american indian area/alaska native area (reservation or statistical entity only)': '252',
		'american indian area (off-reservation trust land only)/hawaiian home land': '254',
		'american indian area/alaska native area/hawaiian home land> tribal census tract': '256',
		'american indian area/alaska native area/hawaiian home land> tribal census tract> tribal block group': '258',
		'american indian area/alaska native area/hawaiian home land> state': '260',
		'american indian area/alaska native area/hawaiian home land> state> place/remainder': '269',
		'american indian area/alaska native area/hawaiian home land> state> county': '270',
		'state> american indian area/alaska native area/hawaiian home land (or part)': '280',
		'state> american indian area> tribal subdivision/remainder (or part)': '281',
		'state> american indian area/alaska native area (reservation or statistical entity only) (or part)': '283',
		'state> american indian area (off-reservation trust land only)/hawaiian home land (or part)': '286',
		'american indian area/alaska native area/hawaiian home land> tribal subdivision/remainder> state': '290',
		'american indian area/alaska native area/hawaiian home land> tribal census tract (or part) within aia (reservation only)': '291',
		'american indian area/alaska native area/hawaiian home land> tribal census tract (or part) within aia (trust land only)': '292',
		'american indian area/alaska native area/hawaiian home land> tribal census tract> tribal block group (or part) within tribal census tract within aia (reservation only)': '293',
		'american indian area/alaska native area/hawaiian home land> tribal census tract> tribal block group (or part) within tribal census tract within aia (trust land only)': '294',
		'metropolitan statistical area/micropolitan statistical area': '310',
		'metropolitan statistical area/micropolitan statistical area> state': '311',
		'metropolitan statistical area/micropolitan statistical area> state> principal city': '312',
		'metropolitan statistical area/micropolitan statistical area> metropolitan division': '314',
		'metropolitan statistical area> metropolitan division> state': '315',
		'state> metropolitan statistical area/micropolitan statistical area (or part)': '320',
		'state> metropolitan statistical area/micropolitan statistical area> principal city (or part)': '321',
		'state> metropolitan statistical area/micropolitan statistical area> county': '322',
		'state> metropolitan statistical area/micropolitan statistical area> metropolitan division (or part)': '323',
		'state> metropolitan statistical area/micropolitan statistical area> metropolitan division> county': '324',
		'combined statistical area': '330',
		'combined statistical area> state': '331',
		'combined statistical area> micropolitan statistical area': '332',
		'combined statistical area> metropolitan statistical area/micropolitan statistical area> state': '333',
		'combined new england city and town area': '335',
		'combined new england city and town area> state': '336',
		'combined new england city and town area> new england city and town area': '337',
		'combined new england city and town area> new england city and town area> state': '338',
		'state> combined statistical area (or part)': '340',
		'state> combined statistical area> metropolitan statistical area/micropolitan statistical area (or part)': '341',
		'state> combined new england city and town area (or part)': '345',
		'state> combined new england city and town area> new england city and town area (or part)': '346',
		'new england city and town area': '350',
		'new england city and town area> state': '351',
		'new england city and town area> state> principal city': '352',
		'new england city and town area> necta division': '355',
		'new england city and town area> necta division> state': '356',
		'state> new england city and town area (or part)': '360',
		'state> new england city and town area> place': '361',
		'state> new england city and town area> county (or part)': '362',
		'state> new england city and town area> county> county subdivision': '363',
		'state> new england city and town area> necta division (or part)': '364',
		'state> new england city and town area> necta division> county (or part)': '365',
		'state> new england city and town area> necta division> county> county subdivision': '366',
		'urban area': '400',
		'urban area> state': '410',
		'urban area> state> county': '430',
		'state> congressional district': '500',
		'state> congressional district> county': '510',
		'state> congressional district> county> tract': '511',
		'state> congressional district> county> county subdivision': '521',
		'state> congressional district> place': '531',
		'state> congressional district> american indian area/alaska native area/hawaiian home land': '550',
		'state> congressional district> alaska native regional corporation': '560',
		'state> state legislative district (upper chamber)': '610',
		'state> state legislative district (upper chamber)> county': '612',
		'state> state legislative district (lower chamber)': '620',
		'state> state legislative district (lower chamber)> county (or part)': '622',
		'state> public use microdata area': '795',
		'zip code tabulation area': '860',
		'state> zip code tabulation area (or part)': '871',
		'state> school district (elementary)': '950',
		'state> school district (secondary)': '960',
		'state> school district (unified)': '970',
	}

	def __init__(self, geo, name=''):
		self.geo = tuple(geo)
		self.name = name

	def __eq__(self, other):
		return self.geo == other.geo

	def __hash__(self):
		return hash(self.geo)

	def __repr__(self):
		if self.name == '':
			return'censusgeo({0})'.format(repr(self.geo))
		else:
			return "censusgeo({0}, {1})".format(repr(self.geo), repr(self.name))

	def __str__(self):
		if self.name == '':
			return 'Summary level: ' + self.sumlevel() + ', ' + '> '.join([geo[0]+':'+geo[1] for geo in self.geo])
		else:
			return self.name + ': Summary level: ' + self.sumlevel() + ', ' + '> '.join([geo[0]+':'+geo[1] for geo in self.geo])

	def params(self):
		"""Geographic parameters of this object.

		Returns:
			tuple: Tuple representing the geography hierarchy. Can be used as argument in creating new censusgeo object.

		Examples::

			g = censusdata.censusgeo([('state', '06'), ('place', '53000')])
			g.params() # returns (('state', '06'), ('place', '53000'))
		"""
		return self.geo

	def hierarchy(self):
		"""Geography hierarchy for the geographic level of this object.

		Returns:
			str: String representing the geography hierarchy (e.g., 'state> county')."""
		return '> '.join([geo[0] for geo in self.geo])

	def sumlevel(self):
		"""Summary level code for the geographic level of this object.

		Returns:
			str: String representing the summary level code for this object's geographic level, e.g., '050' for 'state> county'."""
		return self.sumleveldict.get(self.hierarchy(), 'unknown')

	def request(self):
		"""Generate geographic parameters for Census API request.

		Returns:
			dict: Dictionary with appropriate 'for' and, if needed, 'in' parameters for Census API request."""
		nospacegeo = [(geo[0].replace(' ', '+'), geo[1]) for geo in self.geo]
		if len(nospacegeo) > 1:
			result = {'for': ':'.join(nospacegeo[-1]),
			'in': '+'.join([':'.join(geo) for geo in nospacegeo[:-1]])}
		else:
			result = {'for': ':'.join(nospacegeo[0])}
		return result

