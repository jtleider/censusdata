
Example 3: Downloading State Data
=================================

For this example, we will be running a simple linear regression model,
so we need an additional import:

.. code:: ipython3

    import pandas as pd
    import censusdata
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.precision', 2)
    import statsmodels.formula.api as sm

We begin by downloading data on some basic socioeconomic characteristics
for all U.S. states:

.. code:: ipython3

    statedata = censusdata.download('acs5', 2015, censusdata.censusgeo([('state', '*')]),
                                    ['B01001_001E', 'B19013_001E', 'B19083_001E',
                                     'C17002_001E', 'C17002_002E', 'C17002_003E', 'C17002_004E',
                                     'B03002_001E', 'B03002_003E', 'B03002_004E', 'B03002_012E',])

We then link data on the percent of voters in each state voting
Democratic in the 2016 U.S. presidential election:

.. code:: ipython3

    voting2016 = {
        censusdata.censusgeo((('state', '01'),)): 34.6,
        censusdata.censusgeo((('state', '02'),)): 37.7,
        censusdata.censusgeo((('state', '04'),)): 45.4,
        censusdata.censusgeo((('state', '05'),)): 33.8,
        censusdata.censusgeo((('state', '06'),)): 61.6,
        censusdata.censusgeo((('state', '08'),)): 47.2,
        censusdata.censusgeo((('state', '09'),)): 54.5,
        censusdata.censusgeo((('state', '10'),)): 53.4,
        censusdata.censusgeo((('state', '11'),)): 92.8,
        censusdata.censusgeo((('state', '12'),)): 47.8,
        censusdata.censusgeo((('state', '13'),)): 45.6,
        censusdata.censusgeo((('state', '15'),)): 62.3,
        censusdata.censusgeo((('state', '16'),)): 27.6,
        censusdata.censusgeo((('state', '17'),)): 55.4,
        censusdata.censusgeo((('state', '18'),)): 37.9,
        censusdata.censusgeo((('state', '19'),)): 42.2,
        censusdata.censusgeo((('state', '20'),)): 36.2,
        censusdata.censusgeo((('state', '21'),)): 32.7,
        censusdata.censusgeo((('state', '22'),)): 38.4,
        censusdata.censusgeo((('state', '23'),)): 47.9,
        censusdata.censusgeo((('state', '24'),)): 60.5,
        censusdata.censusgeo((('state', '25'),)): 60.8,
        censusdata.censusgeo((('state', '26'),)): 47.3,
        censusdata.censusgeo((('state', '27'),)): 46.9,
        censusdata.censusgeo((('state', '28'),)): 39.7,
        censusdata.censusgeo((('state', '29'),)): 38,
        censusdata.censusgeo((('state', '30'),)): 36,
        censusdata.censusgeo((('state', '31'),)): 34,
        censusdata.censusgeo((('state', '32'),)): 47.9,
        censusdata.censusgeo((('state', '33'),)): 47.6,
        censusdata.censusgeo((('state', '34'),)): 55,
        censusdata.censusgeo((('state', '35'),)): 48.3,
        censusdata.censusgeo((('state', '36'),)): 58.8,
        censusdata.censusgeo((('state', '37'),)): 46.7,
        censusdata.censusgeo((('state', '38'),)): 27.8,
        censusdata.censusgeo((('state', '39'),)): 43.5,
        censusdata.censusgeo((('state', '40'),)): 28.9,
        censusdata.censusgeo((('state', '41'),)): 51.7,
        censusdata.censusgeo((('state', '42'),)): 47.6,
        censusdata.censusgeo((('state', '44'),)): 55.4,
        censusdata.censusgeo((('state', '45'),)): 40.8,
        censusdata.censusgeo((('state', '46'),)): 31.7,
        censusdata.censusgeo((('state', '47'),)): 34.9,
        censusdata.censusgeo((('state', '48'),)): 43.4,
        censusdata.censusgeo((('state', '49'),)): 27.8,
        censusdata.censusgeo((('state', '50'),)): 61.1,
        censusdata.censusgeo((('state', '51'),)): 49.9,
        censusdata.censusgeo((('state', '53'),)): 54.4,
        censusdata.censusgeo((('state', '54'),)): 26.5,
        censusdata.censusgeo((('state', '55'),)): 46.9,
        censusdata.censusgeo((('state', '56'),)): 22.5,
    }
    voting2016 = pd.DataFrame.from_dict(voting2016, orient='index')
    statedata['percent_democratic_pres_2016'] = voting2016

