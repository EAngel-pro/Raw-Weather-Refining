################################################################################################
#Histogram
################################################################################################
#Purpose: Create a histogram of humidity data from the second period
#Name: Ethan Angel
#Date: 12/6/20
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.read_csv("formatdata.csv")
df2 = pd.read_csv("formatdata2.csv")
df2['Humidity'].hist(bins=10, alpha=0.5); plt.suptitle('Histogram of Humidity')
plt.show()