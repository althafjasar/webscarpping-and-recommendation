# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 22:11:09 2020

@author: Jasar Althaf
"""

import pandas as pd
import numpy as np

df=pd.read_csv('data.csv',encoding='utf8')

df.head()


tot=df.url.values+"***" +df.summary.values


def fun(length,tot):
    data=[]
    
    for i in range(length):
        data.append({
            'userid':np.random.randint(0,100),
            'text':np.random.choice(tot),
            'No_of_visit':np.random.randint(0,10)
            
        })
    
    return pd.DataFrame(data)   
            

data=fun(1000,tot)

data[['url','summary']] = data.text.apply(lambda x: pd.Series(str(x).split("***")))

data.drop('text',axis=1,inplace=True)


data.to_csv('data.csv')