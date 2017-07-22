This package is designed to provide easy access to the U.S. Census Bureau's API (https://www.census.gov/developers/)
in Python. Currently, this package only supports data from the most recent
(2015) American Community Survey (ACS) 1- and 5-year estimates. I plan to add
support for other years of ACS data, as well as 3-year estimates (which were
discontinued but were produced in the past). I also plan to add support
for other Census data sources, starting with the decennial census.

The American Community Survey (https://www.census.gov/programs-surveys/acs/)
started in 2005. It produces estimates
based on survey samples, and replaces the old Census long form. It
provides period estimates, e.g., the 2011-2015 5-year estimates provide
estimates for community characteristics during that entire period. The
5-year estimates are not averages of 1-year estimates. The 5-year estimates
are more precise than the 1-year estimates, and are available for smaller
communities than the 1-year estimates, because they are based on more
data. The ACS provides data on a wide variety of demographic, economic,
housing, commuting, income, and related variables for communities
across the United States, down to the block group level and up
to the national level.

There are a number of facilities available for downloading Census
data, including American FactFinder, the ACS summary files,
and the Census DataFerrett. This package is designed to provide
the following features not available elsewhere:

* Easy download of specific variables across a variety of tables, downloading only the variables you need for the geographies of interest to you. This bypasses data processing hassles associated with working with other sources like the ACS Summary Files.
* Access to the exact variables of interest, with variable names making it easy to look up further information on the source tables or to pull up other years of data. This facilitates work by more technical users.
* Download data for multiple geographies at once, such as all counties in the United States, or all block groups in Illinois.
* Work with the data as a Pandas data frame, or export to CSV for analysis in other data analysis packages.
