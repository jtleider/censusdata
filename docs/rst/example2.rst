
Example 2: Downloading Data for All U.S. Counties
=================================================

Using the Detail Tables
-----------------------

For this example, let’s suppose we have looked up the variables we need
by referring to the Table Shells. We begin by downloading the data and
checking the data we have received:

.. code:: ipython3

    import pandas as pd
    import censusdata
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.precision', 2)
    
    county65plus = censusdata.download('acs5', 2015, censusdata.censusgeo([('county', '*')]),
                                       ['B01001_001E', 'B01001_020E', 'B01001_021E', 'B01001_022E', 'B01001_023E',
                                        'B01001_024E', 'B01001_025E', 'B01001_044E', 'B01001_045E', 'B01001_046E',
                                        'B01001_047E', 'B01001_048E', 'B01001_049E'])
    county65plus.describe()




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
          <th>B01001_001E</th>
          <th>B01001_020E</th>
          <th>B01001_021E</th>
          <th>B01001_022E</th>
          <th>B01001_023E</th>
          <th>B01001_024E</th>
          <th>B01001_025E</th>
          <th>B01001_044E</th>
          <th>B01001_045E</th>
          <th>B01001_046E</th>
          <th>B01001_047E</th>
          <th>B01001_048E</th>
          <th>B01001_049E</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>3.22e+03</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>9.94e+04</td>
          <td>961.47</td>
          <td>1201.25</td>
          <td>1532.44</td>
          <td>1075.61</td>
          <td>748.45</td>
          <td>629.46</td>
          <td>1064.89</td>
          <td>1350.16</td>
          <td>1802.07</td>
          <td>1358.99</td>
          <td>1079.33</td>
          <td>1236.80</td>
        </tr>
        <tr>
          <th>std</th>
          <td>3.19e+05</td>
          <td>2669.50</td>
          <td>3306.09</td>
          <td>4193.15</td>
          <td>2994.94</td>
          <td>2184.18</td>
          <td>1945.32</td>
          <td>3085.53</td>
          <td>3860.28</td>
          <td>5149.07</td>
          <td>3920.19</td>
          <td>3183.31</td>
          <td>3741.48</td>
        </tr>
        <tr>
          <th>min</th>
          <td>8.50e+01</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>2.00</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>0.00</td>
          <td>0.00</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>1.12e+04</td>
          <td>134.00</td>
          <td>173.00</td>
          <td>234.00</td>
          <td>165.00</td>
          <td>106.00</td>
          <td>80.00</td>
          <td>136.00</td>
          <td>178.00</td>
          <td>252.00</td>
          <td>196.00</td>
          <td>143.00</td>
          <td>157.75</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>2.60e+04</td>
          <td>308.00</td>
          <td>391.50</td>
          <td>513.00</td>
          <td>353.00</td>
          <td>231.00</td>
          <td>180.50</td>
          <td>322.00</td>
          <td>413.00</td>
          <td>560.00</td>
          <td>429.00</td>
          <td>318.00</td>
          <td>350.50</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>6.64e+04</td>
          <td>750.75</td>
          <td>949.25</td>
          <td>1242.75</td>
          <td>850.00</td>
          <td>550.25</td>
          <td>430.00</td>
          <td>790.75</td>
          <td>1040.75</td>
          <td>1362.75</td>
          <td>1012.00</td>
          <td>789.00</td>
          <td>847.00</td>
        </tr>
        <tr>
          <th>max</th>
          <td>1.00e+07</td>
          <td>79196.00</td>
          <td>96638.00</td>
          <td>122804.00</td>
          <td>88018.00</td>
          <td>65118.00</td>
          <td>59251.00</td>
          <td>91381.00</td>
          <td>114778.00</td>
          <td>152378.00</td>
          <td>116736.00</td>
          <td>93446.00</td>
          <td>110015.00</td>
        </tr>
      </tbody>
    </table>
    </div>



