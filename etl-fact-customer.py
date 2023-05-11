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

#Create customer fact table
cursor.execute("""
    CREATE TABLE fact_customer(
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
        type NVARCHAR(50),
        order_item_quantity INT,
        order_item_total FLOAT
    )
    INSERT INTO fact_customer(customer_key, date_key, product_key)
    SELECT
        dim_customer.customer_key,
        dim_date.date_key,
        dim_product.product_key
    FROM dcscd
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    """
)
conn.commit()

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute("""
        INSERT INTO [dbo].[fact_customer] (
            type,
            order_item_quantity,
            order_item_total
        ) VALUES (?, ?, ?)
        """,
        row.type,
        row.order_item_quantity,
        row.order_item_total
    )
conn.commit()
print("Insert to SQL Server succeeded.")
cursor.close()
#Perform Join with other tables