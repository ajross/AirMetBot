#!/usr/bin/env python

from Weather import Weather
from Tweeter import Tweeter


w = Weather()
t = Tweeter()

results = t.getResults()

for r in results:
    msg = username = "@" + r.user + "\n"

    weatherResults = []

    charsUsed = len(msg)

    for c in r.hashtags:
        weather = w.getMetar(c['text'])
        if(weather):
            weatherResults.append(weather)

    while(len(weatherResults) > 0):
        if(len(msg) + len(weatherResults[0]) > 240):
            t.sendTweet(msg)
            msg = username
        msg += weatherResults.pop() + "\n"

    t.sendTweet(msg)


