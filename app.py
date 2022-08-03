#Solution 1  using OperWeatherMap.org API
import requests
from pprint import pprint

API_Key = "b13792e5496e29b32e8d739f3d1cb54c"

location = input("Enter Your Desired Location: ")

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid="

final_url = weather_url + API_Key
weather_data = requests.get(final_url).json()

print(weather_data)


#Solution 2 using wttr.in

import requests

city = input('Enter the city name: ')
print(city)

print('Displaying Weather report for: ' + city)

#fetch details
url = 'https://wttr.in/{}'.format(city)
result = requests.get(url)

#print result
print(result.text)
