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
        discount_key INT FOREIGN KEY REFERENCES dim_promotion(discount_key),
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
        dim_date.date_key, #compare order_date with day in date dimension 
        dim_product.product_key, #id
        dim_store.store_key, #compare lat long in df with store dimension
        dim_promotion.discount_key #compare discount with discount dimension
    FROM fact_customer
    JOIN dim_customer ON fact_customer.customer_key = dim_customer.customer_key
    JOIN dim_date ON fact_customer.date_key = dim_date.date_key
    JOIN dim_product ON fact_customer.product_key = dim_product.product_key
    JOIN dim_store ON fact_customer.store_key = dim_store.store_key
    JOIN dim_promotion ON fact_customer.discount_key = dim_promotion.discount_key
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