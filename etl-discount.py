import pandas as pd
import pyodbc
import config

#Connect Python to SQL Server
server = config.server
database = config.database
username = config.username
password = config.password

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')
cursor = conn.cursor()

#Import dataframe
df = config.df

#Avoid duplicate
temp_df = df[['order_item_discount', 'order_item_discount_rate', 'sales']].values.tolist()
discount_df = []
for x in temp_df:
    if x not in discount_df:
        discount_df.append(x)
discount_df = pd.DataFrame(discount_df, columns=['order_item_discount', 'order_item_discount_rate', 'sales'])
print(discount_df)

#Create category table 
cursor.execute("""
    CREATE TABLE dim_disount(
        discount_key INT IDENTITY(1,1) PRIMARY KEY, 
        order_item_discount FLOAT,
        order_item_discount_rate FLOAT,
        sales FLOAT
    )"""
)
conn.commit()

# Insert DataFrame to Table
for row in discount_df.itertuples():
    cursor.execute("""
        INSERT INTO [dbo].[dim_disount](
            order_item_discount,
            order_item_discount_rate,
            sales
        )
        VALUES (?, ?, ?)
        """, 
        row.order_item_discount,
        row.order_item_discount_rate,
        row.sales
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()