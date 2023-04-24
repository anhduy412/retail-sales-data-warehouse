import pandas as pd
import pandas as pd
import pyodbc
import config

#Import dataframe
df = config.df
print(df)

#Connect Python to SQL Server
server = config.server
database = config.database

conn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server}; SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;Trusted_Connection=yes;')
cursor = conn.cursor()

#Create Date table
cursor.execute('''
                CREATE TABLE dim.date(
                    
                )'''
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute('''
                    INSERT INTO RetailSales.dim.orders(
                        
                    ) VALUES (?,)
                    )''', 
                    row.,
                )
conn.commit()
cursor.close()