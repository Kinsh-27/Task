''' Use the requests library to fetch data from a public API
 (e.g., JSONPlaceholder, Weather API, Quotes API). Parse
 and display specific information.'''

# USing open weather to fech the api key and base url
import requests
import json

apikey = "151b58b84c234a3e56db1141ebe8c580"

baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

cityName = input("Enter Your City: ")

completeURL = baseURL + cityName + "&appid=" + apikey

response = requests.get(completeURL)

data = response.json()

print(data)
