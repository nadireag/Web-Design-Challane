import pandas as pd

# Read the csv file in
df = pd.read_csv('Resources/cities.csv')

# Save to file
df.to_html('data.html')

# Assign to string
table = df.to_html(index=False)
print(table)
