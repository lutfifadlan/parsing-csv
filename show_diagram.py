import matplotlib.pyplot as plt
import pandas as pd
from geopy.geocoders import Nominatim

# Read CSV file with city name and data values
df = pd.read_csv('csv-data/Original-Data.csv')

# Extract city names and data values
city_names = df['city_name']
print(type(city_names))
data_values = df['service_filter']

unique_city_names = city_names.unique()
print("unique_city_names counts: ", len(unique_city_names))

# Geocode city names to get latitude and longitude coordinates
geolocator = Nominatim(user_agent='my_app')  # Create a geolocator instance
latitude = []
longitude = []
for city_name in unique_city_names:
    print("city_name: ", city_name)
    location = geolocator.geocode(city_name)
    if location is not None:
        latitude.append(location.latitude)
        longitude.append(location.longitude)
    else:
        latitude.append(None)
        longitude.append(None)

# Create a scatter plot on a map
print("creating scatter...")
plt.scatter(longitude, latitude, c=data_values, cmap='viridis', alpha=0.5)

# Add colorbar
print("adding colorbar...")
plt.colorbar(label='Data Value')

# Set plot title and axis labels
print("setting plot title and axis labels...")
plt.title('Data Visualization on Map by City Name')
plt.xlabel('Longitude')
plt.ylabel('Latitude')

print("generating map...")

plt.savefig('map_visualization.png')

# Show the plot
# plt.show()