#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 08:17:25 2018

@author: thakur
"""

def filter_mi(df_feature,df_target):
    
    print("This method shows how much do we know about target variable given by one variable")
    print("It evaluates P(X,Y) and P(X) and P(Y) If X and Y are independent their Mutual Information is zero")
    print("Not to use doesn't provide much information")
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.feature_selection import mutual_info_classif,mutual_info_regression
    from sklearn.feature_selection import SelectKBest, SelectPercentile
    
    mi=mutual_info_classif(df_feature.fillna(0),df_target)
    mi = pd.Series(mi)
    mi.index=df_feature.columns
    mi.sort_values(ascending=False).plot.bar(figsize=(25,12))
       
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def filter_fischer(df_feature,df_target):
    print("Measure dependency of two variables")
    print("It is good for categorical variables")
    print("Target should be binary, which is expected to be output of feature engineering")
    
    
    print("Important Note :")
    print("It is considered that all categorical variables are encoded")
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.feature_selection import chi2
    from sklearn.feature_selection import SelectKBest, SelectPercentile
    
    f_score=chi2(df_feature.fillna(0),df_target)
    
    p_values=pd.Series(f_score[1])
    p_values.index=df_feature.columns
    p_values=p_values.sort_values()
    
    print("Low p values says more significant is feature to predict the target")
    print("A note here is small p values doesn't always say that feature is important but it also shows sample size is very high")
    print("So it is good to compare output of this with other methods and take a call on importance of features")
    
    return p_values



    

    
    
    
    
    
    
    
    
    
    
    
    
def filter_univariate(df_feature,df_target,type=None):
    print("Measure the dependence of two variables --> ANOVA")
    print("It is good for continous variables,Requires binary target but using SKLEARN we can do for continous also")
    print("Assumes linear relation betwen target and variable")
    print("Assumes feature to be of Random distribution and it is sensitive to sample size")
    
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.feature_selection import f_classif,f_regression
    from sklearn.feature_selection import SelectKBest, SelectPercentile
    
    if type=='classification':
    
       univariate=f_classif(df_feature.fillna(0),df_target)
       

    
   elif type== 'regression':
       
        univariate=f_regression(df_feature.fillna(0),df_target)
    
    
    
    
    
   univariate=pd.Series(univariate[1])
   univariate.index=df_feature.columns
   univariate.sort_values(ascending=True,inplace=True)
       
   univariate.sort_values(ascending=False).plot.bar(figsize=(25,12))
       
   print('Bigger the p-value poorer the feature in predicting target correctly')
   print('You can choose p-value to be less than 0.05 but have a look at the data')
   print("Like f score p-values could be small for sample having large size so make sure to compare with other method's outcome")
           
    
    
    
    
    
def filter_uni_ml(df_feature,df_target,type=None):
    
    print("Measure the dependence of two variables using ML")
    print("Suited for all types of features")
    print("Works on distribution of all types")
    
    print('It creates tree for each feature to predict target and then using evaluation metrics best one is ranked highest in this manner each feature is ranked')
    import matplotlib.pyplot as plt
    import seaborn as sns
    from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
    from sklearn.metrics import roc_auc_score,mean_squared_error
    
    if type == 'regression':
        
        roc_vals =[]
        
        for feature in df_feature.columns:
            
            clf=DecisionTreeRegressor()
            clf.fit(df_feature[feature].na_fill(0).to_frame(),df_target,)
            y_score=clf.predict_proba(df_feature[feature].fillna(0).to_frame())
            roc_values.append(mean_squared_error(df_target,y_score))
            
            
        roc_values=pd.Series(roc_values,index=df_feature.columns)
        roc_values.sort_values(ascending=True,inplce=True)
        
        
        roc_values.sort_values(ascending=False).plot.bar(fig_size=(25,12))
        
        print('Lower the MSE better is the feature for prediction')
        
        
        
    elif type=='classification':
        
        roc_vals =[]
        
        for feature in df_feature.columns:
            
            clf=DecisionTreeClassifier()
            clf.fit(df_feature[feature].na_fill(0).to_frame(),df_target,)
            y_score=clf.predict_proba(df_feature[feature].fillna(0).to_frame())
            roc_values.append(roc_auc_score(df_target,y_score[:,1]))
            
            
        roc_values=pd.Series(roc_values,index=df_feature.columns)
        roc_values.sort_values(ascending=False,inplce=True)
        
        
        roc_values.plot.bar(fig_size=(25,12))
        
        
        
        
        print("Values below or equal to .5 shows very poor prediction using this classifier, But above are important classifier")
   
    return roc_values
    
    
    