import os
import pyodbc
import pandas as pd

#import csv file into dataframe and clean table and coulumn names (lowercase letters. remove spaces and special characters)
data = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding = 'latin-1')
df = pd.DataFrame(data)
df.columns = [x.lower().replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns]
print(df.info)

#check the pyodbc drivers
# print(pyodbc.drivers())

#some required variables for SQL connection
drivers = '{ODBC Driver 17 for SQL Server}'
database = 'RetailSales'
server = ''
username = ''
password = ''