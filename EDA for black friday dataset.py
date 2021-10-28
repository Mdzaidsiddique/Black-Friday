# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 16:20:44 2021

@author: masoo
"""

'''
Exploratory Data Analysis of black friday data set
'''
import pandas as pd
black_friday = pd.read_csv('C:/Users/masoo/Downloads/black friday - Copy.csv')
black_friday.head()
black_friday.columns

black_friday.isnull().sum()
black_friday.isnull().sum().mean()*100
black_friday.Product_Category_2.fillna(0, inplace = True)
black_friday.Product_Category_3.fillna(0, inplace = True)
# we dont need product cat 3 column coz 70 % data is missing, so
black_friday.drop('Product_Category_3',axis = 1, inplace = True)

black_friday.Gender.unique()
black_friday.Gender.value_counts()

black_friday.Age.value_counts()
black_friday.Age.duplicated().sum()
black_friday.Age.unique()
black_friday.Age = black_friday.Age.str.replace('0-17','26-35').replace('26-35','18-25').replace("18-25", "< 35").replace('36-50','46-50').replace('46-50','51-55').replace('51-55','55+').replace('55+','>35')
import seaborn as sns
sns.catplot( data = black_friday, x ='Age', kind = 'count')

black_friday.info()
#column occupation is descrete data
black_friday.City_Category.unique()
black_friday.City_Category.value_counts()
sns.catplot(data = black_friday, x = 'City_Category', kind = 'count')

black_friday.Stay_In_Current_City_Years.unique()
black_friday.Stay_In_Current_City_Years.value_counts()
sns.catplot(data = black_friday, x = 'Stay_In_Current_City_Years', kind = 'count')

# marital status- descrete data
black_friday.Marital_Status.nunique()
black_friday.Marital_Status.value_counts()
sns.catplot(data = black_friday, x = 'Marital_Status', kind = 'count')

# column product category 1
black_friday.Product_Category_1.isnull().sum()
black_friday.Product_Category_1.value_counts()
black_friday.Product_Category_1.nunique()

#end of eda