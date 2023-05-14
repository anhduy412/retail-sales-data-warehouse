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

#Create  fact table
cursor.execute("""
    CREATE TABLE fact_(
        order_key INT FOREIGN KEY REFERENCES dim_order(order_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
        discount_key INT FOREIGN KEY REFERENCES dim_promotion(discount_key),
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        order_status NVARCHAR(50),
        type NVARCHAR(50),
        sales FLOAT
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_()
    SELECT
        dim_order.order_key,
        dim_product.product_key,
        dim_discount.discount_key,
        dim_customer_key,
        type,
    FROM dcscd
    JOIN dim_ ON dcscd. = dim_.
    JOIN dim_ ON dcscd. = dim_.
    JOIN dim_ ON dcscd. = dim_
    JOIN dim_ ON dcscd. = dim_. AND dcscd. = dim_ AND dcscd. = dim_
    """
)