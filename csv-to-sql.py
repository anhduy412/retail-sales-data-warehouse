import pandas as pd
import pyodbc as odb

df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding='latin-1')
df = pd.DataFrame(df)
print(df)

print(odb.drivers())

conn = odb.connect('Driver={SQL Server};' 'Server = DESKTOP-7QJ9Q0G\SQLEXPRESS;' 'Database = SupplyChain;' 'Trusted_Connection=yes;')
cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.Orders')

for _ in df.itertuples():
    cursor.execute('''
        INSERT INTO dbo.Orders (Order_ID, Order_Date, Ship_Date, Ship_Mode, Customer_ID, Customer_Name, Segment, Country, City, State, Postal_Code, Region, Product_ID, Category, Sub_Category, Product_Name, Sales, Quantity, Discount, Profit''')
conn.commit()