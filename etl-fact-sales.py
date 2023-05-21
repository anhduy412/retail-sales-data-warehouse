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
        order_key INT FOREIGN KEY REFERENCES dim_orders(order_key),
        date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
        customer_key INT FOREIGN KEY REFERENCES dim_customer(customer_key),
        product_key INT FOREIGN KEY REFERENCES dim_product(product_key),
        category_key INT FOREIGN KEY REFERENCES dim_category(category_key),
        store_key INT FOREIGN KEY REFERENCES dim_store(store_key),
        department_key INT FOREIGN KEY REFERENCES dim_department(department_key),
        discount_key INT FOREIGN KEY REFERENCES dim_discount(discount_key),
        shipment_key INT FOREIGN KEY REFERENCES dim_shipment(shipment_key),
        order_item_quantity INT,
        order_item_total FLOAT,
        sales FLOAT,
        sales_per_customer FLOAT,
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_sales(order_key, date_key, customer_key, product_key, category_key, store_key, department_key, discount_key, shipment_key, order_item_quantity, order_item_total, sales, sales_per_customer)
    SELECT
        dim_orders.order_key,
        dim_date.date_key,
        dim_customer.customer_key,
        dim_product.product_key,
        dim_category.category_key,
        dim_store.store_key,
        dim_department.department_key,
        dim_discount.discount_key,
        dim_shipment.shipment_key,
        order_item_quantity, 
        order_item_total,
        sales,
        sales_per_customer
    FROM dcscd
    JOIN dim_orders ON dcscd.order_id = dim_orders.order_id
    JOIN dim_date ON dcscd.order_date_dateorders = dim_date.day
    JOIN dim_customer ON dcscd.customer_id = dim_customer.customer_id
    JOIN dim_product ON dcscd.product_card_id = dim_product.product_card_id
    JOIN dim_category ON dcscd.category_id = dim_category.category_id
    JOIN dim_store ON dcscd.latitude = dim_store.latitude AND dcscd.longitude = dim_store.longitude
    JOIN dim_department ON dcscd.department_id = dim_department.department_id
    JOIN dim_discount ON dcscd.order_item_discount = dim_discount.order_item_discount AND dcscd.order_item_discount_rate = dim_discount.order_item_discount_rate
    JOIN dim_shipment ON dcscd.days_for_shipment_scheduled = dim_shipment.days_for_shipment_scheduled AND dcscd.days_for_shipping_real = dim_shipment.days_for_shipping_real AND dcscd.shipping_date_dateorders = dim_shipment.shipping_date_dateorders AND dcscd.shipping_mode = dim_shipment.shipping_mode
    """
)
conn.commit()
print("Insert to SQL Server succeeded.")
cursor.close()