# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 15:26:32 2018

@author: Toshiba-PC
"""

import pandas as pd
import json
import numpy

# exportation 
expoDataIdr = pd.read_csv('IndiceGlobal.csv', sep=',', encoding = "ISO-8859-1")

# Lenna
first = expoDataIdr.iloc[:, [0,1,2,3]]
second = expoDataIdr.iloc[:, [0,4,5,6]]
third = expoDataIdr.iloc[:, [0,7,8,9]]

first.to_csv('evolProjet.csv')
second.to_csv('evolInves.csv')
third.to_csv('evolEmploi.csv')


expoDataCh = pd.read_csv('chomage.csv', sep=',', encoding = "ISO-8859-1")

tauxChomage = expoDataCh[['gouvernorat', 'chomage']]
tauxIdr = expoDataIdr[['gouvernorat', 'IDR']]

tauxChomage['gouvernorat'] = tauxChomage['gouvernorat'].str.upper()

result = pd.merge(tauxChomage, tauxIdr, on=['gouvernorat'])
    
print(tauxIdr.sort_values(['IDR']))

json.dumps(numpy.asscalar(tauxChomage.at[0, 'Chomage']))
type(82)
print((tauxChomage.at[0, 'Chomage']))
type(numpy.asscalar(tauxChomage.at[0, 'Chomage']))

tauxChomage.loc[tauxChomage['Regions'] == "Gouvernorat de Tunis"][['Chomage']].to_string(index=False)

