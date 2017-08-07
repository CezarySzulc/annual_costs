# -*- coding: utf-8 -*-
"""
@author: C
"""

from sklearn.model_selection import train_test_split
from display_annual_costs import raport


class predict(raport):
    def __init__(self):
        self.df = self.import_data()

    def prepare_data(self):
        """ sum all montly costs,
            split data for train and test set """
            
        df_month = self.df.resample('M').sum().sum(axis=1)
        print(df_month)
        #X_train, X_test, y_train, y_test = train_test_split(X, y)
    def test(self):
        print('test')
        
test = predict()
test.test()
test.prepare_data()