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

#Create product table 
cursor.execute("""CREATE TABLE product(
    product_key INT IDENTITY(1,1) PRIMARY KEY,
    product_card_id INT,
    product_category_id INT,
    product_description NVARCHAR(255),
    product_image NVARCHAR(255),
    product_name NVARCHAR(255),
    product_price FLOAT,
    product_status BIT
    )"""
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[product] (product_card_id, product_category_id, product_description, product_image, product_name, product_price, product_status) VALUES ({row.product_card_id}, {row.product_category_id}, {row.product_description}, '{row.product_description}', '{row.product_image}', '{row.product_name}', {row.product_price}, {row.product_status});"
    )
conn.commit()
cursor.close()