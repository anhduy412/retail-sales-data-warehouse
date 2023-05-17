import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df

#Connect Python to SQL Server
server = config.server
database = config.database
username = config.username
password = config.password

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')
cursor = conn.cursor()

#Create a new dataframe to avoid inserting duplicate data
temp_df = df[['order_item_product_price', 'order_item_profit_ratio', 'order_item_quantity', 'order_item_total', 'order_profit_per_order']].values.tolist()
profit_df = []
for x in temp_df:
    if x not in profit_df:
        profit_df.append(x)
profit_df = pd.DataFrame(profit_df, columns=['order_item_product_price', 'order_item_profit_ratio', 'order_item_quantity', 'order_item_total', 'order_profit_per_order'])
# print(profit_df)

#Create shipment table 
cursor.execute("""CREATE TABLE dim_profit(
    profit_key INT IDENTITY(1,1) PRIMARY KEY,
    order_item_product_price FLOAT,
    order_item_profit_ratio FLOAT,
    order_item_quantity INT,
    order_item_total FLOAT,
    order_profit_per_order FLOAT,
    sales_per_customer FLOAT,
    )"""
)

# Insert DataFrame to Table
for row in profit_df.itertuples():
    cursor.execute(
        """INSERT INTO [dbo].[dim_profit](
            order_item_product_price,
            order_item_profit_ratio,
            order_item_quantity,
            order_item_total,
            order_profit_per_order,
            sales_per_customer
            ) 
            VALUES (?, ?, ?, ?, ?, ?);
        """,
        row.order_item_product_price,
        row.order_item_profit_ratio,
        row.order_item_quantity,
        row.order_item_total,
        row.order_profit_per_order,
        row.sales_per_customer
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()