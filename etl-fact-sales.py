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
        profit_key INT FOREIGN KEY REFERENCES dim_profit(profit_key),
        order_item_quantity INT,
        sales FLOAT,
        order_item_total FLOAT
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_sales(order_key, date_key, customer_key, product_key, category_key, store_key, department_key, discount_key, shipment_key, profit_key, order_item_quantity, sales, order_item_total)
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
        dim_profit.profit_key,
        dcscd.order_item_quantity,
        dcscd.sales,
        dcscd.order_item_total
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
    JOIN dim_profit ON dcscd.order_item_product_price = dim_profit.order_item_product_price AND dcscd.order_item_profit_ratio = dim_profit.order_item_profit_ratio AND dcscd.order_item_quantity = dim_profit.order_item_quantity AND dcscd.order_item_total = dim_profit.order_item_total AND dcscd.order_profit_per_order = dim_profit.order_profit_per_order AND dcscd.sales_per_customer = dim_profit.sales_per_customer
    """
)
conn.commit()
print("Insert to SQL Server succeeded.")
cursor.close()