import requests
import aiy.cloudspeech

WHEATHER_KEY = "ea600b8da132c35933164e823ef82814"

def weatherByCity(name):
    endpoint = "http://api.openweathermap.org/data/2.5/weather"
    payload = {"q": name, "units": "metric", "appid": WHEATHER_KEY}
    return requests.get(endpoint, params=payload)

internetResult = weatherByCity('Manchester').json()
temp = internetResult['main']['temp']
city = internetResult['name']
country = internetResult['sys']['country']
weather = internetResult['weather'][0]['main']

aiy.audio.say('The weather in {0} is {1}'.format(city, weather))
aiy.audio.say('The temperature is currently {0} degrees'.format(temp))