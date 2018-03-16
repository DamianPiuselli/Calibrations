# -*- coding: utf-8 -*-
"""
Multiple linear calibration
y = m1*x1 + m1*x1 + ... + b
y = señal
xi = concentraciones
mx = f. de respuesta
"""

import statsmodels.api as sm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.sandbox.regression.predstd import wls_prediction_std


# Cargando los datos desde excel usando pandas.

df = pd.read_excel("dataset calibracion linear multiple.xlsx")
y_data = df["señal"]
x_data = df[["concentracion 1", "concentracion 2", "concentracion 3"]]

# Modelo

x_data = sm.add_constant(x_data)   # agrega la ordenada al origen (b)

model = sm.OLS(y_data, x_data).fit()
predictions = model.predict(x_data)
print(model.summary())

# Graficos

#prstd, iv_l, iv_u = wls_prediction_std(model)
#
#fig, ax = plt.subplots(figsize=(8,6))
#
#ax.plot(x_data, y_data, 'o', label="data")
#ax.plot(x_data, model.fittedvalues, 'r--.', label="OLS")
#ax.plot(x_data, iv_u, 'r--')
#ax.plot(x_data, iv_l, 'r--')
#ax.legend(loc='best');

prstd, iv_l, iv_u = wls_prediction_std(model)

fig, ax = plt.subplots(figsize=(8,6))

ax.plot(x_data["concentracion 1"], y_data, 'o', label="data")
ax.plot(x_data["concentracion 1"], model.fittedvalues, 'o', label="OLS")
#ax.plot(x_data["concentracion 1"], iv_u, 'r--')
#ax.plot(x_data["concentracion 1"], iv_l, 'r--')
ax.legend(loc='best');
