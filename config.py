import pandas as pd
import pyodbc

#import csv file into dataframe and clean table and coulumn names (lowercase letters. remove spaces and special characters)
data = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding = 'latin-1')
df = pd.DataFrame(data)
df.columns = [x.lower().replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns]
print(df.info)

# check the pyodbc drivers
# print(pyodbc.drivers())

#some required variables for SQL connection
database = 'RetailSales' #database name
server = 'ROG' #server name
username = 'sa' #username
password = 'cNU2v7XDaECYHT' #password
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')

# Some code to test connection
cursor = conn.cursor()
cursor.execute("SELECT @@version;")
while row := cursor.fetchone():
    print(row[0])