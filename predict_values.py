# -*- coding: utf-8 -*-
"""
@author: C
"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from display_annual_costs import Raport
import numpy as np


class Predict(Raport):
    def __init__(self):
        self.df = self.import_data()

    def prepare_data(self):
        """ sum all montly costs,
            split data for train and test set """
            
        df_month = self.df.resample('M').sum().sum(axis=1)
        df_month = df_month.reset_index()
        df_month.columns = ['date', 'costs']
        df_month['date'] = df_month['date'].astype(np.int64)
        self.X_train, self.X_test, self.y_train, self.y_test = \
                                train_test_split(
                                    df_month['date'].values.reshape(-1,1), 
                                    df_month['costs'].values.reshape(-1,1), 
                                    test_size=0.3,
                                    random_state=42)
                
    def create_model(self):
        """ creeate model and test it """

        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        score = model.score(self.X_test, self.y_test)
        print("R^2: {}".format(score))

if __name__ == '__main__':       
    cost_predict = Predict()
    cost_predict.prepare_data()
    cost_predict.create_model()