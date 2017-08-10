# -*- coding: utf-8 -*-
"""
@author: C
"""

import random_costs, seaborn 
import matplotlib.pyplot as plt
import pandas as pd


COST_FILE = 'annual_random_costs.xls'
DATA_SIZE = 1000

class Raport():
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
        
        self.df_month = df.resample('M').sum()
        df_month = self.df_month.copy()
        df_month.sum(axis=1).plot(ax=axis[0], marker = '.')
        
        axis[0].set_title('Sum of costs')
        axis[0].grid(b='on', which='major', color='k', linewidth=.5)
        axis[0].grid(b='on', which='minor', color='k', linewidth=.25)
        df_month.columns = df_month.columns.droplevel(1)
        for index, category in enumerate(df_month.columns.unique(), start=1):
            df_month[category].sum(axis=1).plot(ax=axis[index], marker = '.')
            axis[index].set_title(category)
            axis[index].grid(b='on', which='major', color='k', linewidth=.5)
            axis[index].grid(b='on', which='minor', color='k', linewidth=.25)
            
        plt.show()
     
        
if __name__ == '__main__':
    costs_raport = Raport(DATA_SIZE)
    df = costs_raport.import_data()
    costs_raport.display_monthly_costs(df)
