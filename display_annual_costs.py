# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:03:56 2017

@author: C
"""

import random_costs, seaborn 
import matplotlib.pyplot as plt
import pandas as pd


COST_FILE = 'annual_random_costs.xls'
DATA_SIZE = 1000

class raport():
    def __init__(self, data_size):
        self.data_size = data_size
        
    def create_data(self):
        """ create new random values """
        
        df = random_costs.create_df(data_size=self.data_size)
        
        return df
        
    def import_data(self , file_name=COST_FILE):
        """ import data from xls file """
        
        try:
            df = pd.read_excel(file_name, header=[0, 1])         
        except FileNotFoundError:
            print('File does not exist, your data was generated randomly')
            df = self.create_data()
        finally:
            return df
    
    def display_monthly_costs(self, df):
        """ display DataFrame with costs sum of month """        
        
        seaborn.set()
        fig, axis = plt.subplots(nrows=6, sharex=True)
        
        df_month = df.resample('M').sum()
        df_month.sum(axis=1).plot(ax=axis[0], marker = '.')
        
        axis[0].set_title('Sum of costs')

        df_month.columns = df_month.columns.droplevel(1)
        for index, category in enumerate(df_month.columns.unique(), start=1):
            df_month[category].sum(axis=1).plot(ax=axis[index], marker = '.')
            axis[index].set_title(category)
            
        plt.show()
        

costs_raport = raport(DATA_SIZE)
df = costs_raport.import_data()
#print(df.head())
costs_raport.display_monthly_costs(df)
#print(df.shape)
