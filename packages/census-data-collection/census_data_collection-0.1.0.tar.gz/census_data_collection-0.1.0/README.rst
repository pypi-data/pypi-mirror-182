census_collection
===============
A package improving the data collection process from United States Census Bureaus's API).

The package is built upon `census 0.8.19 <https://pypi.org/project/census/#files>`_.

Additional features of this package:

* collect yearly (e.g., 2021) or multi-year data (e.g., 2016-2021) from Census Bureaus' API (particularly, American Community Survey) and transform them into structured long-format dataframe automatically
* simplified parameter input


Install
============
::

  pip install example-publish-pypi-medium

Usage and Example
=====

First, get yourself a `Census API key <https://api.census.gov/data/key_signup.html>`_.
::

  api_key = your_API_key
Then, decide the following parameters:

*  estimates method (1-year, 3-year and 5-year estimates, for the differences in estimates, please refer to this `document <https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch03.pdf>`_); for example:
::

   est = 1 #1-year estimates
   est = 5 #5-year estimate
 
* variable dictionary: keys are the variable name in Census databases, values are the p re of the variable name you want to rename (the variable name in the databases are meaningless); for example: 
::  

   var_dict = {'B19013_001E':'income','B01003_001E':'total_population'}
   
find out all variables using https://api.census.gov/data/[year]/acs/[estimate]/variables.html (e.g., https://api.census.gov/data/2021/acs/acs5/variables.html)

* geographic setting: the geographic area of which data you want to collect (please refer to this file for `geographic areas covered in Census <https://www.census.gov/content/dam/Census/library/publications/2020/acs/acs_general_handbook_2020_ch02.pdf>`_; for example:
::

   geo_setting = 'state: *' #collect data from all states
   geo_setting = 'county: *' #collect data from all counties
   
   #to get fip codes of each state:
   import us
   us.states.[state].fips 


Now, you are ready to collect initatiate an object for collecting data
::

    from censuscollection import ACS_data
    
    ACS_data(1, var_dict, geo_setting, api_key)

Next, you may choose to collect single-year data or multi-year data

:: 

   example = ACS_data(1, var_dict, geo_setting, api_key)
  
   example.collect_data_yearly(2021) #collect 2021 data 
  
   import numpy as np
   year_range = np.arange(2010, 2016)
   example.collect_data_multi_years(np.arange)#collect data from 2010 to 2015


The functions above will return a long-format dataframe (with geo-location and year information):

* the example output for collecting single-year data

.. image:: images/single_year.png

* the example output for collecting multi-year data

.. image:: images/multi_year.png

