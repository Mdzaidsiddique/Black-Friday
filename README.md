# Black-Friday
In this repository, I have done Exploratory Data Analysis and feature engineering for Black Friday Dataset by using
### Pandas, Matplotlib and Seaborn.

### importing the dataset

import pandas as pd

black_friday = pd.read_csv('C:/Users/masoo/Downloads/black friday - Copy.csv')

black_friday.head()

![image](https://user-images.githubusercontent.com/87862008/139216761-ec5d9f30-f1a0-4b29-a3d1-afd3742543ce.png)


### number of rows and columns 

black_friday.shape

#### Number of rows in dataset:  537577
#### Number of columns in dataset:  12

black_friday.columns

['User_ID', 'Product_ID', 'Gender', 'Age', 'Occupation', 'City_Category',
       'Stay_In_Current_City_Years', 'Marital_Status', 'Product_Category_1',
       'Product_Category_2', 'Product_Category_3']
       
### checking null values

black_friday.isnull().sum()

black_friday.isnull().sum().mean()*100

black_friday.isnull().sum()

black_friday.isnull().sum().mean()*100

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

sns.heatmap(black_friday.isnull(), yticklabels=False, cbar = False, cmap = 'viridis')

plt.title('Null Values present in the dataset',fontsize=14)

plt.show()

![image](https://user-images.githubusercontent.com/87862008/139220278-2dc99309-e486-4800-8619-638b36b986e5.png)

### Most of the values in column Product_Category_2 and Product_Category_3 are missing 
### The 'User_ID' column is of no use in describing the dataset and we dont need product category 3 column becouse 70 % data is missing, so that i am going to remove 'User_ID' and 'Product_Category_3' column.

black_friday.drop('Product_Category_3',axis = 1, inplace = True)

Histogram of features in the dataset

sns.set_style('whitegrid')

black_friday.drop('User_ID',axis=1).hist(figsize = (13,10), color = 'darkgreen')

plt.tight_layout()

plt.show()

![image](https://user-images.githubusercontent.com/87862008/139221458-fc7aac7e-3883-465f-a409-45718503db99.png)


## Correlation matrix of features in the dataset

plt.figure(figsize=(10,6))

sns.heatmap(black_friday.corr(), annot = True, cmap='coolwarm',linewidths=1)

plt.show()

![image](https://user-images.githubusercontent.com/87862008/139222806-6973d7a1-a6de-47a0-bc37-80df946cb64c.png)

### fill null value

black_friday.Product_Category_2.fillna(0, inplace = True)

black_friday.Product_Category_3.fillna(0, inplace = True)

### check unique values 

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

![image](https://user-images.githubusercontent.com/87862008/139217455-0eae388d-c093-4e04-aaa8-34b8f205cadf.png)

black_friday.Stay_In_Current_City_Years.unique()

black_friday.Stay_In_Current_City_Years.value_counts()

sns.catplot(data = black_friday, x = 'Stay_In_Current_City_Years', kind = 'count')

![image](https://user-images.githubusercontent.com/87862008/139217556-c10036df-d30c-4848-b8ca-0c50d0656b8c.png)

### marital status- descrete data

black_friday.Marital_Status.nunique()

black_friday.Marital_Status.value_counts()

sns.catplot(data = black_friday, x = 'Marital_Status', kind = 'count')

plt.figure(figsize=(10,6))

![image](https://user-images.githubusercontent.com/87862008/139217658-1c83c8c2-3e7e-4770-b99f-567807b4bcfd.png)

### column product category 1

black_friday.Product_Category_1.isnull().sum()

black_friday.Product_Category_1.value_counts()

black_friday.Product_Category_1.nunique()
