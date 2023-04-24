import pandas as pd
import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df
print(df)

#Connect Python to SQL Server
server = config.server
database = config.database

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+database+'; ENCRYPT=yes; Trusted_Connection=yes;')
cursor = conn.cursor()

#Create Orders table 
cursor.execute('''
                CREATE TABLE dim.orders(
                    # Order Key INT IDENTITY(1,1) PRIMARY KEY,
                    # Order Id INT,
                    # Order Item Id INT,
                    # Order Customer Id INT,
                    # Order Item Cardprod Id INT,
                    # Market NVARCHAR(50),
                    # Order City NVARCHAR(50),
                    # Order Country NVARCHAR(50),
                    # Order Region NVARCHAR(50),
                    # Order State NVARCHAR(50),
                    # Order Zipcode INT,
                    # Order Status BIT,
                    # Order date (DateOrders) DATE,
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.orders(
                        
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    )''', 
                    row.order_id,
                    row.order_item_id,
                    row.order_customer_id,
                    row.order_item_cardprod_id,
                    row.market,
                    row.order_city,
                    row.order_country,
                    row.order_region,
                    row.order_state,
                    row.order_zipcode,
                    row.order_status,
                    row.order_date_dateorders,
                )
conn.commit()
cursor.close()