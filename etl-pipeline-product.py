import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df
print(df)

#Connect Python to SQL Server
server = config.server
database = config.database
username = config.username
password = config.password

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password+';Trusted_Connection=yes;')
cursor = conn.cursor()

#Create Product table
cursor.execute('''
                CREATE TABLE dim.product(
                    Product Card Id INT PRIMARY KEY,
                    Product Category Id INT FOREIGN KEY REFERENCES dim.(),
                    Product Description NVARCHAR(100),
                    Product Image NVARCHAR(100),
                    Product Name NVARCHAR(50),
                    Product Price FLOAT,
                    Product Status BIT,
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.(
                        Product Card Id,
                        Product Card Id,
                        Product Category Id,
                        Product Description,
                        Product Image,
                        Product Name,
                        Product Price,
                        Product Status,
                    ) VALUES (?,?,?,?,?,?,?)
                    )''', 
                    row.product_card_id,
                    row.product_category_id,
                    row.product_description,
                    row.product_image,
                    row.product_name,
                    row.product_price,
                    row.product_status,
    )
conn.commit()
cursor.close()