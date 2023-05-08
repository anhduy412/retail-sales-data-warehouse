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

#Create shipment table 
cursor.execute("""CREATE TABLE dim_shipment(
    shipment_key INT IDENTITY(1,1) PRIMARY KEY,
    days_for_shipment_scheduled INT,
    days_for_shipping_real INT,
    shipping_date_dateorders NVARCHAR(50),
    shipping_mode NVARCHAR(500),
    )"""
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        """INSERT INTO [dbo].[dim_shipment](
                days_for_shipment_scheduled,
                days_for_shipping_real,
                shipping_date_dateorders,
                shipping_mode
            ) VALUES (?, ?, ?, ?);
        """, 
        row.days_for_shipment_scheduled,
        row.days_for_shipping_real,
        row.shipping_date_dateorders,
        row.shipping_mode
    )
conn.commit()
cursor.close()