Then we keep the variables of interest, rename, and print descriptives:

.. code:: ipython3

    county65plus['percent_65plus'] = (county65plus.B01001_020E + county65plus.B01001_021E + county65plus.B01001_022E
                                      + county65plus.B01001_023E + county65plus.B01001_024E + county65plus.B01001_025E
                                      + county65plus.B01001_044E + county65plus.B01001_045E + county65plus.B01001_046E
                                      + county65plus.B01001_047E + county65plus.B01001_048E
                                      + county65plus.B01001_049E) / county65plus.B01001_001E * 100
    county65plus = county65plus[['B01001_001E', 'percent_65plus']]
    county65plus = county65plus.rename(columns={'B01001_001E': 'population_size'})
    county65plus.describe()




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
          <th>population_size</th>
          <th>percent_65plus</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>3.22e+03</td>
          <td>3220.00</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>9.94e+04</td>
          <td>17.10</td>
        </tr>
        <tr>
          <th>std</th>
          <td>3.19e+05</td>
          <td>4.39</td>
        </tr>
        <tr>
          <th>min</th>
          <td>8.50e+01</td>
          <td>3.30</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>1.12e+04</td>
          <td>14.32</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>2.60e+04</td>
          <td>16.78</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>6.64e+04</td>
          <td>19.45</td>
        </tr>
        <tr>
          <th>max</th>
          <td>1.00e+07</td>
          <td>50.89</td>
        </tr>
      </tbody>
    </table>
    </div>



Finally, we show the 30 U.S. counties with the highest percentage aged
65+:

