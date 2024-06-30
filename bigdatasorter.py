import pandas as pd

# Load the CSV dataset
df = pd.read_csv('Trips_Full Data.csv')

# Display the first few rows to understand the structure and contents of the dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Handle missing values: Drop rows with missing values
df = df.dropna()

# Remove duplicates if any
df = df.drop_duplicates()

# Convert data types if needed
# Example: Convert 'Population Staying at Home' to numeric
df['Population Staying at Home'] = pd.to_numeric(df['Population Staying at Home'], errors='coerce')

# Check for outliers and address them if necessary
# Example: Remove outliers in a numerical column
# Here, you can apply outlier removal for any numeric columns as needed
# For example, removing outliers in 'Population Staying at Home' column using z-score
# Calculate z-score for 'Population Staying at Home'
z_scores = (df['Population Staying at Home'] - df['Population Staying at Home'].mean()) / df['Population Staying at Home'].std()
# Filter out rows with z-score beyond a certain threshold (e.g., |z-score| > 3)
df = df[abs(z_scores) < 3]

# Save the cleaned dataset
df.to_csv('cleaned_Trips_Full Data.csv', index=False)

# Optionally, display summary statistics after cleaning
print(df.describe())