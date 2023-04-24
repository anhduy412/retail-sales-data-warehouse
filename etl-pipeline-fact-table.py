import pandas as pd
import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df
print(df)

#Connect Python to SQL Server
server = config.server
database = config.database

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;Trusted_Connection=yes;')
cursor = conn.cursor()

#Create Benefit per Order table 
cursor.execute('''
                CREATE TABLE fact.benefit(
                    Shipment Key INT IDENTITY(1,1) FOREIGN KEY REFERENCES dim.shipment(Shipment Key),
                    Category Key INT IDENTITY(1,1) FOREIGN KEY REFERENCES dim.category(Category Key),
                    Product Key INT IDENTITY(1,1) FOREIGN KEY REFERENCES dim.product(Product Key),
                    Customer Key INT IDENTITY(1,1) FOREIGN KEY REFERENCES dim.customer(Customer Key),
                    Order Key INT IDENTITY(1,1) FOREIGN KEY REFERENCES dim.orders(Order Key),
                    Order Id INT FOREIGN KEY REFERENCES dim.orders(Order Id),
                    Department Key INT IDENTITY(1,1) FOREIGN KEY REFERENCES dim.department(Department Key),
                    Store Key INT IDENTITY(1,1) FOREIGN KEY REFERENCES dim.store(Store Key),
                    Type NVARCHAR(50),
                    Order Item Discount FLOAT,
                    Order Item Discount Rate FLOAT,
                    Order Item Product Price FLOAT,
                    Order Item Profit Ratio FLOAT,
                    Order Item Quantity INT,
                    Sales FLOAT,
                    Order Item Total FLOAT,
                    Order Profit Per Order FLOAT,
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.orders(
                        
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    )''', 
                    row.type,
                    row.order_item_discount,
                    row.order_item_discount_rate,
                    row.order_item_product_price,
                    row.order_item_profit_ratio,
                    row.order_item_quantity,
                    row.sales,
                    row.order_item_total,
                    row.order_profit_per_order,
                )
conn.commit()
cursor.close()