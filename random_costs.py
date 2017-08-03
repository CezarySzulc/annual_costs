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
DATA_SIZE = 1
             
def create_data_time_index(data_size):
    """ create list with DataTime type"""

    day = np.random.randint(1, 29, size=data_size)
    month = np.random.randint(1, 13, size=data_size)
    year = np.random.randint(2016, 2018, size=data_size)
    dates = np.column_stack([day, month, year])
    dates = ['{}-{}-{}'.format(date[0], date[1], date[2]) for date in dates]
    dates = pd.to_datetime(dates)
    
    return dates

def create_random_values():
    """ create numpy array with random values for DataFrame """
    
    x = np.random.randint(1,100, size=31)
    x = x.reshape(1,31)
    
    return x
            
def create_df(keys, values, data_size):
    """ create DataFrame with multi columns,
        all values are set random """
    
    dictionary = [(category, value) 
                    for index, category in enumerate(keys) 
                    for value in values[index]]
    index = create_data_time_index(data_size)
    data = create_random_values()
    df = pd.DataFrame(data=data, columns=dictionary, index=index)
    df.sort_index(inplace=True)
    
    return df
    


df = create_df(CATEGORIES, VALUES, DATA_SIZE)
print(df.shape)

print(len(VALUES))
''' push random values into DataFrame '''