.. code:: ipython3

    county65plus.sort_values('percent_65plus', ascending=False, inplace=True)
    county65plus.head(30)




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
          <th>population_size</th>
          <th>percent_65plus</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Sumter County, Florida: Summary level: 050, state:12&gt; county:119</th>
          <td>108501</td>
          <td>50.89</td>
        </tr>
        <tr>
          <th>Charlotte County, Florida: Summary level: 050, state:12&gt; county:015</th>
          <td>165783</td>
          <td>36.86</td>
        </tr>
        <tr>
          <th>Mineral County, Colorado: Summary level: 050, state:08&gt; county:079</th>
          <td>733</td>
          <td>36.56</td>
        </tr>
        <tr>
          <th>Hooker County, Nebraska: Summary level: 050, state:31&gt; county:091</th>
          <td>681</td>
          <td>35.83</td>
        </tr>
        <tr>
          <th>La Paz County, Arizona: Summary level: 050, state:04&gt; county:012</th>
          <td>20335</td>
          <td>35.17</td>
        </tr>
        <tr>
          <th>Citrus County, Florida: Summary level: 050, state:12&gt; county:017</th>
          <td>139654</td>
          <td>34.43</td>
        </tr>
        <tr>
          <th>Wheeler County, Oregon: Summary level: 050, state:41&gt; county:069</th>
          <td>1348</td>
          <td>34.35</td>
        </tr>
        <tr>
          <th>Highland County, Virginia: Summary level: 050, state:51&gt; county:091</th>
          <td>2244</td>
          <td>34.00</td>
        </tr>
        <tr>
          <th>Real County, Texas: Summary level: 050, state:48&gt; county:385</th>
          <td>3356</td>
          <td>33.97</td>
        </tr>
        <tr>
          <th>Sierra County, New Mexico: Summary level: 050, state:35&gt; county:051</th>
          <td>11615</td>
          <td>33.95</td>
        </tr>
        <tr>
          <th>Alcona County, Michigan: Summary level: 050, state:26&gt; county:001</th>
          <td>10550</td>
          <td>33.93</td>
        </tr>
        <tr>
          <th>Lancaster County, Virginia: Summary level: 050, state:51&gt; county:103</th>
          <td>11129</td>
          <td>33.91</td>
        </tr>
        <tr>
          <th>Llano County, Texas: Summary level: 050, state:48&gt; county:299</th>
          <td>19323</td>
          <td>33.63</td>
        </tr>
        <tr>
          <th>Highlands County, Florida: Summary level: 050, state:12&gt; county:055</th>
          <td>98328</td>
          <td>33.35</td>
        </tr>
        <tr>
          <th>Sarasota County, Florida: Summary level: 050, state:12&gt; county:115</th>
          <td>392038</td>
          <td>33.20</td>
        </tr>
        <tr>
          <th>McIntosh County, North Dakota: Summary level: 050, state:38&gt; county:051</th>
          <td>2759</td>
          <td>33.09</td>
        </tr>
        <tr>
          <th>Northumberland County, Virginia: Summary level: 050, state:51&gt; county:133</th>
          <td>12304</td>
          <td>33.07</td>
        </tr>
        <tr>
          <th>Catron County, New Mexico: Summary level: 050, state:35&gt; county:003</th>
          <td>3583</td>
          <td>32.71</td>
        </tr>
        <tr>
          <th>Towns County, Georgia: Summary level: 050, state:13&gt; county:281</th>
          <td>10800</td>
          <td>31.82</td>
        </tr>
        <tr>
          <th>Hickory County, Missouri: Summary level: 050, state:29&gt; county:085</th>
          <td>9335</td>
          <td>31.49</td>
        </tr>
        <tr>
          <th>Ontonagon County, Michigan: Summary level: 050, state:26&gt; county:131</th>
          <td>6298</td>
          <td>30.61</td>
        </tr>
        <tr>
          <th>Curry County, Oregon: Summary level: 050, state:41&gt; county:015</th>
          <td>22338</td>
          <td>30.48</td>
        </tr>
        <tr>
          <th>Union County, Georgia: Summary level: 050, state:13&gt; county:291</th>
          <td>21725</td>
          <td>30.43</td>
        </tr>
        <tr>
          <th>Hinsdale County, Colorado: Summary level: 050, state:08&gt; county:053</th>
          <td>874</td>
          <td>30.09</td>
        </tr>
        <tr>
          <th>Jefferson County, Washington: Summary level: 050, state:53&gt; county:031</th>
          <td>30083</td>
          <td>30.06</td>
        </tr>
        <tr>
          <th>McPherson County, South Dakota: Summary level: 050, state:46&gt; county:089</th>
          <td>2263</td>
          <td>29.74</td>
        </tr>
        <tr>
          <th>McMullen County, Texas: Summary level: 050, state:48&gt; county:311</th>
          <td>778</td>
          <td>29.69</td>
        </tr>
        <tr>
          <th>Keweenaw County, Michigan: Summary level: 050, state:26&gt; county:083</th>
          <td>2198</td>
          <td>29.66</td>
        </tr>
        <tr>
          <th>Baxter County, Arkansas: Summary level: 050, state:05&gt; county:005</th>
          <td>41040</td>
          <td>29.57</td>
        </tr>
        <tr>
          <th>Indian River County, Florida: Summary level: 050, state:12&gt; county:061</th>
          <td>142866</td>
          <td>29.51</td>
        </tr>
      </tbody>
    </table>
    </div>



Using the Data Profile Tables
-----------------------------

There is more than one way to approach this problem. Let’s see how to
use the data profile tables for the same purpose. First, we identify the
appropriate table:

.. code:: ipython3

    censusdata.search('acs5', 2015, 'label', '65', tabletype='profile')[-25:]




