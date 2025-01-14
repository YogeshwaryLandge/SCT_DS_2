# -*- coding: utf-8 -*-
"""Task 2 Internship

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/13knj8MA5rUxyqwq1vf_fer-Vu2HMkf4t
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv("/content/train.csv")
df

df.head()

df.tail()

df.info()

df.nunique()

df.isnull().sum()

(df.isnull().sum()/(len(df)))*100

df = df.drop(['PassengerId'], axis = 1)
df.info()

df.describe().T

df.describe(include='all').T

cat_cols = df.select_dtypes(include=['object']).columns
num_cols = df.select_dtypes(include=np.number).columns.tolist()
print("Categorical Variables:")
print(cat_cols)
print("Numerical Variables:")
print(num_cols)

for col in num_cols:
    print(col)
    print('Skew :', round(df[col].skew(), 2))
    plt.figure(figsize = (15, 4))
    plt.subplot(1, 2, 1)
    df[col].hist(grid=False)
    plt.ylabel('count')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df[col])
    plt.show()

plt.figure(figsize=(13,17))
sns.pairplot(data=df.drop(['Age','Fare'],axis=1))
plt.show()

