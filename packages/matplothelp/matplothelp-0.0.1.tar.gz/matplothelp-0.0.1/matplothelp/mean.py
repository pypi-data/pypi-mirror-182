print("1")
"""
import numpy as nm
import matplotlib.pyplot as mtp
import pandas as pd
df = pd.read_csv("AirQualityUCI.csv", sep = ";", decimal = ",")
df = df.iloc[ : ,0:14]
print("ÄirQualityUCI data after iloc")
print(df.head())
print('Length of the dataset',len(df))
print('Null values in dataset\n',df.isna().sum())
print('Null values of date column',df['Date'].isna().sum())
df = df[df['Date'].notnull()]
print('Length of the dataset after deleting null value rows',len(df))
print('Null values in dataset\n',df.isna().sum())
print('Mean of Temprature T=',df['T'].mean())
print('Maximum Temprature T=',max(df['T']))
print('Minimum Temprature T=',min(df['T']))
print('Standard Deviation of Temprature T=',nm.std(df['T']))
"""