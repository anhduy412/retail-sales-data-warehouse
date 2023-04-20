import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df

#Connect Python to SQL Server
drivers = config.drivers
server = config.server
database = config.database
username = config.username
password = config.password
 
conn = pyodbc.connect('DRIVER = ' + drivers + '; SERVER = tcp:' + server + '; PORT=1436; DATABASE=' + database + '; UID=' + username +'; PWD='+ password + '; TrustServerCertificate=Yes;')

cursor = conn.cursor()

#Create Table
cursor.execute('''
		CREATE TABLE stg.ITEM (
			order_id NVARCHAR(40) ,
			item_id int,
			product_id nvarchar(40) ,
			seller_id nvarchar(40),
			shipping_limit_date datetime,
			price float,
			freight_value float
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.ITEM (order_id, item_id, product_id,
       seller_id, shipping_limit_date, price, freight_value)
                VALUES (?,?,?,?,?,?,?)
                ''',
                row.order_id,
                row.order_item_id,
                row.product_id,
                row.seller_id,
                row.shipping_limit_date,
                row.price,
                row.freight_value
                )
conn.commit()
cursor.close()