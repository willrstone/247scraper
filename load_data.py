import os
from dotenv import load_dotenv, dotenv_values
import pandas as pd
from sqlalchemy import create_engine

load_dotenv()

# Read data from csv
df = pd.read_csv('recruits_cleaned.csv')

# Replace these placeholders with your actual values
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
host = os.getenv("HOST")
port = os.getenv("PORT")
database_name = os.getenv("DATABASE_NAME")

# Construct the database url
db_url = f'postgresql://{username}:{password}@{host}:{port}/{database_name}'

# Create SQLAlchemy engine
engine = create_engine(db_url)

# Save csv data to SQL database
df.to_sql('recruits', engine, if_exists='replace', index=False)

print(db_url)
