#Understanding variables
#Cleaning Dataset
#Analysing Relationship b/w Variables

import pandas as pd
import numpy as np

df=pd.read_csv("indian_liver_patient.csv")

print(df)

print(df.shape) #View the no.of columns and rows

print(df.head()) #It will print first 5 datas

print(df.tail()) #It will print Last 5 datas

print(df.columns) #print the column names

print(df.describe()) #Print the statistical value like minimum value,Mean,standard deviation

print(df.isnull().sum()) #Show all the null values

#print(df.fillna(1,inplace=True)) #fill all the null value as 1

print(df.dropna(inplace=True)) #Remove the null value and the data will changed as 579 from 583

print(df.shape)


# We have to change catagorial value to binary

print(df.Gender.unique()) #To find the unique values like male,female

print(df.nunique(axis=0)) #axis=1 -->Row vise & axis=0 -->column vise


print(df.Gender.value_counts()) #To print how many male and female present 

import seaborn as sns
#outlayers- e.g 50,45,35,80,90,500,1000

print(sns.boxplot(x=df['Direct_Bilirubin']))

#To remove outlayers

df_clean=df[df['Direct_Bilirubin'].between(0,1.5)]

print(df_clean.shape)

print(sns.boxplot(x=df_clean['Direct_Bilirubin']))




