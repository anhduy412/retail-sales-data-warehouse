import pyodbc
import config

#Import dataframe
df = config.df
print(df.dtypes)

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
    order_item_quantity INT,
    order_date_dateorders DATE,
    )"""
)

# Perform Join with other tables
cursor.execute("""
    """
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[fact_sales_per_time] (order_item_quantity, ) VALUES ('{row.order_item_quantity}, '{row.order_date_dateorders}', {row.numeric},);"
    )

conn.commit()
cursor.close()