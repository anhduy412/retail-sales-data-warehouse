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

# Create customer fact table
cursor.execute("""
    CREATE TABLE fact_customer(
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
        store_key INT FOREIGN KEY REFERENCES dim_store(store_key),
        order_key INT FOREIGN KEY REFERENCES dim_orders(order_key),
        discount_key INT FOREIGN KEY REFERENCES dim_discount(discount_key),
        sales FLOAT,
        order_item_quantity INT,
        order_item_total FLOAT
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_customer(customer_key, date_key, store_key, order_key, discount_key, sales, order_item_quantity, order_item_total)
    SELECT
        dim_customer.customer_key,
        dim_date.date_key,
        dim_store.store_key,
        dim_orders.order_key,
        dim_discount.discount_key,
        sales,
        order_item_quantity,
        order_item_total
    FROM dcscd
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    JOIN dim_store ON dcscd.latitude = dim_store.latitude AND dcscd.longitude = dim_store.longitude
    JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
    JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate
    """
)
conn.commit()
print("Insert to SQL Server succeeded.")
cursor.close()