We then rename columns, compute some additional variables, and rescale
some variables to make regression coefficients more easily
interpretable:

.. code:: ipython3

    statedata = statedata.rename(columns={'B01001_001E': 'population_size'})
    statedata.population_size = statedata.population_size / 100000
    statedata = statedata.rename(columns={'B19013_001E': 'median_HH_income'})
    statedata['median_HH_income'] = statedata['median_HH_income'] / 1000
    statedata = statedata.rename(columns={'B19083_001E': 'gini_index'})
    statedata.gini_index = statedata.gini_index * 100
    statedata['percent_below_125_poverty'] = (statedata['C17002_002E'] + statedata['C17002_003E'] + statedata['C17002_004E']) / statedata['C17002_001E'] * 100
    statedata['percent_nonhisp_white'] = statedata['B03002_003E'] / statedata['B03002_001E'] * 100
    statedata['percent_nonhisp_black'] = statedata['B03002_004E'] / statedata['B03002_001E'] * 100
    statedata['percent_hispanic'] = statedata['B03002_012E'] / statedata['B03002_001E'] * 100

We run a quick check on the data and then delete variables we no longer
need:

.. code:: ipython3

    assert (statedata['population_size'] == statedata['B03002_001E'] / 100000).all()
    for column in ['C17002_001E', 'C17002_002E', 'C17002_003E', 'C17002_004E',
                   'B03002_001E', 'B03002_003E', 'B03002_004E', 'B03002_012E',]:
        del statedata[column]

We are only interested in the 50 states + DC, so we drop Puerto Rico:

.. code:: ipython3

    statedata = statedata.drop([censusdata.censusgeo([('state', '72')])])

Finally, we reorder the variables and run simple descriptives:

.. code:: ipython3

    statedata = statedata.reindex(columns=['percent_democratic_pres_2016', 'population_size', 'median_HH_income', 'percent_below_125_poverty', 'gini_index', 'percent_nonhisp_white', 'percent_nonhisp_black', 'percent_hispanic'])
    statedata.describe()




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
          <th>percent_democratic_pres_2016</th>
          <th>population_size</th>
          <th>median_HH_income</th>
          <th>percent_below_125_poverty</th>
          <th>gini_index</th>
          <th>percent_nonhisp_white</th>
          <th>percent_nonhisp_black</th>
          <th>percent_hispanic</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>count</th>
          <td>51.00</td>
          <td>51.00</td>
          <td>51.00</td>
          <td>51.00</td>
          <td>51.00</td>
          <td>51.00</td>
          <td>51.00</td>
          <td>51.00</td>
        </tr>
        <tr>
          <th>mean</th>
          <td>45.05</td>
          <td>62.06</td>
          <td>54.64</td>
          <td>19.44</td>
          <td>46.22</td>
          <td>69.53</td>
          <td>10.91</td>
          <td>11.20</td>
        </tr>
        <tr>
          <th>std</th>
          <td>12.41</td>
          <td>70.53</td>
          <td>9.16</td>
          <td>3.94</td>
          <td>2.14</td>
          <td>16.12</td>
          <td>10.77</td>
          <td>10.06</td>
        </tr>
        <tr>
          <th>min</th>
          <td>22.50</td>
          <td>5.80</td>
          <td>39.66</td>
          <td>11.84</td>
          <td>41.81</td>
          <td>22.89</td>
          <td>0.44</td>
          <td>1.37</td>
        </tr>
        <tr>
          <th>25%</th>
          <td>36.10</td>
          <td>17.34</td>
          <td>47.55</td>
          <td>16.25</td>
          <td>44.81</td>
          <td>58.43</td>
          <td>3.17</td>
          <td>4.72</td>
        </tr>
        <tr>
          <th>50%</th>
          <td>46.70</td>
          <td>43.97</td>
          <td>53.00</td>
          <td>20.08</td>
          <td>46.26</td>
          <td>73.60</td>
          <td>7.12</td>
          <td>8.84</td>
        </tr>
        <tr>
          <th>75%</th>
          <td>52.55</td>
          <td>68.46</td>
          <td>60.68</td>
          <td>22.45</td>
          <td>47.59</td>
          <td>81.23</td>
          <td>14.92</td>
          <td>12.88</td>
        </tr>
        <tr>
          <th>max</th>
          <td>92.80</td>
          <td>384.21</td>
          <td>74.55</td>
          <td>28.96</td>
          <td>53.17</td>
          <td>93.88</td>
          <td>47.98</td>
          <td>47.36</td>
        </tr>
      </tbody>
    </table>
    </div>



