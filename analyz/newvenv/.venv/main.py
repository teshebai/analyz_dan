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



#2 MTCARS таблицасын оку және оны датафрейм түрінде  шыгару
df = pd.read_sql_query(query, connection)
# print(df)

##(3Checking the types of data)менде mtcars жүйесінде белгілі бағандардың типтерін анықтадым. Ол бойынша 8 int 3 float 1 object типіндегі бағандар бар. 

# df=df.dtypes 
# print(df)

##(#4Dropping irrelevant columns) Мен бұл датафреймның ДРОП функциясы арқылы DISP HP DRAT WT атаулы, өзіме керек емес бағандарын өшіріп тастадым.
## Axis функциясы кай осьтен удалить ету керек екенін білдіреді 

# df = df.drop(['disp', 'hp', 'drat','wt'] ,axis=1)
# df.head(5)
# print(df)

# #5(Renaming the columns) Rename функциясы арқылы таблицадағы түсініксіз немесе ұзақ бағандардың атауын өзімізге ыңғайлы етіп өзгертуге болады. Мен model бағанын models, cyl бағаны атауын cylinders етіп өзгерттім

# df = df.rename(columns={"model": "models", "cyl": "cylinders" })
# df.head(5)
# print(df)

##6(Удаление повторяющихся строк)Данныйлар үлкен болғандықтан дупликат керек емес кате данныйлар да ышынде болады. Соларды түзету үшін, анықтап, оларды жою үшін төмендегі функцияларды қолдандым.
## df.shape функиясы аркылы х у осьтерынде дупликаттарды санап береды
## дроп функциясы аркылы оларды жоямыз

# duplicate_rows_df = df[df.duplicated()]
# print("number of duplicate rows: ", duplicate_rows_df.shape,)
# df=df.count()
# df = df.drop_duplicates()
# df.head(5)
# print(df)

# #7Dropping the missing or null values
# print(df.isnull().sum()) #0дык немесе бос багандар туралы акпарат шыгарамыз
# df = df.dropna()    # Бос немесе калып койган данныйларды ошыремыз
# df.count()
# print(df) 
# print(df.isnull().sum()) # өщкеннен  соң данныйларды шығарамыз 

# #8Detecting Outliers
# df = df.drop(['model'], axis=1)
# Q1 = df.quantile(0.25)
# Q3 = df.quantile(0.75)
# IQR = Q3 - Q1
# print(IQR)
# df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
# df.shape
# print(df)


##9 Plot different features against one another (scatter), against frequency (histogram)

# df.model.value_counts().nlargest(40).plot(kind='bar', figsize=(10,5))
# plt.title("cars") # титл гистограммы
# plt.ylabel('cylinder') # у осьі атауы
# plt.xlabel('models') # ч осьі атауы
# plt.show() # гистограмма көрінуі үшін