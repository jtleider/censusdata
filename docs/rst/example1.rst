
Example 1: Downloading Block Group Data and Exporting to CSV
============================================================

As a first example, let’s suppose we’re interested in unemployment and
high school dropout rates for block groups in Cook County, Illinois,
which contains Chicago, IL.

We begin by importing the censusdata and pandas modules, and setting
some display options in pandas for nicer output:

.. code:: ipython3

    import pandas as pd
    import censusdata
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.precision', 2)

To download data, we need to identify the relevant tables containing the
variables of interest to us. One way to do this would be to refer to the
ACS documentation, in particular the Table Shells
(https://www.census.gov/programs-surveys/acs/technical-documentation/summary-file-documentation.html).
Alternatively, it is possible to do this from within Python.
``censusdata.search`` will search for given text patterns. The downside
to this is output can be voluminous, as in the following searches, as
ACS frequently provides a large number of different tabulations related
to a given topic area. Below, we limit the output to the relevant
variables:

.. code:: ipython3

    censusdata.search('acs5', 2015, 'label', 'unemploy')[80:90]




.. parsed-literal::

    [('B23024_023E',
      'POVERTY STATUS IN THE PAST 12 MONTHS BY DISABILITY STATUS BY EMPLOYMENT STATUS FOR THE POPULATION 20 TO 64 YEARS',
      'Estimate!!Total!!Income in the past 12 months at or above poverty level!!With a disability!!In labor force!!Civilian!!Unemployed'),
     ('B23024_030E',
      'POVERTY STATUS IN THE PAST 12 MONTHS BY DISABILITY STATUS BY EMPLOYMENT STATUS FOR THE POPULATION 20 TO 64 YEARS',
      'Estimate!!Total!!Income in the past 12 months at or above poverty level!!No disability!!In labor force!!Civilian!!Unemployed'),
     ('B23025_005E',
      'EMPLOYMENT STATUS FOR THE POPULATION 16 YEARS AND OVER',
      'Estimate!!Total!!In labor force!!Civilian labor force!!Unemployed'),
     ('B27011_014E',
      'HEALTH INSURANCE COVERAGE STATUS AND TYPE BY EMPLOYMENT STATUS BY AGE',
      'Estimate!!Total!!In labor force!!Unemployed'),
     ('B27011_015E',
      'HEALTH INSURANCE COVERAGE STATUS AND TYPE BY EMPLOYMENT STATUS BY AGE',
      'Estimate!!Total!!In labor force!!Unemployed!!18 to 64 years'),
     ('B27011_016E',
      'HEALTH INSURANCE COVERAGE STATUS AND TYPE BY EMPLOYMENT STATUS BY AGE',
      'Estimate!!Total!!In labor force!!Unemployed!!18 to 64 years!!With health insurance coverage'),
     ('B27011_017E',
      'HEALTH INSURANCE COVERAGE STATUS AND TYPE BY EMPLOYMENT STATUS BY AGE',
      'Estimate!!Total!!In labor force!!Unemployed!!18 to 64 years!!With health insurance coverage!!With private health insurance'),
     ('B27011_018E',
      'HEALTH INSURANCE COVERAGE STATUS AND TYPE BY EMPLOYMENT STATUS BY AGE',
      'Estimate!!Total!!In labor force!!Unemployed!!18 to 64 years!!With health insurance coverage!!With public coverage'),
     ('B27011_019E',
      'HEALTH INSURANCE COVERAGE STATUS AND TYPE BY EMPLOYMENT STATUS BY AGE',
      'Estimate!!Total!!In labor force!!Unemployed!!18 to 64 years!!No health insurance coverage'),
     ('B27011_020E',
      'HEALTH INSURANCE COVERAGE STATUS AND TYPE BY EMPLOYMENT STATUS BY AGE',
      'Estimate!!Total!!In labor force!!Unemployed!!65 years and over')]



.. code:: ipython3

    censusdata.search('acs5', 2015, 'concept', 'education')[350:400]




.. parsed-literal::

    [('B15002_020E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!No schooling completed'),
     ('B15002_021E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!Nursery to 4th grade'),
     ('B15002_022E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!5th and 6th grade'),
     ('B15002_023E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!7th and 8th grade'),
     ('B15002_024E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!9th grade'),
     ('B15002_025E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!10th grade'),
     ('B15002_026E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!11th grade'),
     ('B15002_027E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!12th grade, no diploma'),
     ('B15002_028E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!High school graduate (includes equivalency)'),
     ('B15002_029E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!Some college, less than 1 year'),
     ('B15002_030E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!Some college, 1 or more years, no degree'),
     ('B15002_031E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      "Estimate!!Total!!Female!!Associate's degree"),
     ('B15002_032E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      "Estimate!!Total!!Female!!Bachelor's degree"),
     ('B15002_033E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      "Estimate!!Total!!Female!!Master's degree"),
     ('B15002_034E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!Professional school degree'),
     ('B15002_035E',
      'SEX BY EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Female!!Doctorate degree'),
     ('B15003_001E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total'),
     ('B15003_002E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!No schooling completed'),
     ('B15003_003E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Nursery school'),
     ('B15003_004E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Kindergarten'),
     ('B15003_005E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!1st grade'),
     ('B15003_006E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!2nd grade'),
     ('B15003_007E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!3rd grade'),
     ('B15003_008E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!4th grade'),
     ('B15003_009E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!5th grade'),
     ('B15003_010E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!6th grade'),
     ('B15003_011E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!7th grade'),
     ('B15003_012E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!8th grade'),
     ('B15003_013E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!9th grade'),
     ('B15003_014E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!10th grade'),
     ('B15003_015E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!11th grade'),
     ('B15003_016E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!12th grade, no diploma'),
     ('B15003_017E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Regular high school diploma'),
     ('B15003_018E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!GED or alternative credential'),
     ('B15003_019E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Some college, less than 1 year'),
     ('B15003_020E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Some college, 1 or more years, no degree'),
     ('B15003_021E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      "Estimate!!Total!!Associate's degree"),
     ('B15003_022E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      "Estimate!!Total!!Bachelor's degree"),
     ('B15003_023E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      "Estimate!!Total!!Master's degree"),
     ('B15003_024E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Professional school degree'),
     ('B15003_025E',
      'EDUCATIONAL ATTAINMENT FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Doctorate degree'),
     ('B16010_001E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total'),
     ('B16010_002E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate'),
     ('B16010_003E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate!!In labor force'),
     ('B16010_004E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate!!In labor force!!Speak only English'),
     ('B16010_005E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate!!In labor force!!Speak Spanish'),
     ('B16010_006E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate!!In labor force!!Speak other Indo-European languages'),
     ('B16010_007E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate!!In labor force!!Speak Asian and Pacific Island languages'),
     ('B16010_008E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate!!In labor force!!Speak other languages'),
     ('B16010_009E',
      'EDUCATIONAL ATTAINMENT AND EMPLOYMENT STATUS BY LANGUAGE SPOKEN AT HOME FOR THE POPULATION 25 YEARS AND OVER',
      'Estimate!!Total!!Less than high school graduate!!Not in labor force')]



(Please note that searching Census variables and printing out a single
table rely on previously downloaded information from the Census API,
because otherwise every time we did this we would have to download data
for all variables.) Once we have identified a table of interest, we can
use ``censusdata.printtable`` to show all variables included in the
table:

.. code:: ipython3

    censusdata.printtable(censusdata.censustable('acs5', 2015, 'B23025'))


.. parsed-literal::

    Variable     | Table                          | Label                                                    | Type 
    -------------------------------------------------------------------------------------------------------------------
    B23025_001E  | EMPLOYMENT STATUS FOR THE POPU | !! Estimate Total                                        | int  
    B23025_002E  | EMPLOYMENT STATUS FOR THE POPU | !! !! Estimate Total In labor force                      | int  
    B23025_003E  | EMPLOYMENT STATUS FOR THE POPU | !! !! !! Estimate Total In labor force Civilian labor fo | int  
    B23025_004E  | EMPLOYMENT STATUS FOR THE POPU | !! !! !! !! Estimate Total In labor force Civilian labor | int  
    B23025_005E  | EMPLOYMENT STATUS FOR THE POPU | !! !! !! !! Estimate Total In labor force Civilian labor | int  
    B23025_006E  | EMPLOYMENT STATUS FOR THE POPU | !! !! !! Estimate Total In labor force Armed Forces      | int  
    B23025_007E  | EMPLOYMENT STATUS FOR THE POPU | !! !! Estimate Total Not in labor force                  | int  
    -------------------------------------------------------------------------------------------------------------------


.. code:: ipython3

    censusdata.printtable(censusdata.censustable('acs5', 2015, 'B15003'))


.. parsed-literal::

    Variable     | Table                          | Label                                                    | Type 
    -------------------------------------------------------------------------------------------------------------------
    B15003_001E  | EDUCATIONAL ATTAINMENT FOR THE | !! Estimate Total                                        | int  
    B15003_002E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total No schooling completed              | int  
    B15003_003E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Nursery school                      | int  
    B15003_004E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Kindergarten                        | int  
    B15003_005E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 1st grade                           | int  
    B15003_006E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 2nd grade                           | int  
    B15003_007E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 3rd grade                           | int  
    B15003_008E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 4th grade                           | int  
    B15003_009E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 5th grade                           | int  
    B15003_010E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 6th grade                           | int  
    B15003_011E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 7th grade                           | int  
    B15003_012E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 8th grade                           | int  
    B15003_013E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 9th grade                           | int  
    B15003_014E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 10th grade                          | int  
    B15003_015E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 11th grade                          | int  
    B15003_016E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total 12th grade, no diploma              | int  
    B15003_017E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Regular high school diploma         | int  
    B15003_018E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total GED or alternative credential       | int  
    B15003_019E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Some college, less than 1 year      | int  
    B15003_020E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Some college, 1 or more years, no d | int  
    B15003_021E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Associate's degree                  | int  
    B15003_022E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Bachelor's degree                   | int  
    B15003_023E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Master's degree                     | int  
    B15003_024E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Professional school degree          | int  
    B15003_025E  | EDUCATIONAL ATTAINMENT FOR THE | !! !! Estimate Total Doctorate degree                    | int  
    -------------------------------------------------------------------------------------------------------------------


After identifying relevant variables, we then need to identify the
geographies of interest. We are interested in block groups in Cook
County, Illinois, so first we look for the geographic identifier (FIPS
code) for Illinois, then the identifiers for all counties with Illinois
to find Cook County:

.. code:: ipython3

    censusdata.geographies(censusdata.censusgeo([('state', '*')]), 'acs5', 2015)




.. parsed-literal::

    {'Mississippi': censusgeo((('state', '28'),)),
     'Missouri': censusgeo((('state', '29'),)),
     'Montana': censusgeo((('state', '30'),)),
     'Nebraska': censusgeo((('state', '31'),)),
     'Nevada': censusgeo((('state', '32'),)),
     'New Hampshire': censusgeo((('state', '33'),)),
     'New Jersey': censusgeo((('state', '34'),)),
     'New Mexico': censusgeo((('state', '35'),)),
     'New York': censusgeo((('state', '36'),)),
     'North Carolina': censusgeo((('state', '37'),)),
     'North Dakota': censusgeo((('state', '38'),)),
     'Ohio': censusgeo((('state', '39'),)),
     'Oklahoma': censusgeo((('state', '40'),)),
     'Oregon': censusgeo((('state', '41'),)),
     'Pennsylvania': censusgeo((('state', '42'),)),
     'Rhode Island': censusgeo((('state', '44'),)),
     'South Carolina': censusgeo((('state', '45'),)),
     'South Dakota': censusgeo((('state', '46'),)),
     'Tennessee': censusgeo((('state', '47'),)),
     'Texas': censusgeo((('state', '48'),)),
     'Vermont': censusgeo((('state', '50'),)),
     'Utah': censusgeo((('state', '49'),)),
     'Virginia': censusgeo((('state', '51'),)),
     'Washington': censusgeo((('state', '53'),)),
     'West Virginia': censusgeo((('state', '54'),)),
     'Wisconsin': censusgeo((('state', '55'),)),
     'Wyoming': censusgeo((('state', '56'),)),
     'Puerto Rico': censusgeo((('state', '72'),)),
     'Alabama': censusgeo((('state', '01'),)),
     'Alaska': censusgeo((('state', '02'),)),
     'Arizona': censusgeo((('state', '04'),)),
     'Arkansas': censusgeo((('state', '05'),)),
     'California': censusgeo((('state', '06'),)),
     'Colorado': censusgeo((('state', '08'),)),
     'Delaware': censusgeo((('state', '10'),)),
     'District of Columbia': censusgeo((('state', '11'),)),
     'Connecticut': censusgeo((('state', '09'),)),
     'Florida': censusgeo((('state', '12'),)),
     'Georgia': censusgeo((('state', '13'),)),
     'Idaho': censusgeo((('state', '16'),)),
     'Hawaii': censusgeo((('state', '15'),)),
     'Illinois': censusgeo((('state', '17'),)),
     'Indiana': censusgeo((('state', '18'),)),
     'Iowa': censusgeo((('state', '19'),)),
     'Kansas': censusgeo((('state', '20'),)),
     'Kentucky': censusgeo((('state', '21'),)),
     'Louisiana': censusgeo((('state', '22'),)),
     'Maine': censusgeo((('state', '23'),)),
     'Maryland': censusgeo((('state', '24'),)),
     'Massachusetts': censusgeo((('state', '25'),)),
     'Michigan': censusgeo((('state', '26'),)),
     'Minnesota': censusgeo((('state', '27'),))}



.. code:: ipython3

    censusdata.geographies(censusdata.censusgeo([('state', '17'), ('county', '*')]), 'acs5', 2015)




.. parsed-literal::

    {'Winnebago County, Illinois': censusgeo((('state', '17'), ('county', '201'))),
     'Piatt County, Illinois': censusgeo((('state', '17'), ('county', '147'))),
     'Pulaski County, Illinois': censusgeo((('state', '17'), ('county', '153'))),
     'Schuyler County, Illinois': censusgeo((('state', '17'), ('county', '169'))),
     'Stark County, Illinois': censusgeo((('state', '17'), ('county', '175'))),
     'Edgar County, Illinois': censusgeo((('state', '17'), ('county', '045'))),
     'Bond County, Illinois': censusgeo((('state', '17'), ('county', '005'))),
     'Boone County, Illinois': censusgeo((('state', '17'), ('county', '007'))),
     'Bureau County, Illinois': censusgeo((('state', '17'), ('county', '011'))),
     'Carroll County, Illinois': censusgeo((('state', '17'), ('county', '015'))),
     'Coles County, Illinois': censusgeo((('state', '17'), ('county', '029'))),
     'Crawford County, Illinois': censusgeo((('state', '17'), ('county', '033'))),
     'Jersey County, Illinois': censusgeo((('state', '17'), ('county', '083'))),
     'Putnam County, Illinois': censusgeo((('state', '17'), ('county', '155'))),
     'De Witt County, Illinois': censusgeo((('state', '17'), ('county', '039'))),
     'Fayette County, Illinois': censusgeo((('state', '17'), ('county', '051'))),
     'Lee County, Illinois': censusgeo((('state', '17'), ('county', '103'))),
     'Logan County, Illinois': censusgeo((('state', '17'), ('county', '107'))),
     'Macoupin County, Illinois': censusgeo((('state', '17'), ('county', '117'))),
     'Richland County, Illinois': censusgeo((('state', '17'), ('county', '159'))),
     'Washington County, Illinois': censusgeo((('state', '17'), ('county', '189'))),
     'Montgomery County, Illinois': censusgeo((('state', '17'), ('county', '135'))),
     'Adams County, Illinois': censusgeo((('state', '17'), ('county', '001'))),
     'Clinton County, Illinois': censusgeo((('state', '17'), ('county', '027'))),
     'Edwards County, Illinois': censusgeo((('state', '17'), ('county', '047'))),
     'Jefferson County, Illinois': censusgeo((('state', '17'), ('county', '081'))),
     'Vermilion County, Illinois': censusgeo((('state', '17'), ('county', '183'))),
     'Williamson County, Illinois': censusgeo((('state', '17'), ('county', '199'))),
     'Clark County, Illinois': censusgeo((('state', '17'), ('county', '023'))),
     'Effingham County, Illinois': censusgeo((('state', '17'), ('county', '049'))),
     'Fulton County, Illinois': censusgeo((('state', '17'), ('county', '057'))),
     'Hamilton County, Illinois': censusgeo((('state', '17'), ('county', '065'))),
     'Henry County, Illinois': censusgeo((('state', '17'), ('county', '073'))),
     'Johnson County, Illinois': censusgeo((('state', '17'), ('county', '087'))),
     'Lake County, Illinois': censusgeo((('state', '17'), ('county', '097'))),
     'Livingston County, Illinois': censusgeo((('state', '17'), ('county', '105'))),
     'Scott County, Illinois': censusgeo((('state', '17'), ('county', '171'))),
     'Cass County, Illinois': censusgeo((('state', '17'), ('county', '017'))),
     'Warren County, Illinois': censusgeo((('state', '17'), ('county', '187'))),
     'Madison County, Illinois': censusgeo((('state', '17'), ('county', '119'))),
     'Mercer County, Illinois': censusgeo((('state', '17'), ('county', '131'))),
     'Sangamon County, Illinois': censusgeo((('state', '17'), ('county', '167'))),
     'Randolph County, Illinois': censusgeo((('state', '17'), ('county', '157'))),
     'Ogle County, Illinois': censusgeo((('state', '17'), ('county', '141'))),
     'Stephenson County, Illinois': censusgeo((('state', '17'), ('county', '177'))),
     'White County, Illinois': censusgeo((('state', '17'), ('county', '193'))),
     'Henderson County, Illinois': censusgeo((('state', '17'), ('county', '071'))),
     'McLean County, Illinois': censusgeo((('state', '17'), ('county', '113'))),
     'Pike County, Illinois': censusgeo((('state', '17'), ('county', '149'))),
     'Rock Island County, Illinois': censusgeo((('state', '17'), ('county', '161'))),
     'Wabash County, Illinois': censusgeo((('state', '17'), ('county', '185'))),
     'Cumberland County, Illinois': censusgeo((('state', '17'), ('county', '035'))),
     'Kane County, Illinois': censusgeo((('state', '17'), ('county', '089'))),
     'Brown County, Illinois': censusgeo((('state', '17'), ('county', '009'))),
     'Marshall County, Illinois': censusgeo((('state', '17'), ('county', '123'))),
     'Christian County, Illinois': censusgeo((('state', '17'), ('county', '021'))),
     'Jackson County, Illinois': censusgeo((('state', '17'), ('county', '077'))),
     'Union County, Illinois': censusgeo((('state', '17'), ('county', '181'))),
     'Saline County, Illinois': censusgeo((('state', '17'), ('county', '165'))),
     'Whiteside County, Illinois': censusgeo((('state', '17'), ('county', '195'))),
     'DeKalb County, Illinois': censusgeo((('state', '17'), ('county', '037'))),
     'Jasper County, Illinois': censusgeo((('state', '17'), ('county', '079'))),
     'Will County, Illinois': censusgeo((('state', '17'), ('county', '197'))),
     'Douglas County, Illinois': censusgeo((('state', '17'), ('county', '041'))),
     'Greene County, Illinois': censusgeo((('state', '17'), ('county', '061'))),
     'Hardin County, Illinois': censusgeo((('state', '17'), ('county', '069'))),
     'Knox County, Illinois': censusgeo((('state', '17'), ('county', '095'))),
     'Massac County, Illinois': censusgeo((('state', '17'), ('county', '127'))),
     'Tazewell County, Illinois': censusgeo((('state', '17'), ('county', '179'))),
     'Hancock County, Illinois': censusgeo((('state', '17'), ('county', '067'))),
     'Grundy County, Illinois': censusgeo((('state', '17'), ('county', '063'))),
     'Kankakee County, Illinois': censusgeo((('state', '17'), ('county', '091'))),
     'DuPage County, Illinois': censusgeo((('state', '17'), ('county', '043'))),
     'Alexander County, Illinois': censusgeo((('state', '17'), ('county', '003'))),
     'Menard County, Illinois': censusgeo((('state', '17'), ('county', '129'))),
     'LaSalle County, Illinois': censusgeo((('state', '17'), ('county', '099'))),
     'Cook County, Illinois': censusgeo((('state', '17'), ('county', '031'))),
     'Macon County, Illinois': censusgeo((('state', '17'), ('county', '115'))),
     'Morgan County, Illinois': censusgeo((('state', '17'), ('county', '137'))),
     'Wayne County, Illinois': censusgeo((('state', '17'), ('county', '191'))),
     'Woodford County, Illinois': censusgeo((('state', '17'), ('county', '203'))),
     'Franklin County, Illinois': censusgeo((('state', '17'), ('county', '055'))),
     'McDonough County, Illinois': censusgeo((('state', '17'), ('county', '109'))),
     'McHenry County, Illinois': censusgeo((('state', '17'), ('county', '111'))),
     'Moultrie County, Illinois': censusgeo((('state', '17'), ('county', '139'))),
     'Perry County, Illinois': censusgeo((('state', '17'), ('county', '145'))),
     'Pope County, Illinois': censusgeo((('state', '17'), ('county', '151'))),
     'St. Clair County, Illinois': censusgeo((('state', '17'), ('county', '163'))),
     'Shelby County, Illinois': censusgeo((('state', '17'), ('county', '173'))),
     'Champaign County, Illinois': censusgeo((('state', '17'), ('county', '019'))),
     'Calhoun County, Illinois': censusgeo((('state', '17'), ('county', '013'))),
     'Ford County, Illinois': censusgeo((('state', '17'), ('county', '053'))),
     'Jo Daviess County, Illinois': censusgeo((('state', '17'), ('county', '085'))),
     'Kendall County, Illinois': censusgeo((('state', '17'), ('county', '093'))),
     'Lawrence County, Illinois': censusgeo((('state', '17'), ('county', '101'))),
     'Marion County, Illinois': censusgeo((('state', '17'), ('county', '121'))),
     'Mason County, Illinois': censusgeo((('state', '17'), ('county', '125'))),
     'Iroquois County, Illinois': censusgeo((('state', '17'), ('county', '075'))),
     'Clay County, Illinois': censusgeo((('state', '17'), ('county', '025'))),
     'Gallatin County, Illinois': censusgeo((('state', '17'), ('county', '059'))),
     'Monroe County, Illinois': censusgeo((('state', '17'), ('county', '133'))),
     'Peoria County, Illinois': censusgeo((('state', '17'), ('county', '143')))}



Now that we have identified the variables and geographies of interest,
we can download the data using ``censusdata.download`` and compute
variables for the percent unemployed and the percent with no high school
degree:

.. code:: ipython3

    cookbg = censusdata.download('acs5', 2015,
                                 censusdata.censusgeo([('state', '17'), ('county', '031'), ('block group', '*')]),
                                 ['B23025_003E', 'B23025_005E', 'B15003_001E', 'B15003_002E', 'B15003_003E',
                                  'B15003_004E', 'B15003_005E', 'B15003_006E', 'B15003_007E', 'B15003_008E',
                                  'B15003_009E', 'B15003_010E', 'B15003_011E', 'B15003_012E', 'B15003_013E',
                                  'B15003_014E', 'B15003_015E', 'B15003_016E'])
    cookbg['percent_unemployed'] = cookbg.B23025_005E / cookbg.B23025_003E * 100
    cookbg['percent_nohs'] = (cookbg.B15003_002E + cookbg.B15003_003E + cookbg.B15003_004E
                              + cookbg.B15003_005E + cookbg.B15003_006E + cookbg.B15003_007E + cookbg.B15003_008E
                              + cookbg.B15003_009E + cookbg.B15003_010E + cookbg.B15003_011E + cookbg.B15003_012E
                              + cookbg.B15003_013E + cookbg.B15003_014E +
                              cookbg.B15003_015E + cookbg.B15003_016E) / cookbg.B15003_001E * 100
    cookbg = cookbg[['percent_unemployed', 'percent_nohs']]
    cookbg.describe()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>percent_unemployed</th>
          <th>percent_nohs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>3983.00</td>
          <td>3984.00</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>12.00</td>
          <td>15.19</td>
        </tr>
        <tr>
          <th>std</th>
          <td>10.09</td>
          <td>13.23</td>
        </tr>
        <tr>
          <th>min</th>
          <td>0.00</td>
          <td>0.00</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>4.86</td>
          <td>4.75</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>9.24</td>
          <td>11.66</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>16.28</td>
          <td>22.46</td>
        </tr>
        <tr>
          <th>max</th>
          <td>91.86</td>
          <td>77.43</td>
        </tr>
      </tbody>
    </table>
    </div>



Next, we show the 30 block groups in Cook County with the highest rate
of unemployment, and the percent with no high school degree in those
block groups.

.. code:: ipython3

    cookbg.sort_values('percent_unemployed', ascending=False).head(30)




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>percent_unemployed</th>
          <th>percent_nohs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Block Group 1, Census Tract 8357, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:835700&gt; block group:1</th>
          <td>91.86</td>
          <td>0.00</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 6805, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:680500&gt; block group:2</th>
          <td>66.27</td>
          <td>19.54</td>
        </tr>
        <tr>
          <th>Block Group 3, Census Tract 5103, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:510300&gt; block group:3</th>
          <td>64.07</td>
          <td>16.97</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 6809, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:680900&gt; block group:2</th>
          <td>61.46</td>
          <td>42.33</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 4913, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:491300&gt; block group:1</th>
          <td>56.40</td>
          <td>14.64</td>
        </tr>
        <tr>
          <th>Block Group 5, Census Tract 2315, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:231500&gt; block group:5</th>
          <td>55.58</td>
          <td>44.72</td>
        </tr>
        <tr>
          <th>Block Group 3, Census Tract 8346, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:834600&gt; block group:3</th>
          <td>54.96</td>
          <td>17.85</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 6706, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:670600&gt; block group:2</th>
          <td>54.13</td>
          <td>9.57</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 8386, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:838600&gt; block group:2</th>
          <td>53.78</td>
          <td>48.41</td>
        </tr>
        <tr>
          <th>Block Group 5, Census Tract 4910, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:491000&gt; block group:5</th>
          <td>53.57</td>
          <td>38.23</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 5401.02, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:540102&gt; block group:1</th>
          <td>52.90</td>
          <td>6.67</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 6712, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:671200&gt; block group:2</th>
          <td>52.84</td>
          <td>26.98</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 7109, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:710900&gt; block group:1</th>
          <td>52.68</td>
          <td>19.08</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 3406, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:340600&gt; block group:1</th>
          <td>51.76</td>
          <td>42.59</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 6712, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:671200&gt; block group:1</th>
          <td>51.53</td>
          <td>37.70</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 4910, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:491000&gt; block group:2</th>
          <td>51.47</td>
          <td>26.50</td>
        </tr>
        <tr>
          <th>Block Group 3, Census Tract 4303, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:430300&gt; block group:3</th>
          <td>51.41</td>
          <td>14.85</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 6810, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:681000&gt; block group:1</th>
          <td>51.10</td>
          <td>24.38</td>
        </tr>
        <tr>
          <th>Block Group 6, Census Tract 7104, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:710400&gt; block group:6</th>
          <td>50.00</td>
          <td>9.34</td>
        </tr>
        <tr>
          <th>Block Group 5, Census Tract 6811, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:681100&gt; block group:5</th>
          <td>50.00</td>
          <td>31.95</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 6812, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:681200&gt; block group:2</th>
          <td>49.82</td>
          <td>20.29</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 8290, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:829000&gt; block group:1</th>
          <td>49.57</td>
          <td>28.97</td>
        </tr>
        <tr>
          <th>Block Group 3, Census Tract 6813, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:681300&gt; block group:3</th>
          <td>49.51</td>
          <td>22.92</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 6811, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:681100&gt; block group:1</th>
          <td>49.32</td>
          <td>33.73</td>
        </tr>
        <tr>
          <th>Block Group 2, Census Tract 7107, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:710700&gt; block group:2</th>
          <td>49.00</td>
          <td>17.18</td>
        </tr>
        <tr>
          <th>Block Group 6, Census Tract 4804, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:480400&gt; block group:6</th>
          <td>48.68</td>
          <td>8.32</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 4207, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:420700&gt; block group:1</th>
          <td>48.63</td>
          <td>14.08</td>
        </tr>
        <tr>
          <th>Block Group 1, Census Tract 6715, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:671500&gt; block group:1</th>
          <td>48.28</td>
          <td>30.24</td>
        </tr>
        <tr>
          <th>Block Group 4, Census Tract 4603.02, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:460302&gt; block group:4</th>
          <td>48.00</td>
          <td>48.27</td>
        </tr>
        <tr>
          <th>Block Group 3, Census Tract 8424, Cook County, Illinois: Summary level: 150, state:17&gt; county:031&gt; tract:842400&gt; block group:3</th>
          <td>47.80</td>
          <td>0.00</td>
        </tr>
      </tbody>
    </table>
    </div>



Finally, we show the correlation between these two variables across all
Cook County block groups:

.. code:: ipython3

    cookbg.corr()




.. raw:: html

    <div>
    <style scoped>
        .dataframe tbody tr th:only-of-type {
            vertical-align: middle;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
        }
    
        .dataframe thead th {
            text-align: right;
        }
    </style>
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>percent_unemployed</th>
          <th>percent_nohs</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>percent_unemployed</th>
          <td>1.00</td>
          <td>0.29</td>
        </tr>
        <tr>
          <th>percent_nohs</th>
          <td>0.29</td>
          <td>1.00</td>
        </tr>
      </tbody>
    </table>
    </div>


