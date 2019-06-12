#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:05:02 2018

@author: thakur
"""

###### Duplicate features Elimination #########

def remove_duplicate(df):
    
    print('not splitting train test as believed to be done in previous step')
    
    duplicated_features=[]
    
    for i in range(len(df.columns)):
        
        if i%10==0:
            print(i)
            
        col1=df.columns[i]
        
        for col2 in df.columns[i+1]:
            
            if df[col1].equals(df[col2]):
                duplicated_features.append(col2)
                
                
    df.drop(labels=duplicated_features,axis=1,inplace=True)
    
    
    return df,duplicated_features
