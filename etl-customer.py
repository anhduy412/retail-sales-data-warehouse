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
temp_df = df[['customer_id', 'customer_fname', 'customer_lname', 'customer_segment', 'customer_street', 'customer_city', 'customer_state', 'customer_country', 'customer_zipcode']].values.tolist()
customer_df = []
for x in temp_df:
    if x not in customer_df:
        customer_df.append(x)
customer_df = pd.DataFrame(customer_df, columns=['customer_id', 'customer_fname', 'customer_lname', 'customer_segment', 'customer_street', 'customer_city', 'customer_state', 'customer_country', 'customer_zipcode'])
print(customer_df)

#Create Customer Table 
cursor.execute("""CREATE TABLE dim_customer(
    customer_key INT IDENTITY(1,1) PRIMARY KEY,
    customer_id INT,
    customer_fname NVARCHAR(50),
    customer_lname NVARCHAR(50),
    customer_segment NVARCHAR(50),
    customer_street NVARCHAR(50),
    customer_city NVARCHAR(50),
    customer_state NVARCHAR(50),
    customer_country NVARCHAR(50),
    customer_zipcode NVARCHAR(50)
    )"""
)

# Insert DataFrame to Table
for row in customer_df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[dim_customer](customer_id, customer_fname, customer_lname, customer_segment, customer_street, customer_city, customer_state, customer_country, customer_zipcode)  VALUES ({row.customer_id}, '{row.customer_fname}', '{row.customer_lname}', '{row.customer_segment}','{row.customer_street}', '{row.customer_city}', '{row.customer_state}', '{row.customer_country}', '{row.customer_zipcode}');"
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()