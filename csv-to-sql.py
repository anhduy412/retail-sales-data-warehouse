import pandas as pd

df = pd.read_csv('data/DataCoSupplyChainDataset.csv', encoding='latin-1')
df = pd.DataFrame(df)
print(df)