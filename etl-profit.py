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

#Create shipment table 
cursor.execute("""CREATE TABLE dim_profit(
    profit_key INT IDENTITY(1,1) PRIMARY KEY,
    order_item_product_price FLOAT,
    order_item_profit_ratio FLOAT,
    order_item_quantity INT,
    order_item_total FLOAT,
    order_profit_per_order FLOAT
    )"""
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        """INSERT INTO [dbo].[dim_profit](
            order_item_product_price,
            order_item_profit_ratio,
            order_item_quantity,
            order_item_total,
            order_profit_per_order
            ) 
            VALUES (?, ?, ?, ?, ?);
        """, 
        row.order_item_product_price,
        row.order_item_profit_ratio,
        row.order_item_quantity,
        row.order_item_total,
        row.order_profit_per_order
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()