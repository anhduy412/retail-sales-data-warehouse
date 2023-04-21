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

#Create Shipment Table 
cursor.execute('''
                CREATE TABLE dim.customer(
                    Id PRIMARY KEY,
                    Days for shipment (scheduled) INT,
                    Days for shipping (real) INT,
                    Delivery status NVARCHAR(50),
                    Late delivery risk BIT,
                    Shipping date (DateOrders) DATE,
                    ShippingMode NVARCHAR(50),
                    '''
                )

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.customer(
                        Days for shipment (scheduled),
                        Days for shipping (real),
                        Delivery status,
                        Late delivery risk,
                        Shipping date,
                        ShippingMode
                    ) VALUES (?,?,?,?,?,?,?)
                    )''', 
                    row.customer_id,
                    row.customer_city,
                    row.customer_country,
                    row.customer_email,
                    row.customer_fname,
                    row.customer_lname,
                    row.customer_password,
                    row.customer_segment,
                    row.customer_state,
                    row.customer_street,
                    row.customer_zipcode,
                )
conn.commit()
cursor.close()