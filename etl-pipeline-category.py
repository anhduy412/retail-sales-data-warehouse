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

#Create Category Table 
cursor.execute('''
                CREATE TABLE dim.category(
                    Category Id INT,
                    Category Name NVARCHAR(50),
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.category(
                        Category Id,
                        Category Name,
                    ) VALUES (?,?)
                    )''', 
                    row.category_id,
                    row.category_name
    )
conn.commit()
cursor.close()