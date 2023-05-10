import pyodbc
import config

#Import dataframe
df = config.df

# #Connect Python to SQL Server
server = config.server
database = config.database
username = config.username
password = config.password

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')
cursor = conn.cursor()

#Create benefits table 
cursor.execute("""CREATE TABLE fact_sales_per_time(
    sales_per_time_key INT IDENTITY(1,1) PRIMARY KEY,
    date_key INT FOREIGN KEY REFERENCES dim_date(date_key),
    order_key INT FOREIGN KEY REFERENCES dim_orders(order_key),
    order_item_quantity INT,
    order_date_dateorders DATE,
    )"""
)

#Perform join
# cursor.execute("""SELECT
#     date_key
#     FROM [dbo].[dim_date] dt
#     JOIN [dbo].[benefits] b ON b.date_key = dt.date_key)"""
# )

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[fact_sales_per_time] (order_item_quantity, order_date_dateorders)  VALUES ({row.order_item_quantity}, '{row.order_date_dateorders}');"
    )
conn.commit()
cursor.close()