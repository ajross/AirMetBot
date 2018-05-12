import time
import sys
from Weather import Weather
from Tweeter import Tweeter

class AirMetBot:
    __w = Weather()
    __t = Tweeter()

    def run(self):
        while(True):
            results = self.__t.getResults()

            for r in results:
                msg = username = "@" + r.user + "\n"

                weatherResults = []

                for c in r.hashtags:
                    weather = self.__w.getMetar(c['text'])
                    if(weather):
                        weatherResults.append(weather)

                while(len(weatherResults) > 0):
                    if(len(msg) + len(weatherResults[0]) > 240):
                        self.__t.sendTweet(msg)
                        msg = username
                    msg += weatherResults.pop() + "\n"

                self.__t.sendTweet(msg, r.id)

            time.sleep(30)

            print("looping", file=sys.stderr)

