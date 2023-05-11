import pandas as pd
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

#Create a new dataframe to avoid inserting duplicate data
temp_df = df[['product_card_id', 'product_category_id', 'product_image', 'product_name', 'product_price']].values.tolist()
product_df = []
for x in temp_df:
    if x not in product_df:
        product_df.append(x)
product_df = pd.DataFrame(product_df, columns=['product_card_id', 'product_category_id', 'product_image', 'product_name', 'product_price'])
print(product_df)

#Create product table 
cursor.execute("""CREATE TABLE dim_product(
    product_key INT IDENTITY(1,1) PRIMARY KEY,
    product_card_id INT,
    product_category_id INT,
    product_image NVARCHAR(250),
    product_name NVARCHAR(50),
    product_price FLOAT,
    )"""
)

# Insert DataFrame to Table
for row in product_df.itertuples():
    cursor.execute("""
        INSERT INTO [dbo].[dim_product](
            product_card_id,
            product_category_id,
            product_image,
            product_name,
            product_price
        )
        VALUES (?, ?, ?, ?, ?);
        """, 
        row.product_card_id,
        row.product_category_id,
        row.product_image,
        row.product_name,
        row.product_price,
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()