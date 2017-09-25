
Example 2: Downloading Data for All U.S. Counties
=================================================

Using the Detail Tables
-----------------------

For this example, let's suppose we have looked up the variables we need
by referring to the Table Shells. We begin by downloading the data and
checking the data we have received:

.. code:: ipython3

    county65plus = censusdata.download('acs5', '2015', censusdata.censusgeo([('county', '*')]),
                                       ['B01001_001E', 'B01001_020E', 'B01001_021E', 'B01001_022E', 'B01001_023E',
                                        'B01001_024E', 'B01001_025E', 'B01001_044E', 'B01001_045E', 'B01001_046E',
                                        'B01001_047E', 'B01001_048E', 'B01001_049E'])
    county65plus.describe()




.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
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
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
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
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
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



============================================================

Using the Data Profile Tables
=============================

There is more than one way to approach this problem. Let's see how to
use the data profile tables for the same purpose. First, we identify the
appropriate table:

.. code:: ipython3

    censusdata.search('acs5', '2015', 'label', '65', tabletype='profile')




.. parsed-literal::

    [('DP02PR_0012E',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02PR_0012M',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02PR_0012PE',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02PR_0012PM',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02PR_0014E',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02PR_0014M',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02PR_0014PE',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02PR_0014PM',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02PR_0076E',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02PR_0076M',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02PR_0076PE',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02PR_0076PM',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02PR_0077E',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02PR_0077M',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02PR_0077PE',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02PR_0077PM',
      'SELECTED SOCIAL CHARACTERISTICS IN PUERTO RICO',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02_0012E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02_0012M',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02_0012PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02_0012PM',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Nonfamily households!!Householder living alone!!65 years and over'),
     ('DP02_0014E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02_0014M',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02_0014PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02_0014PM',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'HOUSEHOLDS BY TYPE!!Total households!!Households with one or more people 65 years and over'),
     ('DP02_0076E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02_0076M',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02_0076PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02_0076PM',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over'),
     ('DP02_0077E',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02_0077M',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02_0077PE',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP02_0077PM',
      'SELECTED SOCIAL CHARACTERISTICS IN THE UNITED STATES',
      'DISABILITY STATUS OF THE CIVILIAN NONINSTITUTIONALIZED POPULATION!!65 years and over!!With a disability'),
     ('DP03_0135E',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over'),
     ('DP03_0135M',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over'),
     ('DP03_0135PE',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over'),
     ('DP03_0135PM',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over'),
     ('DP03_0136E',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!People in families'),
     ('DP03_0136M',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!People in families'),
     ('DP03_0137E',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!Unrelated individuals 15 years and over'),
     ('DP03_0137M',
      'SELECTED ECONOMIC CHARACTERISTICS',
      'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL!!65 years and over!!Unrelated individuals 15 years and over'),
     ('DP05_0014E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 to 74 years'),
     ('DP05_0014M',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 to 74 years'),
     ('DP05_0014PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 to 74 years'),
     ('DP05_0014PM',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 to 74 years'),
     ('DP05_0021E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0021M',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0021PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0021PM',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0025E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0025M',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0025PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0025PM',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over'),
     ('DP05_0026E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Male'),
     ('DP05_0026M',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Male'),
     ('DP05_0026PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Male'),
     ('DP05_0026PM',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Male'),
     ('DP05_0027E',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Female'),
     ('DP05_0027M',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Female'),
     ('DP05_0027PE',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Female'),
     ('DP05_0027PM',
      'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
      'SEX AND AGE!!Total population!!65 years and over!!Female')]



.. code:: ipython3

    censusdata.censustable('acs5', '2015', 'DP05')




.. parsed-literal::

    OrderedDict([('DP05_0001E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0001M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0001PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0001PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0002E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0002M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0002PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0002PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0003E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0003M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0003PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0003PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0004E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Under 5 years',
                   'predicateType': 'int'}),
                 ('DP05_0004M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Under 5 years',
                   'predicateType': 'int'}),
                 ('DP05_0004PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Under 5 years',
                   'predicateType': 'int'}),
                 ('DP05_0004PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Under 5 years',
                   'predicateType': 'int'}),
                 ('DP05_0005E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!5 to 9 years',
                   'predicateType': 'int'}),
                 ('DP05_0005M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!5 to 9 years',
                   'predicateType': 'int'}),
                 ('DP05_0005PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!5 to 9 years',
                   'predicateType': 'int'}),
                 ('DP05_0005PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!5 to 9 years',
                   'predicateType': 'int'}),
                 ('DP05_0006E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!10 to 14 years',
                   'predicateType': 'int'}),
                 ('DP05_0006M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!10 to 14 years',
                   'predicateType': 'int'}),
                 ('DP05_0006PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!10 to 14 years',
                   'predicateType': 'int'}),
                 ('DP05_0006PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!10 to 14 years',
                   'predicateType': 'int'}),
                 ('DP05_0007E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!15 to 19 years',
                   'predicateType': 'int'}),
                 ('DP05_0007M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!15 to 19 years',
                   'predicateType': 'int'}),
                 ('DP05_0007PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!15 to 19 years',
                   'predicateType': 'int'}),
                 ('DP05_0007PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!15 to 19 years',
                   'predicateType': 'int'}),
                 ('DP05_0008E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!20 to 24 years',
                   'predicateType': 'int'}),
                 ('DP05_0008M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!20 to 24 years',
                   'predicateType': 'int'}),
                 ('DP05_0008PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!20 to 24 years',
                   'predicateType': 'int'}),
                 ('DP05_0008PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!20 to 24 years',
                   'predicateType': 'int'}),
                 ('DP05_0009E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!25 to 34 years',
                   'predicateType': 'int'}),
                 ('DP05_0009M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!25 to 34 years',
                   'predicateType': 'int'}),
                 ('DP05_0009PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!25 to 34 years',
                   'predicateType': 'int'}),
                 ('DP05_0009PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!25 to 34 years',
                   'predicateType': 'int'}),
                 ('DP05_0010E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!35 to 44 years',
                   'predicateType': 'int'}),
                 ('DP05_0010M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!35 to 44 years',
                   'predicateType': 'int'}),
                 ('DP05_0010PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!35 to 44 years',
                   'predicateType': 'int'}),
                 ('DP05_0010PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!35 to 44 years',
                   'predicateType': 'int'}),
                 ('DP05_0011E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!45 to 54 years',
                   'predicateType': 'int'}),
                 ('DP05_0011M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!45 to 54 years',
                   'predicateType': 'int'}),
                 ('DP05_0011PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!45 to 54 years',
                   'predicateType': 'int'}),
                 ('DP05_0011PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!45 to 54 years',
                   'predicateType': 'int'}),
                 ('DP05_0012E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!55 to 59 years',
                   'predicateType': 'int'}),
                 ('DP05_0012M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!55 to 59 years',
                   'predicateType': 'int'}),
                 ('DP05_0012PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!55 to 59 years',
                   'predicateType': 'int'}),
                 ('DP05_0012PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!55 to 59 years',
                   'predicateType': 'int'}),
                 ('DP05_0013E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!60 to 64 years',
                   'predicateType': 'int'}),
                 ('DP05_0013M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!60 to 64 years',
                   'predicateType': 'int'}),
                 ('DP05_0013PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!60 to 64 years',
                   'predicateType': 'int'}),
                 ('DP05_0013PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!60 to 64 years',
                   'predicateType': 'int'}),
                 ('DP05_0014E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 to 74 years',
                   'predicateType': 'int'}),
                 ('DP05_0014M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 to 74 years',
                   'predicateType': 'int'}),
                 ('DP05_0014PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 to 74 years',
                   'predicateType': 'int'}),
                 ('DP05_0014PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 to 74 years',
                   'predicateType': 'int'}),
                 ('DP05_0015E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!75 to 84 years',
                   'predicateType': 'int'}),
                 ('DP05_0015M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!75 to 84 years',
                   'predicateType': 'int'}),
                 ('DP05_0015PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!75 to 84 years',
                   'predicateType': 'int'}),
                 ('DP05_0015PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!75 to 84 years',
                   'predicateType': 'int'}),
                 ('DP05_0016E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!85 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0016M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!85 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0016PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!85 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0016PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!85 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0017E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Median age (years)',
                   'predicateType': 'int'}),
                 ('DP05_0017M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Median age (years)',
                   'predicateType': 'int'}),
                 ('DP05_0017PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Median age (years)',
                   'predicateType': 'int'}),
                 ('DP05_0017PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!Median age (years)',
                   'predicateType': 'int'}),
                 ('DP05_0018E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0018M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0018PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0018PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0019E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!21 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0019M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!21 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0019PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!21 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0019PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!21 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0020E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!62 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0020M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!62 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0020PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!62 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0020PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!62 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0021E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0021M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0021PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0021PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0022E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0022M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0022PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0022PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0023E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0023M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0023PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0023PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0024E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0024M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0024PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0024PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!18 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0025E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0025M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0025PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0025PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over',
                   'predicateType': 'int'}),
                 ('DP05_0026E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0026M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0026PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0026PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0027E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0027M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0027PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0027PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'SEX AND AGE!!Total population!!65 years and over!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0028E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0028M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0028PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0028PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0029E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0029M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0029PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0029PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0030E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0030M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0030PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0030PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Total population!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0031E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0031M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0031PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0031PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race',
                   'predicateType': 'int'}),
                 ('DP05_0032E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!White',
                   'predicateType': 'int'}),
                 ('DP05_0032M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!White',
                   'predicateType': 'int'}),
                 ('DP05_0032PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!White',
                   'predicateType': 'int'}),
                 ('DP05_0032PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!White',
                   'predicateType': 'int'}),
                 ('DP05_0033E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0033M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0033PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0033PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0034E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0034M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0034PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0034PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0035E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Cherokee tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0035M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Cherokee tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0035PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Cherokee tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0035PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Cherokee tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0036E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Chippewa tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0036M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Chippewa tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0036PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Chippewa tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0036PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Chippewa tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0037E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Navajo tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0037M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Navajo tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0037PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Navajo tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0037PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Navajo tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0038E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Sioux tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0038M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Sioux tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0038PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Sioux tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0038PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!American Indian and Alaska Native!!Sioux tribal grouping',
                   'predicateType': 'int'}),
                 ('DP05_0039E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0039M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0039PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0039PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0040E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Asian Indian',
                   'predicateType': 'int'}),
                 ('DP05_0040M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Asian Indian',
                   'predicateType': 'int'}),
                 ('DP05_0040PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Asian Indian',
                   'predicateType': 'int'}),
                 ('DP05_0040PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Asian Indian',
                   'predicateType': 'int'}),
                 ('DP05_0041E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Chinese',
                   'predicateType': 'int'}),
                 ('DP05_0041M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Chinese',
                   'predicateType': 'int'}),
                 ('DP05_0041PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Chinese',
                   'predicateType': 'int'}),
                 ('DP05_0041PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Chinese',
                   'predicateType': 'int'}),
                 ('DP05_0042E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Filipino',
                   'predicateType': 'int'}),
                 ('DP05_0042M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Filipino',
                   'predicateType': 'int'}),
                 ('DP05_0042PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Filipino',
                   'predicateType': 'int'}),
                 ('DP05_0042PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Filipino',
                   'predicateType': 'int'}),
                 ('DP05_0043E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Japanese',
                   'predicateType': 'int'}),
                 ('DP05_0043M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Japanese',
                   'predicateType': 'int'}),
                 ('DP05_0043PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Japanese',
                   'predicateType': 'int'}),
                 ('DP05_0043PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Japanese',
                   'predicateType': 'int'}),
                 ('DP05_0044E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Korean',
                   'predicateType': 'int'}),
                 ('DP05_0044M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Korean',
                   'predicateType': 'int'}),
                 ('DP05_0044PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Korean',
                   'predicateType': 'int'}),
                 ('DP05_0044PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Korean',
                   'predicateType': 'int'}),
                 ('DP05_0045E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Vietnamese',
                   'predicateType': 'int'}),
                 ('DP05_0045M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Vietnamese',
                   'predicateType': 'int'}),
                 ('DP05_0045PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Vietnamese',
                   'predicateType': 'int'}),
                 ('DP05_0045PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Vietnamese',
                   'predicateType': 'int'}),
                 ('DP05_0046E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Other Asian',
                   'predicateType': 'int'}),
                 ('DP05_0046M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Other Asian',
                   'predicateType': 'int'}),
                 ('DP05_0046PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Other Asian',
                   'predicateType': 'int'}),
                 ('DP05_0046PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Asian!!Other Asian',
                   'predicateType': 'int'}),
                 ('DP05_0047E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0047M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0047PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0047PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0048E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Native Hawaiian',
                   'predicateType': 'int'}),
                 ('DP05_0048M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Native Hawaiian',
                   'predicateType': 'int'}),
                 ('DP05_0048PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Native Hawaiian',
                   'predicateType': 'int'}),
                 ('DP05_0048PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Native Hawaiian',
                   'predicateType': 'int'}),
                 ('DP05_0049E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Guamanian or Chamorro',
                   'predicateType': 'int'}),
                 ('DP05_0049M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Guamanian or Chamorro',
                   'predicateType': 'int'}),
                 ('DP05_0049PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Guamanian or Chamorro',
                   'predicateType': 'int'}),
                 ('DP05_0049PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Guamanian or Chamorro',
                   'predicateType': 'int'}),
                 ('DP05_0050E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Samoan',
                   'predicateType': 'int'}),
                 ('DP05_0050M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Samoan',
                   'predicateType': 'int'}),
                 ('DP05_0050PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Samoan',
                   'predicateType': 'int'}),
                 ('DP05_0050PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Samoan',
                   'predicateType': 'int'}),
                 ('DP05_0051E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0051M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0051PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0051PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Native Hawaiian and Other Pacific Islander!!Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0052E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0052M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0052PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0052PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!One race!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0053E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0053M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0053PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0053PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0054E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0054M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0054PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0054PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0055E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0055M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0055PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0055PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0056E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Asian',
                   'predicateType': 'int'}),
                 ('DP05_0056M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Asian',
                   'predicateType': 'int'}),
                 ('DP05_0056PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Asian',
                   'predicateType': 'int'}),
                 ('DP05_0056PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!White and Asian',
                   'predicateType': 'int'}),
                 ('DP05_0057E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0057M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0057PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0057PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'RACE!!Two or more races!!Black or African American and American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0058E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0058M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0058PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0058PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0059E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!White',
                   'predicateType': 'int'}),
                 ('DP05_0059M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!White',
                   'predicateType': 'int'}),
                 ('DP05_0059PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!White',
                   'predicateType': 'int'}),
                 ('DP05_0059PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!White',
                   'predicateType': 'int'}),
                 ('DP05_0060E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0060M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0060PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0060PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Black or African American',
                   'predicateType': 'int'}),
                 ('DP05_0061E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0061M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0061PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0061PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!American Indian and Alaska Native',
                   'predicateType': 'int'}),
                 ('DP05_0062E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0062M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0062PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0062PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Asian',
                   'predicateType': 'int'}),
                 ('DP05_0063E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0063M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0063PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0063PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Native Hawaiian and Other Pacific Islander',
                   'predicateType': 'int'}),
                 ('DP05_0064E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0064M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0064PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0064PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Race alone or in combination with one or more other races!!Total population!!Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0065E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0065M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0065PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0065PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population',
                   'predicateType': 'int'}),
                 ('DP05_0066E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                   'predicateType': 'int'}),
                 ('DP05_0066M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                   'predicateType': 'int'}),
                 ('DP05_0066PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                   'predicateType': 'int'}),
                 ('DP05_0066PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)',
                   'predicateType': 'int'}),
                 ('DP05_0067E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Mexican',
                   'predicateType': 'int'}),
                 ('DP05_0067M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Mexican',
                   'predicateType': 'int'}),
                 ('DP05_0067PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Mexican',
                   'predicateType': 'int'}),
                 ('DP05_0067PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Mexican',
                   'predicateType': 'int'}),
                 ('DP05_0068E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Puerto Rican',
                   'predicateType': 'int'}),
                 ('DP05_0068M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Puerto Rican',
                   'predicateType': 'int'}),
                 ('DP05_0068PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Puerto Rican',
                   'predicateType': 'int'}),
                 ('DP05_0068PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Puerto Rican',
                   'predicateType': 'int'}),
                 ('DP05_0069E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Cuban',
                   'predicateType': 'int'}),
                 ('DP05_0069M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Cuban',
                   'predicateType': 'int'}),
                 ('DP05_0069PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Cuban',
                   'predicateType': 'int'}),
                 ('DP05_0069PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Cuban',
                   'predicateType': 'int'}),
                 ('DP05_0070E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Other Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0070M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Other Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0070PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Other Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0070PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Hispanic or Latino (of any race)!!Other Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0071E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0071M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0071PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0071PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino',
                   'predicateType': 'int'}),
                 ('DP05_0072E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!White alone',
                   'predicateType': 'int'}),
                 ('DP05_0072M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!White alone',
                   'predicateType': 'int'}),
                 ('DP05_0072PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!White alone',
                   'predicateType': 'int'}),
                 ('DP05_0072PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!White alone',
                   'predicateType': 'int'}),
                 ('DP05_0073E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Black or African American alone',
                   'predicateType': 'int'}),
                 ('DP05_0073M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Black or African American alone',
                   'predicateType': 'int'}),
                 ('DP05_0073PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Black or African American alone',
                   'predicateType': 'int'}),
                 ('DP05_0073PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Black or African American alone',
                   'predicateType': 'int'}),
                 ('DP05_0074E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!American Indian and Alaska Native alone',
                   'predicateType': 'int'}),
                 ('DP05_0074M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!American Indian and Alaska Native alone',
                   'predicateType': 'int'}),
                 ('DP05_0074PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!American Indian and Alaska Native alone',
                   'predicateType': 'int'}),
                 ('DP05_0074PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!American Indian and Alaska Native alone',
                   'predicateType': 'int'}),
                 ('DP05_0075E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Asian alone',
                   'predicateType': 'int'}),
                 ('DP05_0075M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Asian alone',
                   'predicateType': 'int'}),
                 ('DP05_0075PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Asian alone',
                   'predicateType': 'int'}),
                 ('DP05_0075PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Asian alone',
                   'predicateType': 'int'}),
                 ('DP05_0076E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Native Hawaiian and Other Pacific Islander alone',
                   'predicateType': 'int'}),
                 ('DP05_0076M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Native Hawaiian and Other Pacific Islander alone',
                   'predicateType': 'int'}),
                 ('DP05_0076PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Native Hawaiian and Other Pacific Islander alone',
                   'predicateType': 'int'}),
                 ('DP05_0076PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Native Hawaiian and Other Pacific Islander alone',
                   'predicateType': 'int'}),
                 ('DP05_0077E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Some other race alone',
                   'predicateType': 'int'}),
                 ('DP05_0077M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Some other race alone',
                   'predicateType': 'int'}),
                 ('DP05_0077PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Some other race alone',
                   'predicateType': 'int'}),
                 ('DP05_0077PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Some other race alone',
                   'predicateType': 'int'}),
                 ('DP05_0078E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0078M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0078PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0078PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races',
                   'predicateType': 'int'}),
                 ('DP05_0079E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races including Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0079M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races including Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0079PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races including Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0079PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races including Some other race',
                   'predicateType': 'int'}),
                 ('DP05_0080E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races excluding Some other race, and Three or more races',
                   'predicateType': 'int'}),
                 ('DP05_0080M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races excluding Some other race, and Three or more races',
                   'predicateType': 'int'}),
                 ('DP05_0080PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races excluding Some other race, and Three or more races',
                   'predicateType': 'int'}),
                 ('DP05_0080PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'HISPANIC OR LATINO AND RACE!!Total population!!Not Hispanic or Latino!!Two or more races!!Two races excluding Some other race, and Three or more races',
                   'predicateType': 'int'}),
                 ('DP05_0081E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Total housing units',
                   'predicateType': 'int'}),
                 ('DP05_0081M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Total housing units',
                   'predicateType': 'int'}),
                 ('DP05_0081PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Total housing units',
                   'predicateType': 'int'}),
                 ('DP05_0081PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'Total housing units',
                   'predicateType': 'int'}),
                 ('DP05_0082E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population',
                   'predicateType': 'int'}),
                 ('DP05_0082M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population',
                   'predicateType': 'int'}),
                 ('DP05_0082PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population',
                   'predicateType': 'int'}),
                 ('DP05_0082PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population',
                   'predicateType': 'int'}),
                 ('DP05_0083E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0083M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0083PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0083PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Male',
                   'predicateType': 'int'}),
                 ('DP05_0084E',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0084M',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0084PE',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Female',
                   'predicateType': 'int'}),
                 ('DP05_0084PM',
                  {'concept': 'ACS DEMOGRAPHIC AND HOUSING ESTIMATES',
                   'label': 'CITIZEN, VOTING AGE POPULATION!!Citizen, 18 and over population!!Female',
                   'predicateType': 'int'})])



