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
                CREATE TABLE dim.shipment(
                    Shipment Id INT IDENTITY(1,1) PRIMARY KEY,
                    Days for shipment (scheduled) INT,
                    Days for shipping (real) INT,
                    Delivery status NVARCHAR(50),
                    Late delivery risk BIT,
                    Shipping date (DateOrders) DATE,
                    ShippingMode NVARCHAR(50),
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.shipment (
                        Days for shipment (scheduled),
                        Days for shipping (real),
                        Delivery status,
                        Late delivery risk,
                        Shipping date,
                        ShippingMode
                    ) VALUES (?,?,?,?,?,?,?)
                    )''', 
                    row.days_for_shipment_scheduled, 
                    row.days_for_shipping_real, 
                    row.delivery_status, 
                    row.late_delivery_risk,
                    row.shipping_date, 
                    row.shipping_mode, 
                )
conn.commit()
cursor.close()