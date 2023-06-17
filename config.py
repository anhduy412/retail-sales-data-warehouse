import pandas as pd
import pyodbc

#Import csv file into dataframe and perfrom data cleaning
data = pd.read_csv('data/DataCoSupplyChainDataset.csv')
df = pd.DataFrame(data)
df.columns = [x.lower().replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns]
df['shipping_date_dateorders'] = pd.to_datetime(df['shipping_date_dateorders'])
df['shipping_date_dateorders'] = df['shipping_date_dateorders'].dt.strftime('%d-%m-%Y')
df['order_date_dateorders'] = pd.to_datetime(df['order_date_dateorders'])
df['order_date_dateorders'] = df['order_date_dateorders'].dt.strftime('%d-%m-%Y')
# df.to_csv('data/dcscd.csv', encoding='utf-8-sig', index=False)
# print(df.dtypes)

# df['shipping_date_dateorders'] = pd.to_datetime(df['shipping_date_dateorders'], format='%d/%m/%Y')
# df['order_date_dateorders'] = pd.to_datetime(df['order_date_dateorders'], format='%d/%m/%Y')

#Check the pyodbc drivers
# print(pyodbc.drivers())

# Some required variables for SQL connection
database = 'retail_sales' #database name
server = 'ROG' #server name
username = 'sa' #your username
password = 'b4cB4jDA9BPI6Bwg' #your password
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')

# Some code to test connection
cursor = conn.cursor()
cursor.execute("SELECT @@version;")
while row := cursor.fetchone():
    print(row[0])