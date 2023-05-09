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

#Create category table 
cursor.execute("""CREATE TABLE dim_category(category_key INT IDENTITY(1,1) PRIMARY KEY, category_id INT, category_name NVARCHAR(50))""")

# Insert DataFrame to Table
for row in df.itertuples():
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
cursor.close()

# xl df, tránh duplicate