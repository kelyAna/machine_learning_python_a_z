# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:56:53 2020

@author: lopes
"""

from sklearn.preprocessing import StandardScaler
import numpy as np
import pickle


svm = pickle.load(open('svm_finalizado.sav','rb'))
random_forest = pickle.load(open('random_finalizado.sav', 'rb'))
mlp = pickle.load(open('mlp_finalizado.sav', 'rb'))

scaler = StandardScaler()

novo_registro = [[50000, 40, 5000]]
novo_registro = np.asarray(novo_registro)
novo_registro = novo_registro.reshape(-1,1)
novo_registro = scaler.fit_transform(novo_registro)
novo_registro = novo_registro.reshape(-1,3)

resposta_svm = svm.predict(novo_registro)
resposta_random = random_forest.predict(novo_registro)
resposta_mlp = mlp.predict(novo_registro)

paga = 0
n_paga = 0

if resposta_svm[0] == 1:
    paga =+ 1
else:
    n_paga += 1


if resposta_random[0] == 1:
    paga =+ 1
else:
    n_paga += 1


if resposta_mlp[0] == 1:
    paga =+ 1
else:
    n_paga += 1

if paga > n_paga:
    print('Cliente pagara o emprestimo')
elif paga == n_paga:
    print('Resultado empatado')
else:
    print('Cliente não pagará o emprestimo')