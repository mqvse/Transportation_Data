import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset into a DataFrame (replace 'trips_by_distance.csv' with your actual file name)
df = pd.read_csv('trips_by_distance.csv')

# Trends Over Time: Line chart showing the trends in the number of trips over time
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Number of Trips'], marker='o', color='blue')
plt.title('Trends in Number of Trips Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Trips')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Distribution of Trip Distances: Histogram showing the distribution of trip distances
plt.figure(figsize=(10, 6))
plt.hist(df['Trip Distance'], bins=20, color='green', alpha=0.7)
plt.title('Distribution of Trip Distances')
plt.xlabel('Trip Distance')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation Analysis: Scatter plot illustrating correlation between trip distances and population staying at home
plt.figure(figsize=(10, 6))
plt.scatter(df['Population Staying at Home'], df['Trip Distance'], color='red', alpha=0.5)
plt.title('Correlation Between Trip Distance and Population Staying at Home')
plt.xlabel('Population Staying at Home')
plt.ylabel('Trip Distance')
plt.grid(True)
plt.tight_layout()
plt.show()

# Comparison Plots: Comparative plot comparing number of trips conducted by different groups
plt.figure(figsize=(10, 6))
plt.bar(df['Population Staying at Home'], df['Number of Trips'], color='purple', alpha=0.7)
plt.title('Comparison of Number of Trips by Population Staying at Home')
plt.xlabel('Population Staying at Home')
plt.ylabel('Number of Trips')
plt.grid(True)
plt.tight_layout()
plt.show()

# Visualization of Trends: Additional visualizations (e.g., heatmaps, stacked area charts)

