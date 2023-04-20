import pandas as pd
import pyodbc as po
import config

#Import the CSV File into a DataFrame
data = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding = 'latin-1')
df = pd.DataFrame(data)
print(df.info)

#Connect Python to SQL Server
driver = config.driver
server = config.server
database = config.database
username = config.username
password = config.password

conn = po.connect(
    f'DRIVER={driver}; SERVER=tcp:{server}; PORT=; DATABASE={database};UID={username}; PWD={password}; TrustServerCertificate=Yes;'
)

cursor = conn.cursor()

# Create Customer Table
cursor.execute('''
		CREATE TABLE stg.CATEGORY (
			customer_city NVARCHAR(50),
			customer_country NVARCHAR(50),
			customer_email NVARCHAR(50),
			customer_fname NVARCHAR(50),
			customer_id NVARCHAR(50),
			customer_lname NVARCHAR(50),
			customer_password NVARCHAR(50),
			customer_segment NVARCHAR(50),
			customer_state NVARCHAR(50),
			customer_street NVARCHAR(50),
			customer_zipcode NVARCHAR(50),
			)
    ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CATEGORY (customer_city, customer_country, customer_email, customer_fname, customer_id, ,customer_lname,customer_password,customer_segment,customer_state, customer_street, customer_zipcode)
                VALUES (?,?)
                ''',
                row.Customer City,
                row.Customer Country,
                row.Customer Email,
                row.Customer Fname,
                row.Customer Id,
                row.Customer Lname,
                row.Customer Password,
                row.Customer Segment,
                row.Customer State,
                row.Customer Street,
                row.customer Zipcode,
                )
conn.commit()
conn.close()

# Create Table
cursor.execute('''
		CREATE TABLE stg.CATEGORY (
			product_category_name NVARCHAR(50),
			product_category_name_english NVARCHAR(50)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CATEGORY (product_category_name, product_category_name_english)
                VALUES (?,?)
                ''',
                row.product_category_name,
                row.product_category_name_english
                )
conn.commit()
conn.close()

# Create Table
cursor.execute('''
		CREATE TABLE stg.CATEGORY (
			product_category_name NVARCHAR(50),
			product_category_name_english NVARCHAR(50)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CATEGORY (product_category_name, product_category_name_english)
                VALUES (?,?)
                ''',
                row.product_category_name,
                row.product_category_name_english
                )
conn.commit()
conn.close()

# Create Table
cursor.execute('''
		CREATE TABLE stg.CATEGORY (
			product_category_name NVARCHAR(50),
			product_category_name_english NVARCHAR(50)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CATEGORY (product_category_name, product_category_name_english)
                VALUES (?,?)
                ''',
                row.product_category_name,
                row.product_category_name_english
                )
conn.commit()
conn.close()

# Create Table
cursor.execute('''
		CREATE TABLE stg.CATEGORY (
			product_category_name NVARCHAR(50),
			product_category_name_english NVARCHAR(50)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CATEGORY (product_category_name, product_category_name_english)
                VALUES (?,?)
                ''',
                row.product_category_name,
                row.product_category_name_english
                )
conn.commit()
conn.close()

# Create Table
cursor.execute('''
		CREATE TABLE stg.CATEGORY (
			product_category_name NVARCHAR(50),
			product_category_name_english NVARCHAR(50)
			)
               ''')

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dw_retail_sales.stg.CATEGORY (product_category_name, product_category_name_english)
                VALUES (?,?)
                ''',
                row.product_category_name,
                row.product_category_name_english
                )
conn.commit()
conn.close()