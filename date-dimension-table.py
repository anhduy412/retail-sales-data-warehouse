import pandas as pd
import pyodbc
import config

#Create date dimension dataframe
date_df = pd.DataFrame(pd.date_range('1/1/2014','12/31/2024'), columns=['day'])
date_df['year'] = date_df['day'].dt.year
date_df['quarter_number'] = date_df['day'].dt.quarter
date_df['quarter_text'] = date_df['day'].apply(lambda x: f'Q{x.quarter}_{x.strftime("%Y")}')
date_df['month'] = date_df['day'].dt.month
date_df['year_month'] = date_df['day'].dt.strftime("%b_%Y")
date_df['week'] = date_df['day'].dt.isocalendar().week.astype(int)
date_df['year_week'] = date_df['day'].apply(lambda x: f'week_{x.isocalendar()[1]}_{x.isocalendar()[0]}')
date_df['week_start'] = date_df['day'].dt.to_period('W').apply(lambda x: x.start_time)
date_df['weekday'] = date_df['day'].dt.strftime("%A")

date_df = pd.DataFrame(date_df)

# Connect Python to SQL Server
server = config.server
database = config.database
username = config.username
password = config.password

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='+server+'; DATABASE='+database+'; ENCRYPT = yes; Trusted_Connection = yes; UID='+username+'; PWD='+ password +'')
cursor = conn.cursor()

# Create date table
cursor.execute("""CREATE TABLE dim_date(
    date_key INT IDENTITY(1,1) PRIMARY KEY,
    day DATE,
    year INT,
    quarter_number INT,
    quarter_text NVARCHAR(50),
    month INT,
    year_month NVARCHAR(50),
    week INT,
    year_week NVARCHAR(50),
    week_start DATE,
    weekday NVARCHAR(50)
    )"""
)

# Insert DataFrame to Table
for row in date_df.itertuples():
    cursor.execute(
        f"INSERT INTO [dbo].[dim_date](day, year, quarter_number, quarter_text, month, year_month, week, year_week, week_start, weekday) VALUES ('{row.day}', {row.year}, {row.quarter_number}, '{row.quarter_text}', {row.month}, '{row.year_month}', {row.week}, '{row.year_week}', '{row.week_start}', '{row.weekday}');"
    )
conn.commit()
cursor.close()