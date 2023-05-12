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
    CREATE TABLE fact_(
        
    )"""
)
conn.commit()

# Insert DataFrame to Table and perform Join with other tables
cursor.execute("""
    INSERT INTO fact_()
    SELECT
        dim_._key,
    FROM dcscd
    JOIN dim_ ON dcscd. = dim_.
    JOIN dim_ ON dcscd. = dim_.
    JOIN dim_ ON dcscd. = dim_
    JOIN dim_ ON dcscd. = dim_. AND dcscd. = dim_ AND dcscd. = dim_
    """
)