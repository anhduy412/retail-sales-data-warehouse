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