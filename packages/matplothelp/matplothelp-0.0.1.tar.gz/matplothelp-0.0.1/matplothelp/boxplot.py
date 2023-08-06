print("1")
"""
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
df = pd.read_csv("AirQualityUCI.csv", sep = ";", decimal = ",")
print("ÄirQualityUCI data before iloc")
print(df.head())
df = df.iloc[ : ,0:14]
print("ÄirQualityUCI data after iloc")
print(df.head())
print('Length of the dataset',len(df))
print('Null values in dataset\n',df.isna().sum())
print('Null values of date column',df['Date'].isna().sum())
df = df[df['Date'].notnull()]
print('Length of the dataset after deleting null value rows',len(df))
print('Null values in dataset\n',df.isna().sum())
df['DateTime']=df.Date+ ' '+df.Time
print('Data type of newly create DateTime feature',type(df['DateTime']))
print('Date Time variable',df['DateTime'].head())
import datetime
df.DateTime = df.DateTime.apply(lambda x: datetime.datetime.strptime(x, '%d/%m/%Y%H.%M.%S'))
print (type(df.DateTime[0]))
print('Date Time variable',df['DateTime'].head())
df.index = df.DateTime
print('\n\n First 5 rows of dataset\n',df.head())
box_plot_data = [df['C6H6(GT)'],df['T']]
mtp.boxplot(box_plot_data)
mtp.show()
"""