.. parsed-literal::

    [('DP02PR_0077PE',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'Percent!!DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02_0012E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Estimate!!HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02_0012PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Percent!!HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02_0014E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Estimate!!HOUSEHOLDS BY TYPE!!Households with one or more people 65 years and over'),
     ('DP02_0014PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Percent!!HOUSEHOLDS BY TYPE!!Households with one or more people 65 years and over'),
     ('DP02_0076E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Estimate!!DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02_0076PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Percent!!DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02_0077E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Estimate!!DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02_0077PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'Percent!!DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP03_0135E',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'Estimate!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over'),
     ('DP03_0135PE',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over'),
     ('DP03_0136E',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'Estimate!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!People in families'),
     ('DP03_0136PE',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!People in families'),
     ('DP03_0137E',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'Estimate!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!Unrelated individuals 15 years and over'),
     ('DP03_0137PE',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'Percent!!PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!Unrelated individuals 15 years and over'),
     ('DP05_0014E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Estimate!!SEX AND AGE!!65 to 74 years'),
     ('DP05_0014PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Percent!!SEX AND AGE!!65 to 74 years'),
     ('DP05_0021E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Estimate!!SEX AND AGE!!65 years and over'),
     ('DP05_0021PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Percent!!SEX AND AGE!!65 years and over'),
     ('DP05_0025E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Estimate!!SEX AND AGE!!65 years and over'),
     ('DP05_0025PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Percent!!SEX AND AGE!!65 years and over'),
     ('DP05_0026E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Estimate!!SEX AND AGE!!65 years and over!!Male'),
     ('DP05_0026PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Percent!!SEX AND AGE!!65 years and over!!Male'),
     ('DP05_0027E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Estimate!!SEX AND AGE!!65 years and over!!Female'),
     ('DP05_0027PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'Percent!!SEX AND AGE!!65 years and over!!Female')]



.. code:: ipython3

    censusdata.printtable(censusdata.censustable('acs5', 2015, 'DP05'))


.. parsed-literal::

    Variable     | Table                          | Label                                                    | Type 
    -------------------------------------------------------------------------------------------------------------------
    DP05_0001E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE Total population              | int  
    DP05_0001PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE Total population               | int  
    DP05_0002E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate SEX AND AGE Total population Male      | int  
    DP05_0002PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent SEX AND AGE Total population Male       | float
    DP05_0003E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate SEX AND AGE Total population Female    | int  
    DP05_0003PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent SEX AND AGE Total population Female     | float
    DP05_0004E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE Under 5 years                 | int  
    DP05_0004PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE Under 5 years                  | float
    DP05_0005E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 5 to 9 years                  | int  
    DP05_0005PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 5 to 9 years                   | float
    DP05_0006E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 10 to 14 years                | int  
    DP05_0006PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 10 to 14 years                 | float
    DP05_0007E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 15 to 19 years                | int  
    DP05_0007PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 15 to 19 years                 | float
    DP05_0008E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 20 to 24 years                | int  
    DP05_0008PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 20 to 24 years                 | float
    DP05_0009E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 25 to 34 years                | int  
    DP05_0009PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 25 to 34 years                 | float
    DP05_0010E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 35 to 44 years                | int  
    DP05_0010PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 35 to 44 years                 | float
    DP05_0011E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 45 to 54 years                | int  
    DP05_0011PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 45 to 54 years                 | float
    DP05_0012E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 55 to 59 years                | int  
    DP05_0012PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 55 to 59 years                 | float
    DP05_0013E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 60 to 64 years                | int  
    DP05_0013PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 60 to 64 years                 | float
    DP05_0014E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 65 to 74 years                | int  
    DP05_0014PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 65 to 74 years                 | float
    DP05_0015E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 75 to 84 years                | int  
    DP05_0015PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 75 to 84 years                 | float
    DP05_0016E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 85 years and over             | int  
    DP05_0016PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 85 years and over              | float
    DP05_0017E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE Median age (years)            | float
    DP05_0017PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE Median age (years)             | int  
    DP05_0018E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 18 years and over             | int  
    DP05_0018PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 18 years and over              | float
    DP05_0019E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 21 years and over             | int  
    DP05_0019PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 21 years and over              | float
    DP05_0020E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 62 years and over             | int  
    DP05_0020PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 62 years and over              | float
    DP05_0021E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 65 years and over             | int  
    DP05_0021PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 65 years and over              | float
    DP05_0022E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 18 years and over             | int  
    DP05_0022PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 18 years and over              | int  
    DP05_0023E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate SEX AND AGE 18 years and over Male     | int  
    DP05_0023PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent SEX AND AGE 18 years and over Male      | float
    DP05_0024E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate SEX AND AGE 18 years and over Female   | int  
    DP05_0024PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent SEX AND AGE 18 years and over Female    | float
    DP05_0025E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate SEX AND AGE 65 years and over             | int  
    DP05_0025PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent SEX AND AGE 65 years and over              | int  
    DP05_0026E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate SEX AND AGE 65 years and over Male     | int  
    DP05_0026PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent SEX AND AGE 65 years and over Male      | float
    DP05_0027E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate SEX AND AGE 65 years and over Female   | int  
    DP05_0027PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent SEX AND AGE 65 years and over Female    | float
    DP05_0028E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate RACE Total population                     | int  
    DP05_0028PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent RACE Total population                      | int  
    DP05_0029E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE Total population One race         | int  
    DP05_0029PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE Total population One race          | float
    DP05_0030E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE Total population Two or more race | int  
    DP05_0030PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE Total population Two or more races | float
    DP05_0031E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate RACE One race                             | int  
    DP05_0031PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent RACE One race                              | float
    DP05_0032E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE One race White                    | int  
    DP05_0032PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE One race White                     | float
    DP05_0033E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE One race Black or African America | int  
    DP05_0033PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE One race Black or African American | float
    DP05_0034E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE One race American Indian and Alas | int  
    DP05_0034PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE One race American Indian and Alask | float
    DP05_0035E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race American Indian and A | int  
    DP05_0035PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race American Indian and Al | float
    DP05_0036E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race American Indian and A | int  
    DP05_0036PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race American Indian and Al | float
    DP05_0037E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race American Indian and A | int  
    DP05_0037PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race American Indian and Al | float
    DP05_0038E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race American Indian and A | int  
    DP05_0038PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race American Indian and Al | float
    DP05_0039E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE One race Asian                    | int  
    DP05_0039PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE One race Asian                     | float
    DP05_0040E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Asian Asian Indian    | int  
    DP05_0040PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Asian Asian Indian     | float
    DP05_0041E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Asian Chinese         | int  
    DP05_0041PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Asian Chinese          | float
    DP05_0042E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Asian Filipino        | int  
    DP05_0042PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Asian Filipino         | float
    DP05_0043E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Asian Japanese        | int  
    DP05_0043PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Asian Japanese         | float
    DP05_0044E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Asian Korean          | int  
    DP05_0044PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Asian Korean           | float
    DP05_0045E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Asian Vietnamese      | int  
    DP05_0045PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Asian Vietnamese       | float
    DP05_0046E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Asian Other Asian     | int  
    DP05_0046PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Asian Other Asian      | float
    DP05_0047E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE One race Native Hawaiian and Othe | int  
    DP05_0047PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE One race Native Hawaiian and Other | float
    DP05_0048E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Native Hawaiian and O | int  
    DP05_0048PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Native Hawaiian and Ot | float
    DP05_0049E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Native Hawaiian and O | int  
    DP05_0049PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Native Hawaiian and Ot | float
    DP05_0050E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Native Hawaiian and O | int  
    DP05_0050PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Native Hawaiian and Ot | float
    DP05_0051E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE One race Native Hawaiian and O | int  
    DP05_0051PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE One race Native Hawaiian and Ot | float
    DP05_0052E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE One race Some other race          | int  
    DP05_0052PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE One race Some other race           | float
    DP05_0053E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate RACE Two or more races                    | int  
    DP05_0053PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent RACE Two or more races                     | float
    DP05_0054E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE Two or more races White and Black | int  
    DP05_0054PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE Two or more races White and Black  | float
    DP05_0055E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE Two or more races White and Ameri | int  
    DP05_0055PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE Two or more races White and Americ | float
    DP05_0056E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE Two or more races White and Asian | int  
    DP05_0056PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE Two or more races White and Asian  | float
    DP05_0057E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE Two or more races Black or Africa | int  
    DP05_0057PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE Two or more races Black or African | float
    DP05_0058E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate RACE Race alone or in combination with | int  
    DP05_0058PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent RACE Race alone or in combination with  | int  
    DP05_0059E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE Race alone or in combination w | int  
    DP05_0059PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE Race alone or in combination wi | float
    DP05_0060E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE Race alone or in combination w | int  
    DP05_0060PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE Race alone or in combination wi | float
    DP05_0061E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE Race alone or in combination w | int  
    DP05_0061PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE Race alone or in combination wi | float
    DP05_0062E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE Race alone or in combination w | int  
    DP05_0062PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE Race alone or in combination wi | float
    DP05_0063E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE Race alone or in combination w | int  
    DP05_0063PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE Race alone or in combination wi | float
    DP05_0064E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate RACE Race alone or in combination w | int  
    DP05_0064PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent RACE Race alone or in combination wi | float
    DP05_0065E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate HISPANIC OR LATINO AND RACE Total populat | int  
    DP05_0065PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent HISPANIC OR LATINO AND RACE Total populati | int  
    DP05_0066E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate HISPANIC OR LATINO AND RACE Total popu | int  
    DP05_0066PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent HISPANIC OR LATINO AND RACE Total popul | float
    DP05_0067E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0067PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0068E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0068PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0069E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0069PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0070E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0070PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0071E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate HISPANIC OR LATINO AND RACE Total popu | int  
    DP05_0071PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent HISPANIC OR LATINO AND RACE Total popul | float
    DP05_0072E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0072PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0073E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0073PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0074E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0074PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0075E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0075PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0076E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0076PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0077E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0077PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0078E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Total p | int  
    DP05_0078PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total po | float
    DP05_0079E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Tota | int  
    DP05_0079PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total | float
    DP05_0080E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! !! Estimate HISPANIC OR LATINO AND RACE Tota | int  
    DP05_0080PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! !! !! Percent HISPANIC OR LATINO AND RACE Total | float
    DP05_0081E   | ACS DEMOGRAPHIC AND HOUSING ES | !! Estimate Total housing units                          | int  
    DP05_0081PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! Percent Total housing units                           | int  
    DP05_0082E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Estimate CITIZEN, VOTING AGE POPULATION Citizen, 1 | int  
    DP05_0082PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! Percent CITIZEN, VOTING AGE POPULATION Citizen, 18 | int  
    DP05_0083E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate CITIZEN, VOTING AGE POPULATION Citizen | int  
    DP05_0083PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent CITIZEN, VOTING AGE POPULATION Citizen, | float
    DP05_0084E   | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Estimate CITIZEN, VOTING AGE POPULATION Citizen | int  
    DP05_0084PE  | ACS DEMOGRAPHIC AND HOUSING ES | !! !! !! Percent CITIZEN, VOTING AGE POPULATION Citizen, | float
    -------------------------------------------------------------------------------------------------------------------


After identifying the relevant variables, we download and describe the
data, and compute the percent 65+ similarly to how we did so before,
except now the computation is somewhat simpler:

.. code:: ipython3

    county65plus = censusdata.download('acs5', 2015, censusdata.censusgeo([('county', '*')]),
                                       ['DP05_0001E', 'DP05_0014PE', 'DP05_0015PE', 'DP05_0016PE',],
                                       tabletype='profile')
    county65plus.describe()




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
          <th>DP05_0001E</th>
          <th>DP05_0014PE</th>
          <th>DP05_0015PE</th>
          <th>DP05_0016PE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>3.22e+03</td>
          <td>3220.00</td>
          <td>3220.00</td>
          <td>3220.00</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>9.94e+04</td>
          <td>9.61</td>
          <td>5.30</td>
          <td>2.19</td>
        </tr>
        <tr>
          <th>std</th>
          <td>3.19e+05</td>
          <td>2.43</td>
          <td>1.63</td>
          <td>0.93</td>
        </tr>
        <tr>
          <th>min</th>
          <td>8.50e+01</td>
          <td>2.10</td>
          <td>0.00</td>
          <td>0.00</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>1.12e+04</td>
          <td>8.10</td>
          <td>4.20</td>
          <td>1.60</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>2.60e+04</td>
          <td>9.40</td>
          <td>5.10</td>
          <td>2.00</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>6.64e+04</td>
          <td>10.80</td>
          <td>6.20</td>
          <td>2.60</td>
        </tr>
        <tr>
          <th>max</th>
          <td>1.00e+07</td>
          <td>32.50</td>
          <td>14.90</td>
          <td>9.10</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    county65plus['percent_65plus'] = (county65plus['DP05_0014PE'] + county65plus['DP05_0015PE']
                                      + county65plus['DP05_0016PE'])
    county65plus = county65plus[['DP05_0001E', 'percent_65plus']]
    county65plus = county65plus.rename(columns={'DP05_0001E': 'population_size'})
    county65plus.describe()




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
          <th>population_size</th>
          <th>percent_65plus</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>3.22e+03</td>
          <td>3220.00</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>9.94e+04</td>
          <td>17.10</td>
        </tr>
        <tr>
          <th>std</th>
          <td>3.19e+05</td>
          <td>4.39</td>
        </tr>
        <tr>
          <th>min</th>
          <td>8.50e+01</td>
          <td>3.30</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>1.12e+04</td>
          <td>14.30</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>2.60e+04</td>
          <td>16.80</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>6.64e+04</td>
          <td>19.40</td>
        </tr>
        <tr>
          <th>max</th>
          <td>1.00e+07</td>
          <td>50.90</td>
        </tr>
      </tbody>
    </table>
    </div>



Finally, we identify the top 30 counties for population aged 65+, and
export data for all counties to CSV:

.. code:: ipython3

    county65plus.sort_values('percent_65plus', ascending=False, inplace=True)
    county65plus.head(30)




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
          <th>population_size</th>
          <th>percent_65plus</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>Sumter County, Florida: Summary level: 050, state:12&gt; county:119</th>
          <td>108501</td>
          <td>50.9</td>
        </tr>
        <tr>
          <th>Charlotte County, Florida: Summary level: 050, state:12&gt; county:015</th>
          <td>165783</td>
          <td>36.8</td>
        </tr>
        <tr>
          <th>Mineral County, Colorado: Summary level: 050, state:08&gt; county:079</th>
          <td>733</td>
          <td>36.6</td>
        </tr>
        <tr>
          <th>Hooker County, Nebraska: Summary level: 050, state:31&gt; county:091</th>
          <td>681</td>
          <td>35.8</td>
        </tr>
        <tr>
          <th>La Paz County, Arizona: Summary level: 050, state:04&gt; county:012</th>
          <td>20335</td>
          <td>35.2</td>
        </tr>
        <tr>
          <th>Citrus County, Florida: Summary level: 050, state:12&gt; county:017</th>
          <td>139654</td>
          <td>34.4</td>
        </tr>
        <tr>
          <th>Wheeler County, Oregon: Summary level: 050, state:41&gt; county:069</th>
          <td>1348</td>
          <td>34.3</td>
        </tr>
        <tr>
          <th>Real County, Texas: Summary level: 050, state:48&gt; county:385</th>
          <td>3356</td>
          <td>34.0</td>
        </tr>
        <tr>
          <th>Highland County, Virginia: Summary level: 050, state:51&gt; county:091</th>
          <td>2244</td>
          <td>34.0</td>
        </tr>
        <tr>
          <th>Alcona County, Michigan: Summary level: 050, state:26&gt; county:001</th>
          <td>10550</td>
          <td>34.0</td>
        </tr>
        <tr>
          <th>Sierra County, New Mexico: Summary level: 050, state:35&gt; county:051</th>
          <td>11615</td>
          <td>33.9</td>
        </tr>
        <tr>
          <th>Lancaster County, Virginia: Summary level: 050, state:51&gt; county:103</th>
          <td>11129</td>
          <td>33.9</td>
        </tr>
        <tr>
          <th>Llano County, Texas: Summary level: 050, state:48&gt; county:299</th>
          <td>19323</td>
          <td>33.6</td>
        </tr>
        <tr>
          <th>Highlands County, Florida: Summary level: 050, state:12&gt; county:055</th>
          <td>98328</td>
          <td>33.3</td>
        </tr>
        <tr>
          <th>McIntosh County, North Dakota: Summary level: 050, state:38&gt; county:051</th>
          <td>2759</td>
          <td>33.1</td>
        </tr>
        <tr>
          <th>Northumberland County, Virginia: Summary level: 050, state:51&gt; county:133</th>
          <td>12304</td>
          <td>33.1</td>
        </tr>
        <tr>
          <th>Sarasota County, Florida: Summary level: 050, state:12&gt; county:115</th>
          <td>392038</td>
          <td>33.1</td>
        </tr>
        <tr>
          <th>Catron County, New Mexico: Summary level: 050, state:35&gt; county:003</th>
          <td>3583</td>
          <td>32.7</td>
        </tr>
        <tr>
          <th>Towns County, Georgia: Summary level: 050, state:13&gt; county:281</th>
          <td>10800</td>
          <td>31.9</td>
        </tr>
        <tr>
          <th>Hickory County, Missouri: Summary level: 050, state:29&gt; county:085</th>
          <td>9335</td>
          <td>31.5</td>
        </tr>
        <tr>
          <th>Ontonagon County, Michigan: Summary level: 050, state:26&gt; county:131</th>
          <td>6298</td>
          <td>30.6</td>
        </tr>
        <tr>
          <th>Union County, Georgia: Summary level: 050, state:13&gt; county:291</th>
          <td>21725</td>
          <td>30.5</td>
        </tr>
        <tr>
          <th>Curry County, Oregon: Summary level: 050, state:41&gt; county:015</th>
          <td>22338</td>
          <td>30.4</td>
        </tr>
        <tr>
          <th>Hinsdale County, Colorado: Summary level: 050, state:08&gt; county:053</th>
          <td>874</td>
          <td>30.1</td>
        </tr>
        <tr>
          <th>Jefferson County, Washington: Summary level: 050, state:53&gt; county:031</th>
          <td>30083</td>
          <td>30.1</td>
        </tr>
        <tr>
          <th>McMullen County, Texas: Summary level: 050, state:48&gt; county:311</th>
          <td>778</td>
          <td>29.7</td>
        </tr>
        <tr>
          <th>Keweenaw County, Michigan: Summary level: 050, state:26&gt; county:083</th>
          <td>2198</td>
          <td>29.7</td>
        </tr>
        <tr>
          <th>McPherson County, South Dakota: Summary level: 050, state:46&gt; county:089</th>
          <td>2263</td>
          <td>29.7</td>
        </tr>
        <tr>
          <th>Indian River County, Florida: Summary level: 050, state:12&gt; county:061</th>
          <td>142866</td>
          <td>29.6</td>
        </tr>
        <tr>
          <th>Baxter County, Arkansas: Summary level: 050, state:05&gt; county:005</th>
          <td>41040</td>
          <td>29.5</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    censusdata.exportcsv('county65plus.csv', county65plus)
