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
discount_df1 = config.discount_df1

#Create a new dataframe to avoid inserting duplicate data
temp_df = discount_df1[['order_item_discount', 'order_item_discount_rate', 'sales']].values.tolist()
discount_df = []
for x in temp_df:
    if x not in discount_df:
        discount_df.append(x)
discount_df = pd.DataFrame(discount_df, columns=['order_item_discount', 'order_item_discount_rate', 'sales'])
# print(discount_df)

#Create discount  table 
cursor.execute("""
    CREATE TABLE dim_discount(
        discount_key INT IDENTITY(1,1) PRIMARY KEY, 
        order_item_discount FLOAT,
        order_item_discount_rate FLOAT
    )"""
)
conn.commit()

# Insert DataFrame to Table
for row in discount_df.itertuples():
    cursor.execute("""
        INSERT INTO [dbo].[dim_discount](
            order_item_discount,
            order_item_discount_rate
        )
        VALUES (?, ?)
        """, 
        row.order_item_discount,
        row.order_item_discount_rate
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()