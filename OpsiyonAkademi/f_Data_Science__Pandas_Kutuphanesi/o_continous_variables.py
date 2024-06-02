import seaborn as sns

df = sns.load_dataset("planets")
print(df.head())

con_df = df.select_dtypes(include=['float64', 'int64'])
print(con_df.head())




" BU EĞİTİMDE KALDIM. BURDAN DEVAM EDİLMELİDİR."