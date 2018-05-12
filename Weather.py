from config import CHECKWX_API_KEY
import requests


class Weather:
    'Class for providing weather reports, and caching them for performance.'

    def __init__(self):
        self.__apiKey = CHECKWX_API_KEY
        self.__cache = {}

    def __getRemoteWeather(self, icaoCode):
        headers = {'X-API-Key': self.__apiKey}
        resp = requests.get("https://api.checkwx.com/metar/" + icaoCode, headers=headers)

        if(resp.status_code == requests.codes.ok):
            weather = resp.json()['data'][0]
            self.__cache[icaoCode] = weather
        elif(resp.status_code == requests.codes.notfound):
            weather = "Station " + icaoCode + " not found"
        else:
            weather = "Weather unavailable for " + icaoCode

        return weather

    def getMetar(self, icaoCode):
        if(icaoCode in self.__cache):
            return "Cache: " + self.__cache[icaoCode]
        else:
            return self.__getRemoteWeather(icaoCode)