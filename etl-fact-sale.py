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

#Create sales table, a fact table 
cursor.execute("""
    CREATE TABLE fact_sales(
        date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
        order_key INT FOREIGN KEY REFERENCES dim_orders(order_key),
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
        store_key INT FOREIGN KEY REFERENCES dim_store(store_key),
        discount_key INT FOREIGN KEY REFERENCES dim_discount(discount_key),
        market NVARCHAR(255),
        order_region NVARCHAR(255),
        order_item_quantity INT,
        order_item_total FLOAT
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_sales(date_key, order_key, customer_key, product_key, store_key, discount_key, market, order_region, order_item_quantity, order_item_total)
    SELECT
        dim_date.date_key,
        dim_orders.order_key,
        dim_customer.customer_key,
        dim_product.product_key,
        dim_store.store_key,
        dim_discount.discount_key,
        dcscd.market,
        dcscd.order_region,
        order_item_quantity,
        order_item_total
    FROM dcscd
    JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    JOIN dim_store ON dcscd.department_name = dim_store.department_name AND dcscd.latitude = dim_store.latitude AND dcscd.longitude = dim_store.longitude
    JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate
    """
)
conn.commit()
print("Insert to SQL Server succeeded.")
cursor.close()