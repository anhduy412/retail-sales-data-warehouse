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
cursor.execute("""CREATE TABLE fact_sales(
    shipment_key INT FOREIGN KEY REFERENCES [dbo].[dim_shipment](shipment_key),
    category_key INT FOREIGN KEY REFERENCES [dbo].[dim_category](category_key),
    product_key INT FOREIGN KEY REFERENCES [dbo].[dim_product](product_key),
    customer_key INT FOREIGN KEY REFERENCES [dbo].[dim_customer](customer_key),
    discount_key INT FOREIGN KEY REFERENCES [dbo].[dim_discount](discount_key),
    order_key INT FOREIGN KEY REFERENCES [dbo].[dim_orders](order_key),
    department_key INT FOREIGN KEY REFERENCES [dbo].[dim_department](department_key),
    store_key INT FOREIGN KEY REFERENCES [dbo].[dim_store](store_key),
    date_key INT FOREIGN KEY REFERENCES [dbo].[dim_date](date_key),
    profit_key INT FOREIGN KEY REFERENCES [dbo].[dim_profit](profit_key),
    )"""
)

# Perform Join with other tables

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[fact_sales] (type, order_item_discount, order_item_discount_rate, order_item_product_price, order_item_profit_ratio, order_item_quantity, sales, order_item_total, order_profit_per_order)  VALUES ('{row.type}', {row.order_item_discount}, {row.order_item_discount_rate}, {row.order_item_product_price}, {row.order_item_profit_ratio}, {row.order_item_quantity}, {row.sales}, {row.order_item_total}, {row.order_profit_per_order});"
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()