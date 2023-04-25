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

#Create Department table 
cursor.execute("""CREATE TABLE department(
    department_key INT IDENTITY(1,1) PRIMARY KEY, 
    department_id INT,
    department_name NVARCHAR(50)
    )"""
)

# Insert DataFrame to Table
for row in df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[department] (department_id, department_name) VALUES ({row.department_id}, '{row.department_name}');"
    )
conn.commit()
cursor.close()