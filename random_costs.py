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
DATA_SIZE = 2
             
def create_data_time_index():
    """ create list with DataTime type"""

    day = np.random.randint(1, 29, size=DATA_SIZE)
    month = np.random.randint(1, 13, size=DATA_SIZE)
    year = np.random.randint(2016, 2018, size=DATA_SIZE)
    dates = np.column_stack([day, month, year])
    dates = ['{}-{}-{}'.format(date[0], date[1], date[2]) for date in dates]
    dates = pd.to_datetime(dates)
    
    return dates

def create_random_values():
    """ create numpy array with random values for DataFrame """
    category_size = len(sum(VALUES, []))
    data = np.random.randint(1,100, size=(category_size * DATA_SIZE))
    data = data.reshape(DATA_SIZE, category_size)
    
    return data
            
def create_df(keys=CATEGORIES, values=VALUES):
    """ create DataFrame with multi columns,
        all values are set random """
    
    dictionary = [(category, value) 
                    for index, category in enumerate(keys) 
                    for value in values[index]]
    index = create_data_time_index()
    data = create_random_values()
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
    df = create_df(CATEGORIES, VALUES)
    create_excel_file(df)