After identifying the relevant variables, we download and describe the
data, and compute the percent 65+ similarly to how we did so before,
except now the computation is somewhat simpler:

.. code:: ipython3

    county65plus = censusdata.download('acs5', '2015', censusdata.censusgeo([('county', '*')]),
                                       ['DP05_0001E', 'DP05_0014PE', 'DP05_0015PE', 'DP05_0016PE',],
                                       tabletype='profile')
    county65plus.describe()




.. raw:: html

    <div>
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
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
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
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
    <style>
        .dataframe thead tr:only-child th {
            text-align: right;
        }
    
        .dataframe thead th {
            text-align: left;
        }
    
        .dataframe tbody tr th {
            vertical-align: top;
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
          <th>Real County, Texas: Summary level: 050, state:48&gt; county:385</th>
          <td>3356</td>
          <td>34.0</td>
        </tr>
        <tr>
          <th>Lancaster County, Virginia: Summary level: 050, state:51&gt; county:103</th>
          <td>11129</td>
          <td>33.9</td>
        </tr>
        <tr>
          <th>Sierra County, New Mexico: Summary level: 050, state:35&gt; county:051</th>
          <td>11615</td>
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
          <th>Sarasota County, Florida: Summary level: 050, state:12&gt; county:115</th>
          <td>392038</td>
          <td>33.1</td>
        </tr>
        <tr>
          <th>Northumberland County, Virginia: Summary level: 050, state:51&gt; county:133</th>
          <td>12304</td>
          <td>33.1</td>
        </tr>
        <tr>
          <th>McIntosh County, North Dakota: Summary level: 050, state:38&gt; county:051</th>
          <td>2759</td>
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
