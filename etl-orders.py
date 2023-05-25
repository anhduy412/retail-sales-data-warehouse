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
temp_df = df[['order_id', 'order_item_id', 'order_customer_id', 'order_item_cardprod_id', 'market', 'order_city', 'order_country', 'order_date_dateorders', 'order_region', 'order_state', 'order_status', 'days_for_shipment_scheduled', 'days_for_shipping_real', 'shipping_date_dateorders', 'shipping_mode']].values.tolist()
orders_df = []
for x in temp_df:
    if x not in orders_df:
        orders_df.append(x)
orders_df = pd.DataFrame(orders_df, columns=['order_id', 'order_item_id', 'order_customer_id', 'order_item_cardprod_id', 'market', 'order_city', 'order_country', 'order_date_dateorders', 'order_region', 'order_state', 'order_status', 'days_for_shipment_scheduled', 'days_for_shipping_real', 'shipping_date_dateorders', 'shipping_mode'])
# print(orders_df)

#Create orders table 
cursor.execute("""CREATE TABLE dim_orders(
    order_key INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT,
    order_item_id INT,
    order_customer_id INT,
    order_item_cardprod_id INT,
    market NVARCHAR(50),
    order_city NVARCHAR(50),
    order_country NVARCHAR(50),
    order_date_dateorders NVARCHAR(50),
    order_region NVARCHAR(50),
    order_state NVARCHAR(50),
    order_status NVARCHAR(50),
    days_for_shipment_scheduled INT,
    days_for_shipping_real INT,
    shipping_date_dateorders NVARCHAR(50),
    shipping_mode NVARCHAR(500),
    )"""
)

# Insert DataFrame to Table
for row in orders_df.itertuples():
    cursor.execute(
        """INSERT INTO [dbo].[dim_orders](
                order_id,
                order_item_id,
                order_customer_id,
                order_item_cardprod_id,
                market,
                order_city,
                order_country,
                order_date_dateorders,
                order_region,
                order_state,
                order_status,
                days_for_shipment_scheduled,
                days_for_shipping_real,
                shipping_date_dateorders,
                shipping_mode
            ) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, 
        row.order_id,
        row.order_item_id,
        row.order_customer_id,
        row.order_item_cardprod_id,
        row.market,
        row.order_city,
        row.order_country,
        row.order_date_dateorders,
        row.order_region,
        row.order_state,
        row.order_status,
        row.days_for_shipment_scheduled,
        row.days_for_shipping_real,
        row.shipping_date_dateorders,
        row.shipping_mode
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()
