#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 06:31:41 2018

@author: thakur
"""

def rm_correlated(df,y_train,removal_startegy='rf',thresh_rf=None,thresh_brute=None):
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.ensemble import RandomForestClassifier
    col_corr=set()
    print("""Expected to be done after feature preprocessing categorical variables
      are encoded using one hot encoder""")  
    corrmat=df.corr()
        
    fig,ax=plt.subplots()
    fig.set_size_inches(15,15)
    sns.heatmap(corrmat)
    
    
    if removal_strategy =='brute':
        
        for i in range(corrmat.columns):
            for j in range(i):
                if abs(corrmat.iloc[i,j])>thresh_brute:
                    colname=corrmat.columns[i]
                    
                    col_corr.add(colname)
                    
    elif removal_startegy=='rf' :
        
        corrmat=corrmat.abs().unstack()
        corrmat=corrmat.sort_values(ascending=False)
        corrmat=corrmat[corrmat>thresh_rf]
        corrmat=corrmat[corrmat<1]
        corrmat=pd.Dataframe(corrmat).reset_index()
        corrmat.columns=['feature1','feature2','corr']
        
        
        
        grouped_features=[]
        corr_group=[]
        
        for feature in corrmat.feature1.unique():
            
            if feature not in grouped_features:
                
                corr_block=corrmat[corrmat.feature1=feature]
                grouped_features=grouped_features+list(corr_block.feature2.unique()+[feature])
                
                corr_group.append(corr_block)
                
                
                
        keep_features=[]       
        for group in corr_group:
            
            feature=list(group.feature1.unique())+list(group.feature2.unique())
            
            rf=RandomForestClassifier(n_estimators=200,random_state=45,max_depth=5)
            
            rf.fit(X_train[features].fillna(0),y_train)
            
            importance=pd.concat(
                    [pd.Series(features),pd.Series(rf.feature_importance)],axis=1)
            
            importance.columns=['feature','importance']
            importance.sort_values(by='importance',ascending=False)
            
            keep_features.append(importance.iloc[0,0])
            
            
            
    return col_corr,keep_features


        
        
                    
                    
    
        
        
        
        