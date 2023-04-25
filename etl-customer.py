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

#Create Customer Table 
cursor.execute("""CREATE TABLE customer(customer_key INT IDENTITY(1,1) PRIMARY KEY, customer_id INT, customer_fname VARCHAR(50), customer_lname VARCHAR(50), customer_segment VARCHAR(50), customer_street VARCHAR(50), customer_city NVARCHAR(50), customer_state NVARCHAR(50), customer_country NVARCHAR(50), customer_zipcode NVARCHAR(50), customer_email NVARCHAR(50), customer_password NVARCHAR(50))""")

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[customer] (customer_id, customer_fname, customer_lname, customer_segment, customer_street, customer_city, customer_state, customer_country, customer_zipcode, customer_email, customer_password) VALUES ({row.customer_id}, '{row.customer_fname}', '{row.customer_lname}', '{row.customer_segment}', '{row.customer_street}', '{row.customer_city}', '{row.customer_state}', '{row.customer_country}', '{row.customer_zipcode}', '{row.customer_email}', '{row.customer_password}');"
    )
conn.commit()
cursor.close()