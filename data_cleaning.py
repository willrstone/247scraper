import pandas as pd

# Save the csv data to a new dataframe
df = pd.read_csv('recruits.csv')

# Remove any duplicate rows
df.drop_duplicates()

# Remove extra characters from ranking
df['ranking'] = df['ranking'].str.split("\n", expand=True)[0]

# Split height and weight into their own columns
df[['height', 'weight']] = df['height_weight'].str.split('/', expand=True)

# Remove extra spaces in height and weight columns
df['height'] = df['height'].apply(lambda x: str.strip(x))
df['weight'] = df['weight'].apply(lambda x: str.strip(x))

# Extract state from high_school columns
df['state'] = df['high_school'].str.extract(r'([A-Z]{2})')

# Extract feet and inches from height column to calculate total height in inches
df[['feet', 'inches']] = df['height'].str.split('-', expand=True).astype(float)
df['height_inches'] = df['feet'] * 12 + df['inches']

# 247 Sports changed position nomenclature in 2020, updated prior years to match
df['position'].replace({'SDE': 'DL', 'DUAL': 'QB', 'ILB': 'LB', 'DT': 'DL', 'OC': 'IOL', 'OLB': 'LB',
                        'PRO': 'QB', 'WDE': 'EDGE', 'OG': 'IOL', 'APB': 'RB', 'SF': 'RB'}, inplace=True)

# Dropped helper columns
df.drop(columns=['Height & Weight', 'Feet', 'Inches'], inplace=True)

# Converted ranking and weight columns to numeric values
df['ranking'] = pd.to_numeric(df['ranking'], errors='coerce')
df['weight'] = pd.to_numeric(df['weight'], errors='coerce')

# Saved new dataframe to a csv
df.to_csv('recruits_cleaned.csv', index=False)