import pandas as pd
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

#Create Orders table 
cursor.execute('''
                CREATE TABLE dim.orders(
                    Id INT PRIMARY KEY,
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.orders(
                        
                    ) VALUES (?,)qweqe
                    )''', 
                    row.Id,
                )
conn.commit()
cursor.close()