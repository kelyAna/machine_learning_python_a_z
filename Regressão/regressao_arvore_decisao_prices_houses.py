# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 17:41:08 2020

@author: lopes
"""

import pandas as pd

df = pd.read_csv('house_prices.csv')

X = df.iloc[:, 3:19].values
y = df.iloc[:, 2].values

from sklearn.model_selection import train_test_split
X_treinamento, X_teste, y_treinamento, y_teste = train_test_split(X,y,
                                                                  test_size = 0.3,
                                                                  random_state = 0)

from sklearn.tree import DecisionTreeRegressor
regressor = DecisionTreeRegressor()
regressor.fit(X_treinamento, y_treinamento)
score = regressor.score(X_treinamento, y_treinamento)

previsoes = regressor.predict(X_teste)

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_teste, previsoes)

regressor.score(X_teste, y_teste)

