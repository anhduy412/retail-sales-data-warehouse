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
temp_df = df[['customer_key', 'date_key', 'product_key', 'store_key', 'discount_key', 'type', 'order_item_total', 'order_item_quantity']].values.tolist()
fact_customer_df = []
for x in temp_df:
    if x not in fact_customer_df:
        fact_customer_df.append(x)
fact_customer_df = pd.DataFrame(fact_customer_df, columns=['customer_key', 'date_key', 'product_key', 'store_key', 'discount_key', 'type', 'order_item_total', 'order_item_quantity'])
print(fact_customer_df)

#Create customer fact table
cursor.execute("""
    CREATE TABLE fact_customer(
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
        store_key INT FOREIGN KEY REFERENCES dim_store(store_key),
        discount_key INT FOREIGN KEY REFERENCES dim_disount(discount_key),
        type NVARCHAR(50),
        order_item_quantity INT
        order_item_total FLOAT,
    )"""
)

# Perform Join with other tables
cursor.execute("""
    INSERT INTO fact_customer(customer_key, product_key)
    SELECT
        customer_key,
        date_key,
        product_key,
        store_key,
        discount_key,
    FROM dcscd
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_date ON dcscd.order_date_dateorders = dim_customer.day
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    JOIN dim_store ON dcscd.store_latitude = dim_store.latitude AND dcscd.store_longitude = dim_store.longitude
    JOIN dim_discount ON dcscd.order_item_discount = dim_customer.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate AND dcscd.sales = dim_discount.sales
    """
)

# Insert DataFrame to Table
for row in fact_customer_df.itertuples():
    cursor.execute(""" 
        INSERT INTO [dbo].[fact_customer] (
            type,
            order_item_total,
            order_item_quantity
        ) VALUES (?, ?, ?)
        """,
        row.type,
        row.order_item_total,
        row.order_item_quantity
    )
    conn.commit()
print("Insert to SQL Server succeeded.")
cursor.close()