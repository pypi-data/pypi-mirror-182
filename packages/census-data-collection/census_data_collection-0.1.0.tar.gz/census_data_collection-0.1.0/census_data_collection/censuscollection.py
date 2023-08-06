#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SCRIPT FOR COllECTING & PROCESSING American Community Survey/CENSUS BUREA DATA
@ author: Jinyan Xiang

Goal: collect 1-year estimate and 5-year estimate data on 

"""


import warnings

from census import Census
import pandas as pd


warnings.filterwarnings("ignore")

class ACS_data:
    
    ''' 
    Create a Class - ACS_data for collecting different ACS data for different research projects
    
    '''
    
    #c = Census("2ce6be4a8f71a52336616ae611a7979c33880c8b")
    
    def __init__(self, est, var_dict, geo_setting, api_key): #  Intialize data collections
    
        """
        
        Attributes
        ----------
        est : INTEGAR: 1, 3, or 5
            estimation method ACS used: 1 year, 3 year (discountinued), 5 year
                see this link for details: https://www.census.gov/programs-surveys/acs/guidance/estimates.html
        
        var_dict : DICTIONARY
            keys are the variable labels in ACS that are interest and will be collected
            values are the variables names
        
        geo_setting : TUPLE
            geographic criteria for data collection: state, county, etc
                see this link for details: https://pypi.org/project/CensusData/

        """
        self.est = est
        self.var_dict = var_dict
        self.geo_setting = geo_setting
        self.api_key = api_key
    
    def collect_data_yearly(self, year):
        
        
        """
        
        Parameters
        ----------
        year : INTEGAR
             the year of data that is interested and will be collected
        
        Return
        ----------
        DATAFRAME, the collected data for the corresponding year
        """
        key = self.api_key
        c = Census(key)
        
        geo_dict = {'GEO_ID': 'GEO_ID', 'NAME': 'GEO_NAME'}
        full_dict = {**geo_dict, **self.var_dict}
        
        if self.est == 1:
            method = c.acs1
        if self.est == 3:
            method = c.acs3
        if self.est == 5:
            method = c.acs5
            
        data_yearly_raw = method.get(list(full_dict.keys()),
                                 {'for':self.geo_setting},
                                 year = year)

        data_yearly = pd.DataFrame(data_yearly_raw)
        
        var_name_new = map(lambda x: x + '_' + str(self.est)+'y_est',list(self.var_dict.values()))
        var_dict_new = dict(zip(list(self.var_dict.keys()), list(var_name_new)))
        full_dict_new = {**geo_dict, **var_dict_new}
        
        data_yearly.rename(columns = full_dict_new, inplace = True)
        
        if self.geo_setting.split(':')[0] in ['state', 'State']:
            data_yearly['state'] = data_yearly['GEO_NAME']
        
        if self.geo_setting.split(':')[0] in ['county', 'County']:
            data_yearly['state'] = data_yearly['GEO_NAME'].apply(lambda x:x.split(',')[1])
            data_yearly['county'] = data_yearly['GEO_NAME'].apply(lambda x:x.split(',')[0])
        
        data_yearly['year'] = year

        
        return data_yearly
        
    def collect_data_multi_years(self, year_range):
        """
        
        Parameters
        ----------
        year_range : LIST of years
             the years of data that are interested and will be collected
        
        Return
        ----------
        DATAFRAME, the collected data for the corresponding years
        """
        
        data_multi_years = pd.DataFrame()
        
        for year in year_range:
            data_multi_years = data_multi_years.append(self.collect_data_yearly(year))
        
        return data_multi_years