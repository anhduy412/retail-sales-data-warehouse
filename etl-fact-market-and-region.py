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

#Create shipment fact table
cursor.execute("""
    CREATE TABLE fact_market_and_region(
        shipment_key INT FOREIGN KEY REFERENCES dim_shipment(shipment_key),
        date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        order_key INT FOREIGN KEY REFERENCES dim_orders(order_key),
        market NVARCHAR(255),
        order_region NVARCHAR(255),
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_market_and_region(shipment_key, date_key, customer_key, order_key, market, order_region)
    SELECT
        dim_shipment.shipment_key,
        dim_date.date_key,
        dim_customer.customer_key,
        dim_orders.order_key,
        market,
        order_region
    FROM dcscd
    JOIN dim_shipment ON dcscd.days_for_shipment_scheduled = dim_shipment.days_for_shipment_scheduled AND dcscd.days_for_shipping_real = dim_shipment.days_for_shipping_real AND dcscd.shipping_date_dateorders = dim_shipment.shipping_date_dateorders AND dcscd.shipping_mode = dim_shipment.shipping_mode
    JOIN dim_date ON dcscd.shipping_date_dateorders = dim_date.day
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    """
)
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()