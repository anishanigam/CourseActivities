
# coding: utf-8

# In[13]:


# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import requests
# import time

# import api_keys


# In[14]:


# import matplotlib.pyplot as plt
# import requests
# import pandas as pd
# import numpy as np
# import time
# from citipy import citipy
# from random import uniform


# In[15]:


# from citipy import citipy


# In[16]:


# api_key = "2dcb4762f67262ccefb859ef4223abb7"


# In[17]:


# api_key


# In[18]:


# output_data_file = "output_data/cities.csv"


# In[19]:


# api_key


# In[20]:


# column_type = ["City", "Country"]


# In[21]:


# cities_df = pd.DataFrame(columns = column_type)


# In[22]:


# column_names = ["City", "Country"]
# cities_df = pd.DataFrame(columns=column_names)


# In[23]:


# for x in range(1750):
#     lat, lng = np.random.uniform(low=-90.000, high=90.000), np.random.uniform(low=-180.000, high=180.000)
#     city = citipy.nearest_city(lat, lng)
#     cities_df = cities_df.append({"City": city.city_name,"Country": city.country_code,}, ignore_index=True)

# #Remove duplicate cities
# cities_df = cities_df.drop_duplicates(subset='City').reset_index()
# cities_df.count()


# In[24]:


# lat_range = (-90, 90)
# lng_range = (-180, 180)


# In[25]:


# lat_lngs = []
# cities = []


# In[30]:


# lats = np.random.uniform(low = - 90.000, high = 90.000, size = 1500)
# lngs = np.random.uniform(low = -180.000, high = 180.000, size = 1500)
# lat_lngs = zip(lats, lngs)


# In[31]:


# for lat_lng in lat_lngs:
#     city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name

import json
import requests
import random
import pandas as pd
import numpy as np
import time
from citipy import citipy
import matplotlib.pyplot as plt
import seaborn as sns


# In[32]:


# if city not in cities:
#     cities.append(city)
    
# len(cities)


# In[26]:



# #Create a df to add all the data from the API calls.
# column_names = ["City", "Country","Temperature (F)",
#                 "Latitude","Longitude","Humidity (%)",
#                 "Cloudiness (%)", "Wind Speed (mph)"]
# clean_cities_df = pd.DataFrame(columns=column_names)

# # Loop through the list of cities and add the data to the df.
# url = "http://api.openweathermap.org/data/2.5/weather?"

# row_count = 1


# In[27]:


# clean_cities_df.count()


# In[ ]:


# lat_range = (-90, 90)
# lng_range = (-180, 180)


# In[ ]:


# lat_lngs = []
# cities = []


# In[ ]:


# lats = np.random.uniform(low = -90.000, high = 90.000, size = 1500)
# lngs = np.random.uniform(low = -180.000, high = 180.000, size = 1500)
# lat_lngs = zip(lats, lngs)
# for lat_lng in lat_lngs:
#     city = citipy.nearest_city(lat_lng[0], lat_lng[1].city_name)
    
#     if city not in cities:
#         cities.append(city)
        
#     len(cities)


# In[ ]:


# for lat_lng in lat_lngs:
#     city = citipy.nearest_city(lat_lng[0], lat_lng[1].city_name)


# In[ ]:


# base_url = "http://api.openweathermap.org/data/2.5/weather?"


# In[ ]:


# city 


# In[ ]:


# city_name = random.choice(city)


# In[ ]:


# city_name


# In[ ]:


# complete_url = base_url + "appid" + api_key + "&q=" + city_name


# In[12]:


# Dependencies


# Import Open Weather Map API key.
# from owm_api_key import api_key


# In[13]:


# Declare variables describing the scope of lat/lng search for cities. 
# Lat ranges from -90 to 90. Lng ranges from -180 to 180.
lat = {'min': -90, 'max': 90}
lng = {'min': -180, 'max': 180}

# Create arrays containing increments of lat and long.
lat_values = np.arange(lat['min'], lat['max'], 0.01)
lng_values = np.arange(lng['min'], lng['max'], 0.01)
# Create an empty data frame to city and weather data
column_names = ('city_name', 'country_code', 'rand_lat', 'rand_lng', 'Latitude', 'Longitude','Temp (F)',
            'Humidity (%)','Cloudiness (%)','Wind Speed (mph)')
cities_df = pd.DataFrame(columns = column_names)
cities_df


# In[14]:


'''Query Citipy with random lat-long values until we collect our sample, and append weather
data via Open Weather Map API call.''' 

# Set the sample size.
sample_size = 500

target_url = 'http://api.openweathermap.org/data/2.5/weather?q='
units = 'imperial'

