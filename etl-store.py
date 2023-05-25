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
temp_df = df[['department_name', 'latitude', 'longitude']].values.tolist()
store_df = []
for x in temp_df:
    if x not in store_df:
        store_df.append(x)
store_df = pd.DataFrame(store_df, columns=['department_name', 'latitude', 'longitude'])
# print(store_df)

# Create store table
cursor.execute("""CREATE TABLE dim_store(store_key INT IDENTITY(1,1) PRIMARY KEY, department_name NVARCHAR(250), latitude FLOAT, longitude FLOAT)""")

# Insert DataFrame to Table
for row in store_df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[dim_store] (department_name, latitude, longitude) VALUES ('{row.department_name}',{row.latitude}, {row.longitude});"
    )
conn.commit()
print('Data inserted to SQL Server successfully.')
cursor.close()