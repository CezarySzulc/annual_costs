# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:36:21 2017

@author: C
"""

import pandas as pd
import numpy as np

CATEGORIES = ['Housing Expenses', 
              'Auto and Transportation Expenses', 
              'Household Expenses',
              'Living Essentials',
              'Life Style']
VALUES = [['Mortgage Payment',
           'Home Insurance and Maintenance Cost'],
          ['Auto Loan Payment',
           'Auto Insurance Payment',
           'Fuel Cost',
           'Maintenance and Repair',
           'Other Fees'],
           ['Monthly Gas and Electricity',
           'Monthly Alarm System',
           'Monthly Water, Sewer and Garbage',
           'Monthly Cell Phone, Home Phone, Internet and TV',
           'Monthly Home Decoration',
           'Monthly House Keeping & Cleansing',
           'Other'],
           ['Monthly Grocery Cost',
            'Monthly Clothing Cost',
            'Monthly Personal Care',
            'Monthly Medications / Supplements',
            'Monthly Life Insurance & Long-Term Care',
            'Monthly Child Care',
            'Monthly Child Activities',
            'Monthly Pet Care',
            'Other'],
            ['Dining Out',
             'Movies / Theatre / Museum',
             'Monthly Fitness, Hobbies & Collections Cost',
             'Monthly Vacation Cost',
             'Monthly Gift / Donation Cost',
             'Monthly Books, Magazines, Tuition & Classes',
             'Monthly Electronics',
             'Other']]
DATA_SIZE = 1000
             
def create_data_time_index(data_size):
    """ create list with DataTime type"""

    day = np.random.randint(1, 29, size=data_size)
    month = np.random.randint(1, 13, size=data_size)
    year = np.random.randint(2016, 2018, size=data_size)
    dates = np.column_stack([day, month, year])
    dates = ['{}-{}-{}'.format(date[0], date[1], date[2]) for date in dates]
    dates = pd.to_datetime(dates)
    
    return dates

def create_random_values(data_size):
    """ create numpy array with random values for DataFrame """
    category_size = len(sum(VALUES, []))
    data = np.random.randint(1,100, size=(category_size * data_size))
    data = data.reshape(data_size, category_size)
    
    return data
            
def create_df(keys=CATEGORIES, values=VALUES, data_size=DATA_SIZE):
    """ create DataFrame with multi columns,
        all values are set random """
    
    dictionary = [(category, value) 
                    for index, category in enumerate(keys) 
                    for value in values[index]]
    index = create_data_time_index(data_size)
    data = create_random_values(data_size)
    df = pd.DataFrame(data=data, columns=dictionary, index=index)
    #set MultiIndex
    df.columns = pd.MultiIndex.from_tuples(df.columns)
    df.sort_index(inplace=True)
    
    return df
    
def create_excel_file(df):
    """ create excel from DataFrame
        and save it in project dictionary """
    
    df.to_excel('annual_random_costs.xls')   

if __name__ == '__main__':
    df = create_df()
    create_excel_file(df)
