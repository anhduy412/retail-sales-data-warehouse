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

#Create  fact table
cursor.execute("""
    CREATE TABLE fact_profit(
        profit_key INT FOREIGN KEY REFERENCES dim_profit(profit_key),
        order_key INT FOREIGN KEY REFERENCES dim_order(order_key),
        
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_profit()
    SELECT
        dim_._key,
        type,
    FROM dcscd
    JOIN dim_ ON dcscd. = dim_.
    JOIN dim_ ON dcscd. = dim_.
    JOIN dim_ ON dcscd. = dim_
    JOIN dim_ ON dcscd. = dim_. AND dcscd. = dim_ AND dcscd. = dim_
    """
)