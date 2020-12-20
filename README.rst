This package is designed to provide easy access to the U.S. Census Bureau's
API (https://www.census.gov/developers/) in Python. It supports pulling data
from the American Community Survey (ACS) and the Census Summary File,
specifically:

* ACS 5-year estimates (2005-2009 to 2015-2019),
* ACS 1-year estimates (2012-2019),
* ACS 3-year estimates (2010-2012 to 2011-2013),
* ACS 1-year supplemental estimates (2014-2019),
* Census 2010 Summary File 1.

This package handles the details of interacting with the Census API for you,
so that you can focus on working with the data. It provides a class for
representing Census geographies. It also provides functions
for gaining further information about specific variables and tables and
for searching for variables. Full documentation is available at
https://jtleider.github.io/censusdata/.

The ACS (https://www.census.gov/programs-surveys/acs/)
started in 2005. It provides information on a wide range of social, economic,
demographic, and housing characteristics. Topics covered include
income, employment, health insurance, the age distribution, and education, among
many others. The ACS replaces the old Census long form, which used to be
distributed to a subset of households responding to the decennial Census.
The ACS produces survey-based period estimates. For instance, the
5-year 2011-2015 estimates are based on data collected during all 5 years.
They are not simply an aggregate of 1-year estimates, and overlapping
5-year estimates (e.g., 2008-2012 and 2011-2015) should *not* be compared.
The ACS provides margins of error to accompany all estimates. Margins of
error are smaller for estimates based on more years of data.

ACS 5-year estimates are the least current but provide the greatest precision
and are available for geographies of all sizes
(https://www.census.gov/programs-surveys/acs/guidance/estimates.html). By
contrast, 1-year estimates are the most current but the least precise and are
only available for geographies with populations of 65,000+.
In between are the 1-year supplemental estimates or, in past years, the
3-year estimates, both of which are for geographies with populations of
20,000+. The choice of which ACS estimates to use will depend on your needs
for current data vs. data for a variety of geographies with greater
precision.

The decennial Census counts every resident of the United States. The 2010
Census Summary File 1 provides information about each community's population,
including age, sex, and race distributions, as well as information
on households and families. (Summary File 2 provides additional data
for specific racial/ethnic groups.)

There are a number of facilities available for downloading Census
data, including American FactFinder, the ACS summary files,
and the Census DataFerrett. This package is designed to provide
the following features not available elsewhere:

* Easy download of specific variables across a variety of tables, downloading only the variables you need for the geographies of interest to you. This bypasses data processing hassles associated with working with other sources like the ACS Summary Files.
* Access to the exact variables of interest, with variable names making it easy to look up further information on the source tables or to pull up other years of data. This facilitates work by more technical users.
* Download data for multiple geographies at once, such as all counties in the United States, or all block groups in Illinois.
* Work with the data as a Pandas data frame, or export to CSV for analysis in other data analysis packages.
