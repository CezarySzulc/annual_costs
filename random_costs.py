# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:36:21 2017

@author: C
"""

import pandas as pd

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
             
             
def create_df(keys, values):
    """create DataFrame with multi columns"""
    dictionary = {(category, value): [0] 
                    for index, category in enumerate(keys) 
                    for value in values[index]}
    df = pd.DataFrame(dictionary)
    
    return df

create_df(CATEGORIES, VALUES)
#df = pd.read_csv('liveing_expences_by_categories.txt', sep='\t', index_col=0, names=['Categories'], header=0)
#print(df.head())