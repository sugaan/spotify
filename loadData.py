import pandas as pd
from sqlalchemy import create_engine

file_path = '/Users/sugaankandhasamy/Documents/Projects/spotify-2023.csv'

df=pd.read_csv(file_path, encoding='latin-1')
print(df.head())

engine = create_engine('postgresql://postgres:test@localhost:5432/postgres')

df.to_sql('spotify_data', engine, if_exists='replace', index=False)

print("Data loaded successfully!")