Then we examine bivariate correlations prior to running a linear
regression model:

.. code:: ipython3

    statedata.corr()




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
          <th>percent_democratic_pres_2016</th>
          <th>population_size</th>
          <th>median_HH_income</th>
          <th>percent_below_125_poverty</th>
          <th>gini_index</th>
          <th>percent_nonhisp_white</th>
          <th>percent_nonhisp_black</th>
          <th>percent_hispanic</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>percent_democratic_pres_2016</th>
          <td>1.00</td>
          <td>0.24</td>
          <td>0.57</td>
          <td>-0.21</td>
          <td>0.47</td>
          <td>-0.53</td>
          <td>0.34</td>
          <td>0.26</td>
        </tr>
        <tr>
          <th>population_size</th>
          <td>0.24</td>
          <td>1.00</td>
          <td>0.03</td>
          <td>0.18</td>
          <td>0.43</td>
          <td>-0.40</td>
          <td>0.11</td>
          <td>0.53</td>
        </tr>
        <tr>
          <th>median_HH_income</th>
          <td>0.57</td>
          <td>0.03</td>
          <td>1.00</td>
          <td>-0.81</td>
          <td>-0.09</td>
          <td>-0.27</td>
          <td>-0.06</td>
          <td>0.11</td>
        </tr>
        <tr>
          <th>percent_below_125_poverty</th>
          <td>-0.21</td>
          <td>0.18</td>
          <td>-0.81</td>
          <td>1.00</td>
          <td>0.48</td>
          <td>-0.23</td>
          <td>0.39</td>
          <td>0.19</td>
        </tr>
        <tr>
          <th>gini_index</th>
          <td>0.47</td>
          <td>0.43</td>
          <td>-0.09</td>
          <td>0.48</td>
          <td>1.00</td>
          <td>-0.45</td>
          <td>0.61</td>
          <td>0.28</td>
        </tr>
        <tr>
          <th>percent_nonhisp_white</th>
          <td>-0.53</td>
          <td>-0.40</td>
          <td>-0.27</td>
          <td>-0.23</td>
          <td>-0.45</td>
          <td>1.00</td>
          <td>-0.46</td>
          <td>-0.63</td>
        </tr>
        <tr>
          <th>percent_nonhisp_black</th>
          <td>0.34</td>
          <td>0.11</td>
          <td>-0.06</td>
          <td>0.39</td>
          <td>0.61</td>
          <td>-0.46</td>
          <td>1.00</td>
          <td>-0.13</td>
        </tr>
        <tr>
          <th>percent_hispanic</th>
          <td>0.26</td>
          <td>0.53</td>
          <td>0.11</td>
          <td>0.19</td>
          <td>0.28</td>
          <td>-0.63</td>
          <td>-0.13</td>
          <td>1.00</td>
        </tr>
      </tbody>
    </table>
    </div>



.. code:: ipython3

    result = sm.ols(formula=("percent_democratic_pres_2016 ~ population_size + median_HH_income"
                             "+ percent_nonhisp_black + percent_hispanic"), data=statedata).fit()
    result.summary()




