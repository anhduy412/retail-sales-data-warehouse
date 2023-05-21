import pandas as pd
import pyodbc

#Import csv file into dataframe and perfrom data cleaning
data = pd.read_csv('data/DataCoSupplyChainDataset.csv', float_precision=None, encoding='utf-8-sig')
df = pd.DataFrame(data)
df.columns = [x.lower().replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns]
df['shipping_date_dateorders'] = pd.to_datetime(df['shipping_date_dateorders'])
df['shipping_date_dateorders'] = df['shipping_date_dateorders'].dt.strftime('%Y-%m-%d')
df['order_date_dateorders'] = pd.to_datetime(df['order_date_dateorders'])
df['order_date_dateorders'] = df['order_date_dateorders'].dt.strftime('%Y-%m-%d')
# df.to_csv('DataCoSupplyChainDataset.csv', encoding='utf-8-sig', index=False)
# print(df.dtypes)

#create discount dataframe from the original dataframe
discount_df1 = df[['order_item_discount', 'order_item_discount_rate', 'sales']].copy()
#print(discount_df1)
# discount_df1.to_csv('dcscd_discount.csv', index=False)

#create store dataframe from the original dataframe
store_df1 = df[['latitude', 'longitude']].copy()
# print(store_df1)
# store_df1.to_csv('dcscd_store.csv', index=False)

#create profit dataframe from the original dataframe
profit_df1 = df[['order_item_product_price', 'order_item_profit_ratio', 'order_item_quantity', 'order_item_total', 'order_profit_per_order', 'sales_per_customer']].copy()
#print(profit_df1)
# profit_df1.to_csv('dcscd_profit.csv', index=False)

#Check the pyodbc drivers
# print(pyodbc.drivers())

# Some required variables for SQL connection
database = 'retail_sales' #database name
server = 'ROG' #server name
username = 'ad' #username
password = 'b4cB4jDA9BPI6Bwg' #password
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')

# Some code to test connection
cursor = conn.cursor()
cursor.execute("SELECT @@version;")
while row := cursor.fetchone():
    print(row[0])