import pandas as pd

# Load the datasets
trips_by_distance = pd.read_csv('cleaned_Trips_By_Distance.csv')
trips_full_data = pd.read_csv('cleaned_Trips_Full Data.csv')

# Check the column names to find the correct one
print(trips_full_data.columns)

# Calculate the number of people staying at home
people_staying_at_home = trips_full_data['Population Staying at Home'].mean()

# Calculate the average distance traveled by people who are not staying at home
# Assuming you want the average distance for trips between 1-25 miles
# Adjust the column name accordingly
average_distance_travelled = trips_full_data['Trips 1-25 Miles'].mean()

# Print the results
print("Number of people staying at home:", people_staying_at_home)
print("Average distance traveled by people who don't stay at home:", average_distance_travelled)