.. raw:: html

    <table class="simpletable">
    <caption>OLS Regression Results</caption>
    <tr>
      <th>Dep. Variable:</th>    <td>percent_democratic_pres_2016</td> <th>  R-squared:         </th> <td>   0.532</td>
    </tr>
    <tr>
      <th>Model:</th>                         <td>OLS</td>             <th>  Adj. R-squared:    </th> <td>   0.492</td>
    </tr>
    <tr>
      <th>Method:</th>                   <td>Least Squares</td>        <th>  F-statistic:       </th> <td>   13.08</td>
    </tr>
    <tr>
      <th>Date:</th>                   <td>Sat, 15 Sep 2018</td>       <th>  Prob (F-statistic):</th> <td>3.42e-07</td>
    </tr>
    <tr>
      <th>Time:</th>                       <td>18:48:26</td>           <th>  Log-Likelihood:    </th> <td> -180.94</td>
    </tr>
    <tr>
      <th>No. Observations:</th>            <td>    51</td>            <th>  AIC:               </th> <td>   371.9</td>
    </tr>
    <tr>
      <th>Df Residuals:</th>                <td>    46</td>            <th>  BIC:               </th> <td>   381.5</td>
    </tr>
    <tr>
      <th>Df Model:</th>                    <td>     4</td>            <th>                     </th>     <td> </td>   
    </tr>
    <tr>
      <th>Covariance Type:</th>            <td>nonrobust</td>          <th>                     </th>     <td> </td>   
    </tr>
    </table>
    <table class="simpletable">
    <tr>
                <td></td>               <th>coef</th>     <th>std err</th>      <th>t</th>      <th>P>|t|</th>  <th>[0.025</th>    <th>0.975]</th>  
    </tr>
    <tr>
      <th>Intercept</th>             <td>   -5.7076</td> <td>    7.801</td> <td>   -0.732</td> <td> 0.468</td> <td>  -21.409</td> <td>    9.994</td>
    </tr>
    <tr>
      <th>population_size</th>       <td>    0.0121</td> <td>    0.021</td> <td>    0.563</td> <td> 0.576</td> <td>   -0.031</td> <td>    0.055</td>
    </tr>
    <tr>
      <th>median_HH_income</th>      <td>    0.7715</td> <td>    0.138</td> <td>    5.603</td> <td> 0.000</td> <td>    0.494</td> <td>    1.049</td>
    </tr>
    <tr>
      <th>percent_nonhisp_black</th> <td>    0.4551</td> <td>    0.120</td> <td>    3.790</td> <td> 0.000</td> <td>    0.213</td> <td>    0.697</td>
    </tr>
    <tr>
      <th>percent_hispanic</th>      <td>    0.2578</td> <td>    0.151</td> <td>    1.704</td> <td> 0.095</td> <td>   -0.047</td> <td>    0.562</td>
    </tr>
    </table>
    <table class="simpletable">
    <tr>
      <th>Omnibus:</th>       <td> 2.104</td> <th>  Durbin-Watson:     </th> <td>   2.420</td>
    </tr>
    <tr>
      <th>Prob(Omnibus):</th> <td> 0.349</td> <th>  Jarque-Bera (JB):  </th> <td>   1.237</td>
    </tr>
    <tr>
      <th>Skew:</th>          <td> 0.208</td> <th>  Prob(JB):          </th> <td>   0.539</td>
    </tr>
    <tr>
      <th>Kurtosis:</th>      <td> 3.640</td> <th>  Cond. No.          </th> <td>    647.</td>
    </tr>
    </table><br/><br/>Warnings:<br/>[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.



In this simple model, the percentage voting Democratic is not
significantly associated with population size or % Hispanic, at the
p<.05 level. It is significantly associated with median household income
and the % non-Hispanic black. Every $1,000 increase in median household
income is associated with an increase of just under 1 percentage point
in the Democratic vote. Every one percentage point increase in the %
non-Hispanic black is associated with about a half a percentage point
increase in the Democratic vote. Of course,

1. The outcome variable is not continuous, due to its bounded range, and
   this model does not account for this (it is essentially a linear
   probability model);
2. The choice of covariates is simplistic and just designed to
   demonstrate fitting a model;
3. We might consider robust standard errors for this model.
