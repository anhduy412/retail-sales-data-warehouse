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

#Create Department table 
cursor.execute('''
                CREATE TABLE dim.department(
                    Department Id INT PRIMARY KEY,
                    Department Name NVARCHAR(50),
                    Latitude FLOAT,
                    Longitude FLOAT,
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.department(
                        Department Id,
                        Department Name,
                        Latitude,
                        Longitude,
                    ) VALUES (?,?,?,?)
                    )''', 
                    row.department_id, 
                    row.department_name,
                    row.latitude, 
                    row.longtitude,
    )
conn.commit()
cursor.close()