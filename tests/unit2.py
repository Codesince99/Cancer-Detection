# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:38:23 2021

@author: Lalit Chauhan
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt

cell_df=pd.read_csv("C:/Users/Lalit Chauhan/Downloads/cell_samples.csv")
cell_df.drop('ID',axis=1,inplace=True)

#Missing Or Null data points

#print(cell_df.isnull().sum())
#print(cell_df.isna().sum())
#print(cell_df.count())
#print(cell_df.columns)
col_names = ['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize', 'BareNuc', 'BlandChrom', 'NormNucl', 'Mit', 'Class']
#for x in col_names: 
 #   print(cell_df[x].nunique())
    
# Let us check whether the dataset is a balanced or imbalanced one.
target_count = cell_df.Class.value_counts()
#print('Benign:', target_count[2])
#print('Malignant:', target_count[4])
cell_df = cell_df[pd.to_numeric(cell_df['BareNuc'],errors='coerce').notnull()]
cell_df['BareNuc']=cell_df['BareNuc'].astype('int')

#print(cell_df.describe().transpose())

feature_df=cell_df[['Clump', 'UnifSize', 'UnifShape', 'MargAdh', 'SingEpiSize',
       'BareNuc', 'BlandChrom', 'NormNucl', 'Mit']]
x=np.asarray(feature_df)
y=np.asarray(cell_df['Class'])

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=4)
#print(x_test)
from sklearn.naive_bayes import GaussianNB
classifier_naive=GaussianNB()
classifier_naive.fit(x_train, y_train)
y_predict=classifier_naive.predict(x_test)

