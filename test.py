import pandas as pd
# Read the CSV file with UTF-8 encoding
df = pd.read_csv('data/DataCoSupplyChainDataset.csv')
df.columns = [x.lower().replace(' ', '_').replace('(', '').replace(')', '') for x in df.columns]
df.to_csv('DataCoSupplyChainDatasetUTF81.csv', encoding='utf-8-sig', index=False)