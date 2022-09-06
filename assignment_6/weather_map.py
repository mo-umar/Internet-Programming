import json
import requests
from datetime import datetime


with open("api.txt", 'r') as f:
    api_key = f.read().replace(" ", "").replace("\n", "")

API = 'https://api.openweathermap.org/data/2.5/weather?zip={},{}&appid={}'
data = requests.get(API.format(30144, 'us', api_key)).json()

print("Name: ".ljust(25) + "{}".format(data["name"]))
temp = round(1.8*(data["main"]["temp"] - 273)+32, 2)
print("Current Temperature: ".ljust(25) + "{} Degrees Fahrenheit".format(temp))
print("Atmospheric Pressure: ".ljust(25) + "{} hPa".format(data['main']['pressure']))
wind_speed = round(2.23694*data['wind']['speed'], 2)
print("Wind Speed:".ljust(25) + "{} mph".format(wind_speed))
print("Wind Direction:".ljust(25) + str(data["wind"]["deg"]))
report_time = datetime.fromtimestamp(data["dt"])
report_time = report_time.strftime("%Y-%m-%d %H:%M:%S")
print("Time of Report:".ljust(25) + str(report_time))
