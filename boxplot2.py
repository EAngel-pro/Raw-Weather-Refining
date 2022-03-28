# -*- coding: utf-8 -*-
"""
Created on Sun Dec 6 03:34:16 2020

@author: Ethan
"""

#Purpose: Create box plot for period 2 data
#Name: Ethan Angel
#Date: 12/6/20
import pandas as pd
import matplotlib.pyplot as plt
df2 = pd.read_csv("formatdata.csv")
df2.boxplot(); plt.suptitle('Period 2 box plot')
plt.show()
print(df2.info())
print(df2.describe())
print("Median is ",df2.median())