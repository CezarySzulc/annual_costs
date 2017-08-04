# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:03:56 2017

@author: C
"""

import random_costs
import matplotlib.pyplot as plt
import pandas as pd

COST_FILE = 'annual_random_costs.xls'

class raport():
    def create_data(self):
        """ create new random values """
        df = random_costs.create_df()
        
        return df
        
    def import_data(self , file_name=COST_FILE):
        """ import data from xls file """
        try:
            df = pd.read_excel(file_name, header=[0, 1])
        except FileNotFoundError:
            print('File does not exist')
        else:
            return df
    
    def display_monthly_costs(df):
        pass

costs_raport = raport()
df = costs_raport.import_data()
#print(df.shape)