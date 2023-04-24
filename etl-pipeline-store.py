import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df
print(df)

#Connect Python to SQL Server
server = config.server
database = config.database

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+';DATABASE='+database+'; ENCRYPT=yes; Trusted_Connection=yes;')
cursor = conn.cursor()

#Create Department table 
cursor.execute('''
                CREATE TABLE dim.department(
                    Shipment Id INT IDENTITY(1,1) PRIMARY KEY,
                    Department Id INT,
                    Department Name NVARCHAR(50),
                    Latitude FLOAT,
                    Longitude FLOAT,
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.department(
                        Latitude,
                        Longitude,
                    ) VALUES (?,?,?,?)
                    )''',
                    row.latitude, 
                    row.longtitude,
    )
conn.commit()
cursor.close()