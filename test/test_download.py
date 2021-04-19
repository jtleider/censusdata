"""
Test downloading data from Census API.
"""

from __future__ import absolute_import, division, print_function, unicode_literals

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import censusdata
import unittest
import pandas as pd
from pandas.util.testing import assert_frame_equal

class TestDownload(unittest.TestCase):

	def test_raw_download_state(self):
		self.assertEqual(censusdata._download('acs5', 2015, {'get': 'NAME,B01001_001E', 'for': 'state:17'}),
			{'NAME': ['Illinois'], 'B01001_001E': ['12873761'], 'state': ['17']})

	def test_raw_download_place(self):
		self.assertEqual(censusdata._download('acs5', 2015, {'get': 'NAME,B01001_001E', 'for': 'place:53000', 'in': 'state:06'}),
			{'NAME': ['Oakland city, California'], 'B01001_001E': ['408073'], 'state': ['06'], 'place': ['53000']})

	def test_geographies_state(self):
		for year in range(2009, 2019+1):
			self.assertEqual(censusdata.geographies(censusdata.censusgeo([('state', '*')]), 'acs5', year),
				{
				'Alaska': censusdata.censusgeo([('state', '02')]),
				'Alabama': censusdata.censusgeo([('state', '01')]),
				'Arkansas': censusdata.censusgeo([('state', '05')]),
				'Arizona': censusdata.censusgeo([('state', '04')]),
				'California': censusdata.censusgeo([('state', '06')]),
				'Colorado': censusdata.censusgeo([('state', '08')]),
				'Connecticut': censusdata.censusgeo([('state', '09')]),
				'District of Columbia': censusdata.censusgeo([('state', '11')]),
				'Delaware': censusdata.censusgeo([('state', '10')]),
				'Florida': censusdata.censusgeo([('state', '12')]),
				'Georgia': censusdata.censusgeo([('state', '13')]),
				'Hawaii': censusdata.censusgeo([('state', '15')]),
				'Iowa': censusdata.censusgeo([('state', '19')]),
				'Idaho': censusdata.censusgeo([('state', '16')]),
				'Illinois': censusdata.censusgeo([('state', '17')]),
				'Indiana': censusdata.censusgeo([('state', '18')]),
				'Kansas': censusdata.censusgeo([('state', '20')]),
				'Kentucky': censusdata.censusgeo([('state', '21')]),
				'Louisiana': censusdata.censusgeo([('state', '22')]),
				'Massachusetts': censusdata.censusgeo([('state', '25')]),
				'Maryland': censusdata.censusgeo([('state', '24')]),
				'Maine': censusdata.censusgeo([('state', '23')]),
				'Michigan': censusdata.censusgeo([('state', '26')]),
				'Minnesota': censusdata.censusgeo([('state', '27')]),
				'Missouri': censusdata.censusgeo([('state', '29')]),
				'Mississippi': censusdata.censusgeo([('state', '28')]),
				'Montana': censusdata.censusgeo([('state', '30')]),
				'North Carolina': censusdata.censusgeo([('state', '37')]),
				'North Dakota': censusdata.censusgeo([('state', '38')]),
				'Nebraska': censusdata.censusgeo([('state', '31')]),
				'New Hampshire': censusdata.censusgeo([('state', '33')]),
				'New Jersey': censusdata.censusgeo([('state', '34')]),
				'New Mexico': censusdata.censusgeo([('state', '35')]),
				'Nevada': censusdata.censusgeo([('state', '32')]),
				'New York': censusdata.censusgeo([('state', '36')]),
				'Ohio': censusdata.censusgeo([('state', '39')]),
				'Oklahoma': censusdata.censusgeo([('state', '40')]),
				'Oregon': censusdata.censusgeo([('state', '41')]),
				'Pennsylvania': censusdata.censusgeo([('state', '42')]),
				'Puerto Rico': censusdata.censusgeo([('state', '72')]),
				'Rhode Island': censusdata.censusgeo([('state', '44')]),
				'South Carolina': censusdata.censusgeo([('state', '45')]),
				'South Dakota': censusdata.censusgeo([('state', '46')]),
				'Tennessee': censusdata.censusgeo([('state', '47')]),
				'Texas': censusdata.censusgeo([('state', '48')]),
				'Utah': censusdata.censusgeo([('state', '49')]),
				'Virginia': censusdata.censusgeo([('state', '51')]),
				'Vermont': censusdata.censusgeo([('state', '50')]),
				'Washington': censusdata.censusgeo([('state', '53')]),
				'Wisconsin': censusdata.censusgeo([('state', '55')]),
				'West Virginia': censusdata.censusgeo([('state', '54')]),
				'Wyoming': censusdata.censusgeo([('state', '56')]),
				})

	def test_geographies_county(self):
		self.assertEqual(censusdata.geographies(censusdata.censusgeo([('state', '15'), ('county', '*')]), 'acs5', 2015), 
			{'Hawaii County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '001')]),
			'Honolulu County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '003')]),
			'Kalawao County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '005')]),
			'Kauai County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '007')]),
			'Maui County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '009')]),})
		self.assertEqual(censusdata.geographies(censusdata.censusgeo([('state', '15'), ('county', '*')]), 'acs1', 2015), 
			{'Hawaii County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '001')]),
			'Honolulu County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '003')]),
			'Kauai County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '007')]),
			'Maui County, Hawaii': censusdata.censusgeo([('state', '15'), ('county', '009')]),})

	def test_download_acs5_2019(self):
		assert_frame_equal(censusdata.download('acs5', 2019, censusdata.censusgeo([('state', '06'), ('place', '53000')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 425097, 'B01002_001E': 36.5, 'B19013_001E': 73692}, [censusdata.censusgeo([('state', '06'), ('place', '53000')], 'Oakland city, California')]))
		assert_frame_equal(censusdata.download('acs5', 2019, censusdata.censusgeo([('state', '15'), ('county', '*')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': [199459, 984821, 71769, 66, 165979,], 'B01002_001E': [42.7, 37.9, 42.6, 57.4, 41.2], 'B19013_001E': [62409, 85857, 83554, 69375, 80948]}, 
				[censusdata.censusgeo([('state', '15'), ('county', '001')], 'Hawaii County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '003')], 'Honolulu County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '007')], 'Kauai County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '005')], 'Kalawao County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '009')], 'Maui County, Hawaii'),
				]))
		assert_frame_equal(censusdata.download('acs5', 2019, censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 1586, 'B19013_001E': 45313}, [censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')], 'Block Group 2, Census Tract 3501, Cook County, Illinois')]))
		assert_frame_equal(censusdata.download('acs5', 2019, censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 9508605, 'B19013_001E': 71770}, [censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')], 'Chicago-Naperville-Elgin, IL-IN-WI Metro Area')]))
		assert_frame_equal(censusdata.download('acs5', 2019, censusdata.censusgeo([('state', '06')]), ['DP03_0021PE'], tabletype='profile'),
			pd.DataFrame({'DP03_0021PE': 5.1}, [censusdata.censusgeo([('state', '06')], 'California')]))
		assert_frame_equal(censusdata.download('acs5', 2019, censusdata.censusgeo([('state', '06')]), ['C24010_001E'], tabletype='detail'),
			pd.DataFrame({'C24010_001E': 18591241}, [censusdata.censusgeo([('state', '06')], 'California')]))

	def test_download_acs5_2018(self):
		assert_frame_equal(censusdata.download('acs5', 2018, censusdata.censusgeo([('state', '06'), ('place', '53000')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 421042, 'B01002_001E': 36.5, 'B19013_001E': 68442}, [censusdata.censusgeo([('state', '06'), ('place', '53000')], 'Oakland city, California')]))
		assert_frame_equal(censusdata.download('acs5', 2018, censusdata.censusgeo([('state', '15'), ('county', '*')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': [197658, 987638, 71377, 75, 165281], 'B01002_001E': [42.3, 37.6, 42.4, 57.1, 41.1], 'B19013_001E': [59297, 82906, 78482, 61875, 77117]}, 
				[censusdata.censusgeo([('state', '15'), ('county', '001')], 'Hawaii County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '003')], 'Honolulu County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '007')], 'Kauai County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '005')], 'Kalawao County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '009')], 'Maui County, Hawaii'),]))
		assert_frame_equal(censusdata.download('acs5', 2018, censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 1433, 'B19013_001E': 33750}, [censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')], 'Block Group 2, Census Tract 3501, Cook County, Illinois')]))
		assert_frame_equal(censusdata.download('acs5', 2018, censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 9536428, 'B19013_001E': 68715}, [censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')], 'Chicago-Naperville-Elgin, IL-IN-WI Metro Area')]))
		assert_frame_equal(censusdata.download('acs5', 2018, censusdata.censusgeo([('state', '06')]), ['DP03_0021PE'], tabletype='profile'),
			pd.DataFrame({'DP03_0021PE': 5.1}, [censusdata.censusgeo([('state', '06')], 'California')]))
		assert_frame_equal(censusdata.download('acs5', 2018, censusdata.censusgeo([('state', '06')]), ['C24010_001E'], tabletype='detail'),
			pd.DataFrame({'C24010_001E': 18309012}, [censusdata.censusgeo([('state', '06')], 'California')]))

	def test_download_acs5_2017(self):
		assert_frame_equal(censusdata.download('acs5', 2017, censusdata.censusgeo([('state', '06'), ('place', '53000')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 417442, 'B01002_001E': 36.4, 'B19013_001E': 63251}, [censusdata.censusgeo([('state', '06'), ('place', '53000')], 'Oakland city, California')]))
		assert_frame_equal(censusdata.download('acs5', 2017, censusdata.censusgeo([('state', '15'), ('county', '*')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': [196325, 990060, 164094, 71093, 86], 'B01002_001E': [42.1, 37.6, 40.9, 42.1, 57.6], 'B19013_001E': [56395, 80078, 72762, 72330, 61750]}, 
				[censusdata.censusgeo([('state', '15'), ('county', '001')], 'Hawaii County, Hawaii'), censusdata.censusgeo([('state', '15'), ('county', '003')], 'Honolulu County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '009')], 'Maui County, Hawaii'), censusdata.censusgeo([('state', '15'), ('county', '007')], 'Kauai County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '005')], 'Kalawao County, Hawaii'),]))
		assert_frame_equal(censusdata.download('acs5', 2017, censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 1476, 'B19013_001E': 41638}, [censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')], 'Block Group 2, Census Tract 3501, Cook County, Illinois')]))
		assert_frame_equal(censusdata.download('acs5', 2017, censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 9549229, 'B19013_001E': 65757}, [censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')], 'Chicago-Naperville-Elgin, IL-IN-WI Metro Area')]))
		assert_frame_equal(censusdata.download('acs5', 2017, censusdata.censusgeo([('state', '06')]), ['DP03_0021PE'], tabletype='profile'),
			pd.DataFrame({'DP03_0021PE': 5.2}, [censusdata.censusgeo([('state', '06')], 'California')]))

	def test_download_acs5_2016(self):
		assert_frame_equal(censusdata.download('acs5', 2016, censusdata.censusgeo([('state', '06'), ('place', '53000')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 412040, 'B01002_001E': 36.2, 'B19013_001E': 57778}, [censusdata.censusgeo([('state', '06'), ('place', '53000')], 'Oakland city, California')]))
		assert_frame_equal(censusdata.download('acs5', 2016, censusdata.censusgeo([('state', '15'), ('county', '*')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': [986999, 162456, 91, 193680, 70447], 'B01002_001E': [37.4, 40.5, 56.5, 41.8, 42.0], 'B19013_001E': [77161, 68777, 65625, 53936, 68224]}, 
				[
				censusdata.censusgeo([('state', '15'), ('county', '003')], 'Honolulu County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '009')], 'Maui County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '005')], 'Kalawao County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '001')], 'Hawaii County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '007')], 'Kauai County, Hawaii'),
				]))
		assert_frame_equal(censusdata.download('acs5', 2016, censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 1374, 'B19013_001E': 44044}, [censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')], 'Block Group 2, Census Tract 3501, Cook County, Illinois')]))
		assert_frame_equal(censusdata.download('acs5', 2016, censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 9528396, 'B19013_001E': 63327}, [censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')], 'Chicago-Naperville-Elgin, IL-IN-WI Metro Area')]))
		assert_frame_equal(censusdata.download('acs5', 2016, censusdata.censusgeo([('state', '06')]), ['DP03_0021PE'], tabletype='profile'),
			pd.DataFrame({'DP03_0021PE': 5.2}, [censusdata.censusgeo([('state', '06')], 'California')]))

	def test_download_acs5_2015(self):
		assert_frame_equal(censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '06'), ('place', '53000')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 408073, 'B01002_001E': 36.3, 'B19013_001E': 54618}, [censusdata.censusgeo([('state', '06'), ('place', '53000')], 'Oakland city, California')]))
		assert_frame_equal(censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '15'), ('county', '*')]), ['B01001_001E', 'B01002_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': [191482, 69691, 984178, 160863, 85], 'B01002_001E': [41.1, 41.6, 36.9, 40, 51.9], 'B19013_001E': [52108, 65101, 74460, 66476, 66250]}, 
				[censusdata.censusgeo([('state', '15'), ('county', '001')], 'Hawaii County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '007')], 'Kauai County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '003')], 'Honolulu County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '009')], 'Maui County, Hawaii'),
				censusdata.censusgeo([('state', '15'), ('county', '005')], 'Kalawao County, Hawaii'),]))
		assert_frame_equal(censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 1293, 'B19013_001E': 49375}, [censusdata.censusgeo([('state', '17'), ('county', '031'), ('tract', '350100'), ('block group', '2')], 'Block Group 2, Census Tract 3501, Cook County, Illinois')]))
		assert_frame_equal(censusdata.download('acs5', 2015, censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')]), ['B01001_001E', 'B19013_001E']),
			pd.DataFrame({'B01001_001E': 9534008, 'B19013_001E': 61828}, [censusdata.censusgeo([('metropolitan statistical area/micropolitan statistical area', '16980')], 'Chicago-Naperville-Elgin, IL-IN-WI Metro Area')]))
		assert_frame_equal(censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '06')]), ['DP03_0021PE'], tabletype='profile'),
			pd.DataFrame({'DP03_0021PE': 5.2}, [censusdata.censusgeo([('state', '06')], 'California')]))

	def test_download_acs5_200914(self):
		medhhinc = {2009: 55222, 2010: 55735, 2011: 56576, 2012: 56853, 2013: 56797, 2014: 57166}
		for year in range(2009, 2014+1):
			assert_frame_equal(censusdata.download('acs5', year, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
				pd.DataFrame({'B19013_001E': medhhinc[year]}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs5_zcta(self):
		str(censusdata.download('acs5', 2019, censusdata.censusgeo([('zip code tabulation area','*')]), ['B19013_001E']))

	def test_download_acs1_2019(self):
		assert_frame_equal(censusdata.download('acs1', 2019, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
			pd.DataFrame({'B19013_001E': 69187}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs1_2018(self):
		assert_frame_equal(censusdata.download('acs1', 2018, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
			pd.DataFrame({'B19013_001E': 65030}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs1_2017(self):
		assert_frame_equal(censusdata.download('acs1', 2017, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
			pd.DataFrame({'B19013_001E': 62992}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs1_2016(self):
		assert_frame_equal(censusdata.download('acs1', 2016, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
			pd.DataFrame({'B19013_001E': 60960}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs1_2015(self):
		assert_frame_equal(censusdata.download('acs1', 2015, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
			pd.DataFrame({'B19013_001E': 59588}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs1_201214(self):
		medhhinc = {2012: 55137, 2013: 56210, 2014: 57444}
		for year in range(2012, 2014+1):
			assert_frame_equal(censusdata.download('acs1', year, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
				pd.DataFrame({'B19013_001E': medhhinc[year]}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acsse(self):
		nocomputer = {2014: 731135, 2015: 658047, 2016: 522736, 2017: 464053, 2018: 414688, 2019: 378926}
		for year in range(2014, 2019+1):
			assert_frame_equal(censusdata.download('acsse', year, censusdata.censusgeo([('state', '17')]), ['K202801_006E']),
				pd.DataFrame({'K202801_006E': nocomputer[year]}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs3_detail(self):
		medhhinc = {2012: 55231, 2013: 55799}
		for year in medhhinc:
			assert_frame_equal(censusdata.download('acs3', year, censusdata.censusgeo([('state', '17')]), ['B19013_001E']),
				pd.DataFrame({'B19013_001E': medhhinc[year]}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_acs3_profile(self):
		insured = {2012: 78.3, 2013: 78.5}
		for year in insured:
			assert_frame_equal(censusdata.download('acs3', year, censusdata.censusgeo([('state', '17')]), ['DP03_0115PE'], tabletype='profile'),
				pd.DataFrame({'DP03_0115PE': insured[year]}, [censusdata.censusgeo([('state', '17')], 'Illinois')]))

	def test_download_sf1_2010(self):
		assert_frame_equal(censusdata.download('sf1', 2010, censusdata.censusgeo([('state', '17'), ('place', '14000')]), ['P001001']),
			pd.DataFrame({'P001001': 2695598}, [censusdata.censusgeo([('state', '17'), ('place', '14000')])]))

	def test_download_error_variable(self):
		self.assertRaises(ValueError, censusdata.download, 'acs5', 2015, censusdata.censusgeo([('state', '06'), ('place', '53000')]), ['B19013_010E'])

	def test_download_error_tabletype(self):
		self.assertRaises(ValueError, censusdata.download, 'acs5', 2015, censusdata.censusgeo([('state', '06')]), ['B19013_001E'], tabletype='cdetail')

	def test_download_gt50_vars(self):
		vars = ['DP05_{:04}PE'.format(i) for i in range(1, 84+1)]
		data = censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '06')]), vars, tabletype='profile')
		expected = pd.DataFrame({'DP05_0001PE': 38421464, 'DP05_0002PE': 49.7, 'DP05_0003PE': 50.3, 'DP05_0004PE': 6.5, 'DP05_0005PE': 6.6,
			'DP05_0006PE': 6.6, 'DP05_0007PE': 6.9, 'DP05_0008PE': 7.6, 'DP05_0009PE': 14.6, 'DP05_0010PE': 13.5, 'DP05_0011PE': 13.7,
			'DP05_0012PE': 6.2, 'DP05_0013PE': 5.3, 'DP05_0014PE': 7.0, 'DP05_0015PE': 3.8, 'DP05_0016PE': 1.7, 'DP05_0017PE': -888888888,
			'DP05_0018PE': 76.1, 'DP05_0019PE': 71.7, 'DP05_0020PE': 15.5, 'DP05_0021PE': 12.5, 'DP05_0022PE': 29247121, 'DP05_0023PE': 49.2,
			'DP05_0024PE': 50.8, 'DP05_0025PE': 4797320, 'DP05_0026PE': 44.0, 'DP05_0027PE': 56.0, 'DP05_0028PE': 38421464, 'DP05_0029PE': 95.5,
			'DP05_0030PE': 4.5, 'DP05_0031PE': 95.5, 'DP05_0032PE': 61.8, 'DP05_0033PE': 5.9, 'DP05_0034PE': 0.7, 'DP05_0035PE': 0.1, 'DP05_0036PE': 0.0,
			'DP05_0037PE': 0.0, 'DP05_0038PE': 0.0, 'DP05_0039PE': 13.7, 'DP05_0040PE': 1.7, 'DP05_0041PE': 3.6, 'DP05_0042PE': 3.2,
			'DP05_0043PE': 0.7, 'DP05_0044PE': 1.2, 'DP05_0045PE': 1.6, 'DP05_0046PE': 1.6, 'DP05_0047PE': 0.4, 'DP05_0048PE': 0.1, 'DP05_0049PE': 0.1,
			'DP05_0050PE': 0.1, 'DP05_0051PE': 0.2, 'DP05_0052PE': 12.9, 'DP05_0053PE': 4.5, 'DP05_0054PE': 0.6, 'DP05_0055PE': 0.7, 'DP05_0056PE': 1.3,
			'DP05_0057PE': 0.1, 'DP05_0058PE': 38421464, 'DP05_0059PE': 65.5, 'DP05_0060PE': 7.1, 'DP05_0061PE': 1.9, 'DP05_0062PE': 15.6,
			'DP05_0063PE': 0.8, 'DP05_0064PE': 14.1, 'DP05_0065PE': 38421464, 'DP05_0066PE': 38.4, 'DP05_0067PE': 31.9, 'DP05_0068PE': 0.5,
			'DP05_0069PE': 0.2, 'DP05_0070PE': 5.7, 'DP05_0071PE': 61.6, 'DP05_0072PE': 38.7, 'DP05_0073PE': 5.6, 'DP05_0074PE': 0.4,
			'DP05_0075PE': 13.5, 'DP05_0076PE': 0.4, 'DP05_0077PE': 0.2, 'DP05_0078PE': 2.8, 'DP05_0079PE': 0.1, 'DP05_0080PE': 2.7,
			'DP05_0081PE': -888888888, 'DP05_0082PE': 24280349, 'DP05_0083PE': 49.0, 'DP05_0084PE': 51.0},
			[censusdata.censusgeo([('state', '06')])])
		assert_frame_equal(data, expected)

if __name__ == '__main__':
	unittest.main()

