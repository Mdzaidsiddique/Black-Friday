# Black-Friday
In this repository, I have done Exploratory Data Analysis for Black Friday Dataset and try to identify relationship between a Purchase Price and other various features
import pandas as pd
black_friday = pd.read_csv('C:/Users/masoo/Downloads/black friday - Copy.csv')
black_friday.head()
![head](https://user-images.githubusercontent.com/87862008/139215722-89c640fa-c266-4571-8b11-be7bd0a96b81.png)
black_friday.columns
black_friday.isnull().sum()
black_friday.isnull().sum().mean()*100
black_friday.Product_Category_2.fillna(0, inplace = True)
black_friday.Product_Category_3.fillna(0, inplace = True)
# we dont need product cat 3 column becouse 70 % data is missing, so
black_friday.drop('Product_Category_3',axis = 1, inplace = True)
black_friday.Gender.unique()
black_friday.Gender.value_counts()
black_friday.Age.value_counts()
black_friday.Age.duplicated().sum()
black_friday.Age.unique()
black_friday.Age = black_friday.Age.str.replace('0-17','26-35').replace('26-35','18-25').replace("18-25", "< 35").replace('36-50','46-50').replace('46-50','51-55').replace('51-55','55+').replace('55+','>35')
import seaborn as sns
sns.catplot( data = black_friday, x ='Age', kind = 'count')
