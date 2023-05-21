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

#Create fact transaction table
cursor.execute("""
    CREATE TABLE fact_transaction(
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        order_key INT FOREIGN KEY REFERENCES dim_orders(order_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
        discount_key INT FOREIGN KEY REFERENCES dim_discount(discount_key),
        type NVARCHAR(50),
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_transaction(customer_key, order_key, product_key, discount_key, type)
    SELECT
        dim_customer.customer_key,
        dim_orders.order_key,
        dim_product.product_key,
        dim_discount.discount_key,
        type
    FROM dcscd
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate
    """
)
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()