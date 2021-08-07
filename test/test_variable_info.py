"""" Test showing information on variables from Census API.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import censusdata
import unittest
from collections import OrderedDict
import io
import textwrap
import re

class TestVariableInfo(unittest.TestCase):

	def test_censusvar_acs5(self):
		expected = {'B01001_001E': ['B01001.  Sex by Age', 'Total:', 'int'],
			'B01002_001E': ['B01002.  Median Age by Sex', 'Median age --!!Total:', 'int'],
			'B19013_001E': ['B19013.  Median Household Income',
				'Median household income in the past 12 months (in 2009 inflation-adjusted dollars)', 'int']}
		self.assertEqual(censusdata.censusvar('acs5', 2009, ['B01001_001E', 'B01002_001E', 'B19013_001E']), expected)
		for year in range(2010, 2019+1):
			concepts = ['SEX BY AGE', 'MEDIAN AGE BY SEX', 'MEDIAN HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN {0} INFLATION-ADJUSTED DOLLARS)'.format(year)]
			types = ['int', 'float', 'int']
			inflation = 'inflation'
			if year == 2014 or year == 2015: inflation = 'Inflation'
			median_age_label = 'Estimate!!Median age!!Total'
			if year == 2017: median_age_label = 'Estimate!!Median age --!!Total'
			if year == 2018: median_age_label = 'Estimate!!Median age --!!Total'
			if year == 2019: median_age_label = 'Estimate!!Median age --!!Total:'
			total_label = 'Estimate!!Total'
			if year == 2019: total_label = 'Estimate!!Total:'
			expected = {'B01001_001E': [concepts[0], total_label, types[0]],
				'B01002_001E': [concepts[1], median_age_label, types[1]],
				'B19013_001E': [concepts[2],
					'Estimate!!Median household income in the past 12 months (in {0} {1}-adjusted dollars)'.format(year, inflation), types[2]]}
			self.assertEqual(censusdata.censusvar('acs5', year, ['B01001_001E', 'B01002_001E', 'B19013_001E']), expected)
		expected = {'C24010_001E': ['SEX BY OCCUPATION FOR THE CIVILIAN EMPLOYED POPULATION 16 YEARS AND OVER',
				'Estimate!!Total', 'int']}
		self.assertEqual(censusdata.censusvar('acs5', 2018, ['C24010_001E']), expected)
		expected = {'C24010_001E': ['SEX BY OCCUPATION FOR THE CIVILIAN EMPLOYED POPULATION 16 YEARS AND OVER',
				'Estimate!!Total:', 'int']}
		self.assertEqual(censusdata.censusvar('acs5', 2019, ['C24010_001E']), expected)

	def test_censusvar_acs1(self):
		censusdata.censusvar('acs1', 2015, ['S0101_C02_001E', 'DP03_0021PE', 'CP02_2012_030E'])
		censusdata.censusvar('acs1', 2016, ['S0101_C02_001E', 'DP03_0021PE', 'CP02_2012_030E'])
		censusdata.censusvar('acs1', 2017, ['S0101_C02_001E', 'DP03_0021PE', 'CP02_2013_030E'])
		censusdata.censusvar('acs1', 2018, ['S0101_C02_001E', 'DP03_0021PE', 'CP02_2014_030E'])
		censusdata.censusvar('acs1', 2019, ['S0101_C02_001E', 'DP03_0021PE', 'CP02_2015_030E'])

	def test_censusvar_acsse(self):
		for year in range(2014, 2019+1):
			label = 'Estimate!!Total!!No computer'
			if year == 2019: label = 'Estimate!!Total:!!No computer'
			expected = {'K202801_006E': ['PRESENCE OF A COMPUTER AND TYPE OF INTERNET SUBSCRIPTION IN HOUSEHOLD', label, 'int']}
			self.assertEqual(censusdata.censusvar('acsse', year, ['K202801_006E']), expected)

	def test_censusvar_acs3(self):
		for year in range(2013, 2013+1):
			expected = {'B19013_001E': ['MEDIAN HOUSEHOLD INCOME IN THE PAST 12 MONTHS (IN {0} INFLATION-ADJUSTED DOLLARS)'.format(year),
				'Estimate!!Median household income in the past 12 months (in {0} inflation-adjusted dollars)'.format(year), 'int']}
			self.assertEqual(censusdata.censusvar('acs3', year, ['B19013_001E']), expected)

	def test_censusvar_sf1(self):
		self.assertEqual(censusdata.censusvar('sf1', 2010, ['P001001']),
			{'P001001': ['TOTAL POPULATION', 'Total', '']})

	def test_unknownvar(self):
		self.assertRaises(ValueError, censusdata.censusvar, 'acs5', 2015, ['B19013_010E'])

	def test_censustable_acs1_201219_detail(self):
		for year in range(2012, 2019+1):
			censusdata.censustable('acs1', year, 'B23025')

	def test_censustable_acs5_2015_detail(self):
		censusdata.censustable('acs5', 2015, 'B23025')

	def test_censustable_acs5_2016_detail(self):
		expected = OrderedDict()
		expected['B23025_001E'] = {'label': 'Estimate!!Total', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_002E'] = {'label': 'Estimate!!Total!!In labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_003E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_004E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force!!Employed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_005E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force!!Unemployed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_006E'] = {'label': 'Estimate!!Total!!In labor force!!Armed Forces', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_007E'] = {'label': 'Estimate!!Total!!Not in labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		self.assertEqual(censusdata.censustable('acs5', 2016, 'B23025'), expected)

	def test_censustable_acs5_2017_detail(self):
		expected = OrderedDict()
		expected['B23025_001E'] = {'label': 'Estimate!!Total', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_002E'] = {'label': 'Estimate!!Total!!In labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_003E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_004E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force!!Employed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_005E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force!!Unemployed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_006E'] = {'label': 'Estimate!!Total!!In labor force!!Armed Forces', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_007E'] = {'label': 'Estimate!!Total!!Not in labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		self.assertEqual(censusdata.censustable('acs5', 2017, 'B23025'), expected)

	def test_censustable_acs5_2018_detail(self):
		expected = OrderedDict()
		expected['B23025_001E'] = {'label': 'Estimate!!Total', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_002E'] = {'label': 'Estimate!!Total!!In labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_003E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_004E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force!!Employed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_005E'] = {'label': 'Estimate!!Total!!In labor force!!Civilian labor force!!Unemployed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_006E'] = {'label': 'Estimate!!Total!!In labor force!!Armed Forces', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_007E'] = {'label': 'Estimate!!Total!!Not in labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		self.assertEqual(censusdata.censustable('acs5', 2018, 'B23025'), expected)
		expected = OrderedDict()
		expected['C15010_001E'] = {'label': 'Estimate!!Total', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_002E'] = {'label': 'Estimate!!Total!!Science and Engineering', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_003E'] = {'label': 'Estimate!!Total!!Science and Engineering Related Fields', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_004E'] = {'label': 'Estimate!!Total!!Business', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_005E'] = {'label': 'Estimate!!Total!!Education', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_006E'] = {'label': 'Estimate!!Total!!Arts, Humanities and Other', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		self.assertEqual(censusdata.censustable('acs5', 2018, 'C15010'), expected)

	def test_censustable_acs5_2019_detail(self):
		expected = OrderedDict()
		expected['B23025_001E'] = {'label': 'Estimate!!Total:', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_002E'] = {'label': 'Estimate!!Total:!!In labor force:', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_003E'] = {'label': 'Estimate!!Total:!!In labor force:!!Civilian labor force:', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_004E'] = {'label': 'Estimate!!Total:!!In labor force:!!Civilian labor force:!!Employed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_005E'] = {'label': 'Estimate!!Total:!!In labor force:!!Civilian labor force:!!Unemployed', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_006E'] = {'label': 'Estimate!!Total:!!In labor force:!!Armed Forces', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		expected['B23025_007E'] = {'label': 'Estimate!!Total:!!Not in labor force', 'concept': 'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER', 'predicateType': 'int'}
		self.assertEqual(censusdata.censustable('acs5', 2019, 'B23025'), expected)
		expected = OrderedDict()
		expected['C15010_001E'] = {'label': 'Estimate!!Total:', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_002E'] = {'label': 'Estimate!!Total:!!Science and Engineering', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_003E'] = {'label': 'Estimate!!Total:!!Science and Engineering Related Fields', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_004E'] = {'label': 'Estimate!!Total:!!Business', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_005E'] = {'label': 'Estimate!!Total:!!Education', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		expected['C15010_006E'] = {'label': 'Estimate!!Total:!!Arts, Humanities and Other', 'concept': "FIELD OF BACHELOR'S DEGREE FOR FIRST MAJOR FOR THE POPULATION 25 YEARS AND OVER", 'predicateType': 'int'}
		self.assertEqual(censusdata.censustable('acs5', 2019, 'C15010'), expected)

	def test_censustable_acs5_2015_subject(self):
		censusdata.censustable('acs5', 2015, 'S0101_C02')

	def test_censustable_acs5_2016_subject(self):
		censusdata.censustable('acs5', 2016, 'S0101_C02')

	def test_censustable_acs5_2017_subject(self):
		expected = OrderedDict()
		expected['S0101_C02_001E'] = {'label': 'Estimate!!Percent!!Total population', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_002E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!Under 5 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_003E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!5 to 9 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_004E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!10 to 14 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_005E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!15 to 19 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_006E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!20 to 24 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_007E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!25 to 29 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_008E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!30 to 34 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_009E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!35 to 39 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_010E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!40 to 44 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_011E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!45 to 49 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_012E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!50 to 54 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_013E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!55 to 59 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_014E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!60 to 64 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_015E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!65 to 69 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_016E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!70 to 74 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_017E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!75 to 79 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_018E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!80 to 84 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_019E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!85 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_020E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!5 to 14 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_021E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!15 to 17 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_022E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!Under 18 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_023E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!18 to 24 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_024E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!15 to 44 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_025E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!16 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_026E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!18 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_027E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!21 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_028E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!60 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_029E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!62 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_030E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!65 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_031E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!75 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_032E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Median age (years)', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_033E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_034E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Age dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_035E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Old-age dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_036E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Child dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_037E'] = {'label': 'Estimate!!Percent!!PERCENT ALLOCATED!!Sex', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_038E'] = {'label': 'Estimate!!Percent!!PERCENT ALLOCATED!!Age', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		self.assertEqual(censusdata.censustable('acs5', 2017, 'S0101_C02'), expected)

	def test_censustable_acs5_2018_subject(self):
		expected = OrderedDict()
		expected['S0101_C02_001E'] = {'label': 'Estimate!!Percent!!Total population', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_002E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!Under 5 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_003E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!5 to 9 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_004E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!10 to 14 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_005E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!15 to 19 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_006E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!20 to 24 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_007E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!25 to 29 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_008E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!30 to 34 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_009E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!35 to 39 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_010E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!40 to 44 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_011E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!45 to 49 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_012E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!50 to 54 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_013E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!55 to 59 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_014E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!60 to 64 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_015E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!65 to 69 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_016E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!70 to 74 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_017E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!75 to 79 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_018E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!80 to 84 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_019E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!85 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_020E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!5 to 14 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_021E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!15 to 17 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_022E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!Under 18 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_023E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!18 to 24 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_024E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!15 to 44 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_025E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!16 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_026E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!18 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_027E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!21 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_028E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!60 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_029E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!62 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_030E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!65 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_031E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!75 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_032E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Median age (years)', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_033E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_034E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Age dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_035E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Old-age dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_036E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Child dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_037E'] = {'label': 'Estimate!!Percent!!PERCENT ALLOCATED!!Sex', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_038E'] = {'label': 'Estimate!!Percent!!PERCENT ALLOCATED!!Age', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		self.assertEqual(censusdata.censustable('acs5', 2018, 'S0101_C02'), expected)

	def test_censustable_acs5_2019_subject(self):
		expected = OrderedDict()
		expected['S0101_C02_001E'] = {'label': 'Estimate!!Percent!!Total population', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_002E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!Under 5 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_003E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!5 to 9 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_004E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!10 to 14 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_005E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!15 to 19 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_006E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!20 to 24 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_007E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!25 to 29 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_008E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!30 to 34 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_009E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!35 to 39 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_010E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!40 to 44 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_011E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!45 to 49 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_012E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!50 to 54 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_013E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!55 to 59 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_014E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!60 to 64 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_015E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!65 to 69 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_016E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!70 to 74 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_017E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!75 to 79 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_018E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!80 to 84 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_019E'] = {'label': 'Estimate!!Percent!!Total population!!AGE!!85 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_020E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!5 to 14 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_021E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!15 to 17 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_022E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!Under 18 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_023E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!18 to 24 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_024E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!15 to 44 years', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_025E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!16 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_026E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!18 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_027E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!21 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_028E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!60 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_029E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!62 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_030E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!65 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_031E'] = {'label': 'Estimate!!Percent!!Total population!!SELECTED AGE CATEGORIES!!75 years and over', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_032E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Median age (years)', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_033E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Sex ratio (males per 100 females)', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_034E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Age dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_035E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Old-age dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_036E'] = {'label': 'Estimate!!Percent!!Total population!!SUMMARY INDICATORS!!Child dependency ratio', 'concept': 'AGE AND SEX', 'predicateType': 'int'}
		expected['S0101_C02_037E'] = {'label': 'Estimate!!Percent!!Total population!!PERCENT ALLOCATED!!Sex', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		expected['S0101_C02_038E'] = {'label': 'Estimate!!Percent!!Total population!!PERCENT ALLOCATED!!Age', 'concept': 'AGE AND SEX', 'predicateType': 'float'}
		self.assertEqual(censusdata.censustable('acs5', 2019, 'S0101_C02'), expected)

	def test_censustable_acs_subject_full(self):
		censusdata.censustable('acs5', 2018, 'S1810')

	def test_censustable_acsse(self):
		for year in range(2014, 2015+1):
			censusdata.censustable('acsse', year, 'K201601')
		for year in range(2016, 2018+1):
			censusdata.censustable('acsse', year, 'K201601')
		censusdata.censustable('acsse', 2019, 'K201601')

	def test_censustable_acs3(self):
		for year in range(2012, 2013+1):
			censusdata.censustable('acs3', year, 'B23025')

	def test_censustable_sf1(self):
		expected = OrderedDict()
		expected['P002001'] = {'label': 'Total', 'concept': 'URBAN AND RURAL', 'predicateType': 'int'}
		expected['P002002'] = {'label': 'Total!!Urban', 'concept': 'URBAN AND RURAL', 'predicateType': 'int'}
		expected['P002003'] = {'label': 'Total!!Urban!!Inside urbanized areas', 'concept': 'URBAN AND RURAL', 'predicateType': 'int'}
		expected['P002004'] = {'label': 'Total!!Urban!!Inside urban clusters', 'concept': 'URBAN AND RURAL', 'predicateType': 'int'}
		expected['P002005'] = {'label': 'Total!!Rural', 'concept': 'URBAN AND RURAL', 'predicateType': 'int'}
		expected['P002006'] = {'label': 'Total!!Not defined for this file', 'concept': 'URBAN AND RURAL', 'predicateType': 'int'}
		self.assertEqual(censusdata.censustable('sf1', 2010, 'P002'), expected)

	def test_unknowntable(self):
		self.assertRaises(ValueError, censusdata.censustable, 'acs5', 2015, 'B24444')

	def test_search(self):
		censusdata.search('acs5', 2015, 'concept', 'unweighted sample')
		censusdata.search('acs5', 2018, 'concept', 'SEX BY AGE')
		censusdata.search('acs5', 2015, 'concept',
		lambda value: re.search('unweighted sample', value, re.IGNORECASE) and re.search('housing', value, re.IGNORECASE))
		censusdata.search('sf1', 2010, 'concept', 'JUVENILE FACILITIES')
		censusdata.search('acsse', 2019, 'concept', 'SEX BY AGE')

	def test_printtable(self):
		testtable = censusdata.censustable('acs5', 2015, 'B19013')
		printedtable = io.StringIO()
		sys.stdout = printedtable
		censusdata.printtable(testtable)
		sys.stdout = sys.__stdout__
		self.assertEqual(printedtable.getvalue(), textwrap.dedent(
			'''\
			Variable     | Table                          | Label                                                    | Type 
			-------------------------------------------------------------------------------------------------------------------
			B19013_001E  | MEDIAN HOUSEHOLD INCOME IN THE | !! Estimate Median household income in the past 12 month | int  
			-------------------------------------------------------------------------------------------------------------------
			'''))
		printedtable.close()
		printedtable = io.StringIO()
		sys.stdout = printedtable
		censusdata.printtable(testtable, moe=True)
		sys.stdout = sys.__stdout__
		self.assertEqual(printedtable.getvalue(), textwrap.dedent(
			'''\
			Variable     | Table                          | Label                                                    | Type 
			-------------------------------------------------------------------------------------------------------------------
			B19013_001E  | MEDIAN HOUSEHOLD INCOME IN THE | !! Estimate Median household income in the past 12 month | int  
			-------------------------------------------------------------------------------------------------------------------
			'''))
		printedtable.close()


	def test_unknown_tabletype(self):
		self.assertRaises(ValueError, censusdata.censusvar, 'acs5', 2015, ['B19013_001E', 'D19013_002E'])
		self.assertRaises(ValueError, censusdata.censustable, 'acs5', 2015, 'C19013')
		self.assertRaises(ValueError, censusdata.search, 'acs5', 2015, 'concept', 'unweighted sample', tabletype='cdetail')


if __name__ == '__main__':
	unittest.main()

