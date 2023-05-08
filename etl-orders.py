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

#Create orders table 
cursor.execute("""CREATE TABLE dim_orders(
    order_key INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT,
    order_item_id INT,
    order_customer_id INT,
    order_item_cardprod_id INT,
    market NVARCHAR(50),
    order_city NVARCHAR(50),
    order_country NVARCHAR(50),
    order_date_dateorders NVARCHAR(50),
    order_region NVARCHAR(50),
    order_state NVARCHAR(50),
    order_status NVARCHAR(50),
    )"""
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        """INSERT INTO [dbo].[dim_orders](
                order_id,
                order_item_id,
                order_customer_id,
                order_item_cardprod_id,
                market,
                order_city,
                order_country,
                order_date_dateorders,
                order_region,
                order_state,
                order_status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, 
        row.order_id,
        row.order_item_id,
        row.order_customer_id,
        row.order_item_cardprod_id,
        row.market,
        row.order_city,
        row.order_country,
        row.order_date_dateorders,
        row.order_region,
        row.order_state,
        row.order_status,
    )
conn.commit()
cursor.close()
