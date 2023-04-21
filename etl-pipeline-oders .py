import pandas as pd
import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df
print(df)

#Connect Python to SQL Server
drivers = config.drivers
server = config.server
database = config.database
username = config.username
password = config.password

conn = pyodbc.connect('DRIVER = ' + drivers + '; SERVER = tcp:' + server + '; PORT=1436; DATABASE=' + database + '; UID = ' + username +'; PWD = '+ password + '; TrustServerCertificate = Yes;')
cursor = conn.cursor()

#Create Orders table 
cursor.execute('''
                CREATE TABLE dim.orders(
                    Order Id INT PRIMARY KEY,
                    Order Item Id INT FOREIGN KEY REFERENCES dim.(),
                    Order Customer Id INT FOREIGN KEY REFERENCES dim.(),
                    Order Item Cardprod Id INT FOREIGN KEY REFERENCES dim.(),
                    Order City NVARCHAR(50),
                    Order Country NVARCHAR(50),
                    Order Region NVARCHAR(50),
                    Order State NVARCHAR(50),
                    Order Zipcode INT,
                    Order Market NVARCHAR(50),
                    Order Item Total FLOAT,
                    Order Benefit Per Order FLOAT,
                    Order Sales Per Customer FLOAT,
                    Order Type NVARCHAR(50),
                    Order Date Dateorders DATE,
                    Order Item Discount FLOAT,
                    Order Item Discount Rate FLOAT,
                    Order Item Product Price FLOAT,
                    Order Item Profit Ratio FLOAT,
                    Order Item Quantity INT,
                    Order Sales FLOAT,
                    Order Profit Per Order FLOAT,
                    Order Status NVARCHAR(50),
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.orders(
                        
                    ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)qweqe
                    )''', 
                    row.order_id,
                    row.order_item_id,
                    row.order_customer_id,
                    row.order_item_cardprod_id,
                    row.order_city,
                    row.order_country,
                    row.order_region,
                    row.order_state,
                    row.order_zipcode,
                    row.market,
                    row.order_item_total,
                    row.benefit_per_order,
                    row.sales_per_customer,
                    row.type,
                    row.order_date_dateorders,
                    row.order_item_discount,
                    row.order_item_discount_rate,
                    row.order_item_product_price,
                    row.order_item_profit_ratio,
                    row.order_item_quantity,
                    row.sales,
                    row.order_profit_per_order,
                    row.order_status,
                )
conn.commit()
cursor.close()