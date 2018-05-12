#!/usr/bin/env python
import tweepy
from config import *
from weather import getWeather

auth = tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
api = tweepy.API(auth)

latestId = 1

#api.update_status("Hello World!")

results = api.mentions_timeline(latestId)

results = [r for r in api.mentions_timeline(latestId) if len(r.entities['hashtags']) > 0]

for r in results:
    user = r.author.screen_name
    msg = "@" + user + "\n"

    possibleCodes = (c for c in r.entities['hashtags'] if len(c['text']) == 4)

    weatherResults = []

    for c in possibleCodes:
        weather = getWeather(c['text'])
        if(weather):
            weatherResults.append(weather)

    if(len(weatherResults) > 0):
        msg += "\n".join(str(w) for w in weatherResults)

    print(msg)

