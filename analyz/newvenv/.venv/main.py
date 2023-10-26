import sqlite3
from matplotlib import pyplot as plt
import psycopg2
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
connection = psycopg2.connect(
    database="analiz_dannykh",
    user="postgres",
    password="Teshebayev",
    host="localhost",
    port=5432,
)
if connection:
    print("connection is set...")
else:
    print("connection is not set...")
query = "select * from mtcars"



df = pd.read_sql_query(query, connection)
print(df)

##(3Checking the types of data)
 df=df.dtypes 
 print(df)

##(#4Dropping irrelevant columns) 
 df = df.drop(['disp', 'hp', 'drat','wt'] ,axis=1)
 df.head(5)
 print(df)

# #5(Renaming the columns)
 df = df.rename(columns={"model": "models", "cyl": "cylinders" })
 df.head(5)
 print(df)

##6(Удаление повторяющихся строк)
 duplicate_rows_df = df[df.duplicated()]
 print("number of duplicate rows: ", duplicate_rows_df.shape,)
 df=df.count()
 df = df.drop_duplicates()
 df.head(5)
 print(df)

#7Dropping the missing or null values
print(df.isnull().sum()) 
df = df.dropna()   
df.count()
print(df) 
print(df.isnull().sum())

#8Detecting Outliers
df = df.drop(['model'], axis=1)
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
df.shape
print(df)


##9 Plot different features against one another (scatter), against frequency (histogram)

df.model.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
plt.title("cars") # титл гистограммы
plt.ylabel('cylinder') # у осьі атауы
plt.xlabel('models') # ч осьі атауы
plt.show() # гистограмма көрінуі үшін