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
        df = random_costs.create_df()
        print(df)
    def import_data(self):
        df = pd.read_excel(COST_FILE, header=[0, 1])
        print(df)

