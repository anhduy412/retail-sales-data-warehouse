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
        store_key INT FOREIGN KEY REFERENCES dim_store(store_key),
        discount_key INT FOREIGN KEY REFERENCES dim_disount(discount_key),
        type NVARCHAR(50),
        order_item_total FLOAT,
        order_item_discount FLOAT,
        order_item_discount_rate FLOAT,
        order_item_product_price FLOAT,
        order_item_profit_ratio FLOAT,
        order_item_quantity INT
    )"""
)

# Perform Join with other tables
cursor.execute("""
    SELECT
        dim_customer.customer_key, #id
        dim_product.product_key, #id
    FROM fact_customer
    JOIN dim_customer ON fact_customer.customer_id = dim_customer.customer_id
    JOIN dim_product ON fact_customer.product_key = dim_product.product_id
    """
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute("""
        INSERT INTO [dbo].[fact_customer] (
            type,
            order_item_total,
            order_item_discount,
            order_item_discount_rate,
            order_item_product_price,
            order_item_profit_ratio,
            order_item_quantity
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        row.type,
        row.order_item_total,
        row.order_item_discount,
        row.order_item_discount_rate,
        row.order_item_product_price,
        row.order_item_profit_ratio,
        row.order_item_quantity
    )
    conn.commit()
print("Insert to SQL Server succeeded.")
cursor.close()