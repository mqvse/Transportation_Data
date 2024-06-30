import pandas as pd

# Load the CSV dataset
df = pd.read_csv('Trips_Full Data.csv')

# Display the first few rows to understand the structure and contents of the dataset
print(df.head())

# Check for missing values
print("Missing Values:")
print(df.isnull().sum())

# Handle missing values: Replace NaN values with the mean of the column
df.fillna(df.mean(), inplace=True)

# Remove duplicates if any
df.drop_duplicates(inplace=True)

# Convert data types if needed
# Example: Convert 'Population Staying at Home' to numeric
df['Population Staying at Home'] = pd.to_numeric(df['Population Staying at Home'], errors='coerce')

# Check for outliers and address them if necessary
# Example: Remove outliers in a numerical column
# Here, you can apply outlier removal for any numeric columns as needed

# Save the cleaned dataset
df.to_csv('cleaned_Trips_Full Data.csv', index=False)

# Optionally, display summary statistics after cleaning
print("\nCleaned DataFrame Summary Statistics:")
print(df.describe())
