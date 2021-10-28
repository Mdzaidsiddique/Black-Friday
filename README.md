# Black-Friday
In this repository, I have done Exploratory Data Analysis for Black Friday Dataset and try to identify relationship between a Purchase Price and other various features
import pandas as pd
black_friday = pd.read_csv('C:/Users/masoo/Downloads/black friday - Copy.csv')
black_friday.head()
![image](https://user-images.githubusercontent.com/87862008/139216761-ec5d9f30-f1a0-4b29-a3d1-afd3742543ce.png)
black_friday.columns
black_friday.isnull().sum()
black_friday.isnull().sum().mean()*100
black_friday.Product_Category_2.fillna(0, inplace = True)
black_friday.Product_Category_3.fillna(0, inplace = True)
### we dont need product category 3 column becouse 70 % data is missing, so i am going to drop product category 3
black_friday.drop('Product_Category_3',axis = 1, inplace = True)
black_friday.Gender.unique()
black_friday.Gender.value_counts()
black_friday.Age.value_counts()
black_friday.Age.duplicated().sum()
black_friday.Age.unique()
black_friday.Age = black_friday.Age.str.replace('0-17','26-35').replace('26-35','18-25').replace("18-25", "< 35").replace('36-50','46-50').replace('46-50','51-55').replace('51-55','55+').replace('55+','>35')
import seaborn as sns
sns.catplot( data = black_friday, x ='Age', kind = 'count')
![image](https://user-images.githubusercontent.com/87862008/139216450-d4d50dee-68ee-41e7-8bb4-f430d6f8b22a.png)
black_friday.info()
### column occupation is descrete data
black_friday.City_Category.unique()
black_friday.City_Category.value_counts()
sns.catplot(data = black_friday, x = 'City_Category', kind = 'count')

