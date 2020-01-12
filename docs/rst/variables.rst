==============================================================
Variables
==============================================================

--------------------------------------------------------------
American Community Survey 1-, 3-, and 5-Year Estimates
--------------------------------------------------------------

The American Community Survey (ACS) provides four different sets of data
tables:

* **Detailed tables.** These provide the most detailed set of variables. Table
  names begin with B followed by a numeric code. 
* **Data profile tables.** These tables are designed to provide information
  on a broad array of characteristics for a given geography. There are data profile tables on:
	- Social Characteristics (DP02),
	- Economic Characteristics (DP03),
	- Housing Characteristics (DP04), and
	- Demographic Characteristics (DP05).
  Table names (beginning in DP) are shown in parentheses above.
* **Subject tables.** These tables are designed to provide information on
  narrower topics for a broader range of geographies. Table names
  begin with S.
* **Comparison profile tables.** These tables provide information on changes
  in characteristics in particular geographies over time, including statistical
  significance testing. Table names begin with CP.

(Note that this package does not support the new Selected population profile tables
for the 1-year estimates.)

The detailed tables are documented in the Summary File Table Shells, available
from the ACS Summary File Documentation:
https://www.census.gov/programs-surveys/acs/technical-documentation/summary-file-documentation.html
This provides data on available variables on a table-by-table basis, and
specifies which data releases (1-, 3-, or 5-year estimates) the variable is
available for. Each table specifies the universe for which it provides
estimates, and includes a total value (denominator) in addition to specific
estimates out of that total (numerators). For instance, in the ACS 2015 5-year
estimates, table B01001 provides estimates of population by sex and age. The
universe for this table is the total population, and variable B01001_001
provides the estimated total. By contrast, a variable like B01001_010 provides
the estimated male population aged 22 to 24.  To compute the percentage of the
population that is male aged 22 to 24, we would divide B01001_010 by B01001_001.
It is important to use the denominator from the specific table you are using
when performing such computations. While estimates should of the same total
should generally be the same across tables, in practice they sometimes differ
slightly, so it is important to use consistent values.

Information on the data profile and subject tables is available from
https://www.census.gov/acs/www/data/data-tables-and-tools/. Table shells
for selected years for the data profile, subject, and comparison profile
tables are available from American FactFinder
(https://www.census.gov/acs/www/data/data-tables-and-tools/american-factfinder/).
Unfortunately, these do not include variable names, unlike the detailed table
shells.

*Note about annotation fields.* The Census has recently updated the API for the
ACS 1- and 5-year estimates to include separate annotation fields for each
variable. The main data variables (e.g., B01001_001E from the detailed tables)
will now contain numeric data exclusively, while any text annotations providing
notes about the data will be placed in annotation fields with names ending in 'A'
(e.g., B01001_001EA). It is important to refer to the annotation fields for
relevant notes about the data (e.g., if data are missing due to too few sample
observations).

--------------------------------------------------------------
American Community Survey 1-Year Supplemental Estimates
--------------------------------------------------------------
The ACS 1-year supplemental estimates supplement the 1-year estimates by
providing estimates for all geographies with a population of 20,000+,
as opposed to 65,000+ for the regular 1-year estimates. There are
separate tables for the 1-year supplemental estimates. Table names begin
with K20. Table shells are available for 2014-2016 under
https://www2.census.gov/programs-surveys/acs/tech_docs/table_shells/
Unfortunately, unlike the detailed tables for the regular 1-year estimates,
there is no single spreadsheet containing all the table shells.

--------------------------------------------------------------
Census 2010 Summary File 1
--------------------------------------------------------------

Extensive information on the Summary File 1 data is available under
https://www.census.gov/newsroom/releases/archives/2010_census/press-kits/summary-file-1.html
In particular, the technical documentation, currently available under
https://www.census.gov/prod/cen2010/doc/sf1.pdf,
provides detailed information on the tables and variables that are available.

----------------------------------------------------------------------
Obtaining Information on Variables Through the `censusdata` package
----------------------------------------------------------------------

The `censusdata` package provides several functions for finding information
on tables and variables for these data sets:

* `censustable` provides information on entire tables. `printtable` is also
  provided to format this information.
* `censusvar` provides information on individual variables.
* `search` can be used to search for variables based on regular
  expression matching.