record = 0

# Loop through and grab the Temp, Humidity, Cloudiness and Wind Speed using OpenWeatherMapAPI
    
while len(cities_df) < sample_size:
    # Choose a random point within our lat-lng domain.
    rand_lat = random.choice(lat_values)
    rand_lng = random.choice(lng_values)
    # Call citipy's nearest_city() method to get a city object.
    city = citipy.nearest_city(rand_lat, rand_lng)
    city_name = city.city_name
    country_code = city.country_code
    # Call Open Weather Map API to obtain data and append it to df
    url = target_url + city_name + ',' + country_code + '&units=' + units + '&APPID=' + api_key
    weather_response = requests.get(url)
    weather_json = weather_response.json()
    if weather_json["cod"] == 200:
        print('City: %s. %s' % (weather_json['name'], url))
        latitude = weather_json["coord"]["lat"]
        longitude = weather_json["coord"]["lon"]
        temp = weather_json["main"]["temp"]
        humidity = weather_json["main"]["humidity"]
        cloud = weather_json["clouds"]["all"]
        wind = weather_json["wind"]["speed"]
        # Avoid repeating cities
        if city_name not in cities_df.city_name.values:
            print('Status code: %s. DF length is now: %d' % (str(weather_json["cod"]), len(cities_df)+1))
            # Append data to df columns
            cities_df.set_value(record, "city_name", city_name)
            cities_df.set_value(record, "country_code", country_code)
            cities_df.set_value(record, "rand_lat", rand_lat)
            cities_df.set_value(record, "rand_lng", rand_lng)
            cities_df.set_value(record, "Latitude", latitude)
            cities_df.set_value(record, "Longitude", longitude)
            cities_df.set_value(record, "Temp (F)", temp)
            cities_df.set_value(record, "Humidity (%)", humidity)
            cities_df.set_value(record, "Cloudiness (%)", cloud)
            cities_df.set_value(record, "Wind Speed (mph)", wind)

            record += 1
        
            # Wait between 1-4 seconds before next loop
            time.sleep(random.randint(1, 4))
        else:
            pass
    else:
        pass
    
print(
"------------------------------\n"
"Data Retrieval Complete\n"
"------------------------------\n"
)

# Visualize df
cities_df.head()


# In[ ]:


# , , s = * 10,
#            marker = "o", facecolors = "red", edgecolors = "black", alpha = 0.5, label = "Urban")


# In[15]:


type(cities_df)


# In[ ]:


# (avg_urban_city_fare, total_urban_city_rides, s = total_urban_city_drivers * 10,
#            marker = "o", facecolors = "red", edgecolors = "black", alpha = 0.5, label = "Urban")


# In[ ]:


#scatterplot


# In[ ]:


#latitude v temperature plot


# In[ ]:


#latitude v humidity plot


# In[ ]:


#latitude v cloudiness plot


# In[16]:


#city latitude v windspeed(08/22/18)


# In[17]:


len(cities_df)


# In[ ]:


# # Save the DataFrame as a csv
# cities_df.to_csv("Output/weatherpy_data.csv", encoding="utf-8", index=False)


# In[29]:


# Build a scatter plot City Latitude vs. Temperature
sns.set_style('ticks')
sns.set(style="dark")
fig, ax = plt.subplots()
p = sns.regplot(x="Latitude", y="Temp (F)", data=cities_df, fit_reg=False).set_title('Temp (F) by Latitude')

# Save the figure


# Show plot
plt.show()


# In[28]:


# Build a scatter plot City Latitude vs. Humidity
sns.set_style('ticks')
sns.set(style="dark")
fig, ax = plt.subplots()
p = sns.regplot(x="Latitude", y="Humidity (%)", data=cities_df, fit_reg=False).set_title('Humidity (%) by Latitude')

# Save the figure


# Show plot
plt.show()


# In[27]:


# Build a scatter plot City Latitude vs. Cloudiness
sns.set_style('ticks')
sns.set(style="dark")
fig, ax = plt.subplots()
p = sns.regplot(x="Latitude", y="Cloudiness (%)", data=cities_df, fit_reg=False).set_title('Cloud Cover (%) by Latitude')



# Show plot
plt.show()


# In[25]:


# Build a scatter plot City Latitude vs. Wind Speed
sns.set_style('ticks')
sns.set(style="dark")
fig, ax = plt.subplots()
p = sns.regplot(x="Latitude", y="Wind Speed (mph)", data=cities_df, fit_reg=False).set_title('Wind Speed (mph) by Latitude')

# Save the figure

# Show plot
plt.show()

