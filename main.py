# -*- coding: utf-8 -*-
"""
Multiple linear calibration
y = m1*x1 + m1*x1 + ... + b
y = señal
xi = concentration i
mi = sensibility i
b = constant
"""

import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std


# Loading dummy data.
df = pd.read_excel("dummy data.xls")
y = df["señal"]
x = df[["concentracion 1","concentracion 2"]]

# Defining class Linear Regression (OLS)

class linear:
    """Multiple Linear Regression clas"""    
    def __init__(self, y_data, x_data, constant=True):
        self.Y = y_data
        self.X = x_data
        self.constant = constant
        if self.constant == True:
            self.X = sm.add_constant(self.X)
        
        self.model = sm.OLS(self.Y, self.X)
        self.results = self.model.fit()
        self.summary = self.results.summary()
        
    def ccurve(self):
        
        plt.