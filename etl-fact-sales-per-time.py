import pyodbc
import config

#Import dataframe
df = config.df
print(df.dtypes)

# #Connect Python to SQL Server
server = config.server
database = config.database
username = config.username
password = config.password

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')
cursor = conn.cursor()

#Create benefits table 
cursor.execute("""CREATE TABLE fact_sales_per_time(
    sales_per_time_key INT IDENTITY(1,1) PRIMARY KEY,
    order_item_quantity INT,
    order_date_dateorders DATE,
    )"""
)

#Perform join
cursor.execute("""SELECT
    shipment_key, 
    category_key, 
    product_key, 
    customer_key, 
    order_key, 
    department_key, 
    store_key,
    date_key
    FROM [dbo].[shipment] s, [dbo].[category] c, [dbo].[product] p, [dbo].[customer] cust, [dbo].[orders] o, [dbo].[department] d, [dbo].[store] st, [dbo].[date] dt
    LEFT JOIN [dbo].[benefits] b ON b.shipment_key = s.shipment_key, b.category_key = c.category_key, b.product_key = p.product_key, b.customer_key = cust.customer_key, b.order_key = o.order_key, b.department_key = d.department_key, b.store_key = st.store_key, b.date_key = dt.date_key)"""
)


# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[benefits] (type, order_item_discount, order_item_discount_rate, order_item_product_price, order_item_profit_ratio, order_item_quantity, sales, order_item_total, order_profit_per_order) VALUES ('{row.type}', {row.order_item_discount}, {row.order_item_discount_rate}, {row.order_item_product_price}, {row.order_item_profit_ratio}, {row.order_item_quantity}, {row.sales}, {row.order_item_total}, {row.order_profit_per_order});"
    )

conn.commit()
cursor.close()