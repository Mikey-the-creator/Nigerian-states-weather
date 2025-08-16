import pandas
import requests

weather = []
weather_description = []
Temperature = []
doc = pandas.read_csv("./ngs.csv")
doc.to_dict()
for states in range(0, 37):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={doc['Latitude'][states]}&lon={doc['Longitude'][states]}&appid=b3e45815278989324657cdc3f7dd5414")
    res = response.json()
    weather.append(res["weather"][0]["main"])
    weather_description.append(res["weather"][0]["description"])
    temp = int(res["main"]["temp"] - 273.15)
    Temperature.append(temp)
doc["weather"] = weather
doc["weather_description"] = weather_description
doc["Temperature(°c)"] = Temperature
doc.to_csv("./nigerian states with weather forcast.csv", index=False)