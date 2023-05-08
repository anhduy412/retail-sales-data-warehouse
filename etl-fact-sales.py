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

#Create benefits table 
cursor.execute("""CREATE TABLE fact_sales(
    sales_key INT IDENTITY(1,1) PRIMARY KEY,
    shipment_key INT FOREIGN KEY REFERENCES [dbo].[dim_shipment](shipment_key),
    category_key INT FOREIGN KEY REFERENCES [dbo].[dim_category](category_key),
    product_key INT FOREIGN KEY REFERENCES [dbo].[dim_product](product_key),
    customer_key INT FOREIGN KEY REFERENCES [dbo].[dim_customer](customer_key),
    order_key INT FOREIGN KEY REFERENCES [dbo].[dim_orders](order_key),
    department_key INT FOREIGN KEY REFERENCES [dbo].[dim_department](department_key),
    store_key INT FOREIGN KEY REFERENCES [dbo].[dim_store](store_key),
    date_key INT FOREIGN KEY REFERENCES [dbo].[dim_date](date_key),
    type NVARCHAR(50),
    order_item_discount FLOAT,
    order_item_discount_rate FLOAT,
    order_item_product_price FLOAT,
    order_item_profit_ratio FLOAT,
    order_item_quantity INT,
    sales FLOAT,
    order_item_total FLOAT,
    order_profit_per_order FLOAT
    )"""
)

# Perform Join with other tables
cursor.execute("""SELECT
    shipment_key, 
    category_key, 
    product_key, 
    customer_key, 
    order_key, 
    department_key, 
    store_key,
    date_key
    FROM [dbo].[dim_shipment] s, [dbo].[dim_category] c, [dbo].[dim_product] p, [dbo].[dim_customer] cust, [dbo].[dim_orders] o, [dbo].[dim_department] d, [dbo].[dim_store] st, [dbo].[dim_date] dt
    JOIN [dbo].[fact_sales] b ON b.shipment_key = s.shipment_key, b.category_key = c.category_key, b.product_key = p.product_key, b.customer_key = cust.customer_key, b.order_key = o.order_key, b.department_key = d.department_key, b.store_key = st.store_key, b.date_key = dt.date_key)"""
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[fact_sales] (type, order_item_discount, order_item_discount_rate, order_item_product_price, order_item_profit_ratio, order_item_quantity, sales, order_item_total, order_profit_per_order) WHERE () NOT IN (SELECT * FROM [dbo].[dim_]) VALUES ('{row.type}', {row.order_item_discount}, {row.order_item_discount_rate}, {row.order_item_product_price}, {row.order_item_profit_ratio}, {row.order_item_quantity}, {row.sales}, {row.order_item_total}, {row.order_profit_per_order});"
    )

conn.commit()
cursor.close()