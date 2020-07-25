"""
Test censusdata.censusgeo class for representing geographies.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import censusdata

class TestCensusgeo(unittest.TestCase):

	def setUp(self):
		self.countygeo = censusdata.censusgeo([('state', '17'), ('county', '031')])
		self.placecountygeo = censusdata.censusgeo([('state', '17'), ('place', '55555'), ('county (or part)', '*')])
		self.placegeo = censusdata.censusgeo([('state', '06'), ('place', '53000')], 'Oakland city, California')
		self.blockg = censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')])
		self.msa = censusdata.censusgeo((('metropolitan statistical area/micropolitan statistical area', '16980'),))

	def test_request_for(self):
		self.assertEqual(self.countygeo.request()['for'], 'county:031')
		self.assertEqual(self.placecountygeo.request()['for'], 'county+(or+part):*')
		self.assertEqual(self.blockg.request()['for'], 'block+group:2')
		self.assertEqual(self.msa.request()['for'], 'metropolitan+statistical+area/micropolitan+statistical+area:16980')

	def test_request_in(self):
		self.assertEqual(self.countygeo.request()['in'], 'state:17')
		self.assertEqual(self.placecountygeo.request()['in'], 'state:17+place:55555')
		self.assertEqual(self.blockg.request()['in'], 'state:17+county:031+tract:350100')
		self.assertTrue('in' not in self.msa.request().keys())

	def test_sumlevel(self):
		self.assertEqual(self.countygeo.sumlevel(), '050')
		self.assertEqual(self.placecountygeo.sumlevel(), '155')
		self.assertEqual(self.blockg.sumlevel(), '150')
		self.assertEqual(self.msa.sumlevel(), '310')

	def test_params(self):
		self.assertEqual(self.countygeo.params(), (('state', '17'), ('county', '031')))
		self.assertEqual(self.placecountygeo.params(), (('state', '17'), ('place', '55555'), ('county (or part)', '*')))
		self.assertEqual(self.placegeo.params(), (('state', '06'), ('place', '53000')))
		self.assertEqual(self.blockg.params(), (('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')))
		self.assertEqual(self.msa.params(), (('metropolitan statistical area/micropolitan statistical area', '16980'),))

	def test_hierarchy(self):
		self.assertEqual(self.countygeo.hierarchy(), 'state> county')
		self.assertEqual(self.placecountygeo.hierarchy(), 'state> place> county (or part)')
		self.assertEqual(self.blockg.hierarchy(), 'state> county> tract> block group')
		self.assertEqual(self.msa.hierarchy(), 'metropolitan statistical area/micropolitan statistical area')

	def test_eq(self):
		self.assertEqual(censusdata.censusgeo([('state', '17'), ('county', '*')]), censusdata.censusgeo([('state', '17'), ('county', '*')]))

	def test_repr(self):
		self.assertEqual(repr(self.countygeo), str("censusgeo((({0[0]}, {0[1]}), ({0[2]}, {0[3]})))".format([repr(s) for s in ['state', '17', 'county', '031']])))
		self.assertEqual(repr(self.placecountygeo), str("censusgeo((({0[0]}, {0[1]}), ({0[2]}, {0[3]}), ({0[4]}, {0[5]})))".format([repr(s) for s in ['state', '17', 'place', '55555', 'county (or part)', '*']])))
		self.assertEqual(repr(self.placegeo), str("censusgeo((({0[0]}, {0[1]}), ({0[2]}, {0[3]})), {0[4]})".format([repr(s) for s in ['state', '06', 'place', '53000', 'Oakland city, California']])))
		self.assertEqual(repr(self.blockg), str("censusgeo((({0[0]}, {0[1]}), ({0[2]}, {0[3]}), ({0[4]}, {0[5]}), ({0[6]}, {0[7]})))".format([repr(s) for s in ['state', '17', 'county', '031', 'tract', '350100', 'block group', '2']])))
		self.assertEqual(repr(self.msa), str("censusgeo((({0[0]}, {0[1]}),))".format([repr(s) for s in ['metropolitan statistical area/micropolitan statistical area', '16980']])))

	def test_str(self):
		self.assertEqual(str(self.countygeo), 'Summary level: 050, state:17> county:031')
		self.assertEqual(str(self.placecountygeo), 'Summary level: 155, state:17> place:55555> county (or part):*')
		self.assertEqual(str(self.placegeo), 'Oakland city, California: Summary level: 160, state:06> place:53000')
		self.assertEqual(str(self.blockg), 'Summary level: 150, state:17> county:031> tract:350100> block group:2')
		self.assertEqual(str(self.msa), 'Summary level: 310, metropolitan statistical area/micropolitan statistical area:16980')


if __name__ == '__main__':
	unittest.main()

