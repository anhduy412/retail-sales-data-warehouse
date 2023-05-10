import pandas as pd

# Read the CSV file with UTF-8 encoding
df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding = 'latin-1')

# Write the DataFrame to a new CSV file with UTF-8 encoding
df.to_csv('DataCoSupplyChainDatasetUTF8.csv', encoding='utf-8-sig', index=False)