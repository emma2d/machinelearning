import pandas as pd

# Get data frame from raw data in url.
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")

# Show.
print(df.head())
