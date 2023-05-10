import pandas as pd
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

#Avoid duplicate
temp_df = df[['category_id', 'category_name']].values.tolist()
category_df = []
for x in temp_df:
    if x not in category_df:
        category_df.append(x)
category_df = pd.DataFrame(category_df, columns=['category_id', 'category_name'])
print(category_df)

#Create category table 
cursor.execute("""CREATE TABLE dim_category(category_key INT IDENTITY(1,1) PRIMARY KEY, category_id INT, category_name NVARCHAR(50))""")

# Insert DataFrame to Table
for row in category_df.itertuples():
    cursor.execute(
        """INSERT INTO [dbo].[dim_category](
            category_id, 
            category_name
            )
            VALUES (?, ?);
        """, 
        row.category_id, 
        row.category_name
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()