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

#Create a new dataframe to avoid inserting duplicate data
temp_df = df[['department_id', 'department_name']].values.tolist()
dept_df = []
for x in temp_df:
    if x not in dept_df:
        dept_df.append(x)
dept_df = pd.DataFrame(dept_df, columns=['department_id', 'department_name'])
# print(dept_df)

#Create Department table 
cursor.execute("""CREATE TABLE dim_department(department_key INT IDENTITY(1,1) PRIMARY KEY, department_id INT, department_name NVARCHAR(50))""")

# Insert DataFrame to Table
for row in dept_df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[dim_department] (department_id, department_name)  VALUES ({row.department_id}, '{row.department_name}');"
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()