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

#Create store table 
cursor.execute("""CREATE TABLE store(store_key INT IDENTITY(1,1) PRIMARY KEY, latitude FLOAT, longitude FLOAT)""")

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[store] (latitude, longitude) VALUES ({row.latitude}, '{row.longitude}');"
    )
conn.commit()
cursor.close()