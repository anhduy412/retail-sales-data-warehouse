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

#Create Shipment Table 
cursor.execute('''
                CREATE TABLE dim.customer(
                    Customer Id INT PRIMARY KEY,
                    Customer City NVARCHAR(50),
                    Customer Country NVARCHAR(50),
                    Customer Fname NVARCHAR(50),
                    Customer Lname NVARCHAR(50),
                    Customer Segment NVARCHAR(50),
                    Customer State NVARCHAR(50),
                    Customer Street NVARCHAR(50),
                    Customer Zipcode INT,
                    Customer Email NVARCHAR(50),
                    Customer Password NVARCHAR(50),
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.customer(
                        Customer Id,
                        Customer City,
                        Customer Country,
                        Customer Fname,
                        Customer Lname,
                        Customer Segment,
                        Customer State,
                        Customer Street,
                        Customer Zipcode,
                        Customer Email,
                        Customer Password,
                    ) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    )''', 
                    row.customer_id,
                    row.customer_city,
                    row.customer_country,
                    row.customer_fname,
                    row.customer_lname,
                    row.customer_segment,
                    row.customer_state,
                    row.customer_street,
                    row.customer_zipcode,
                    row.customer_email,
                    row.customer_password,
    )
conn.commit()
cursor.close()