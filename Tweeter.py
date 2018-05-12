import tweepy
from config import *
from TweetResult import TweetResult

class Tweeter:
    'Class for retrieving results from timeline, and sending messages'

    __latestId = 1

    def __init__(self):
        auth = tweepy.OAuthHandler(TW_CONSUMER_KEY, TW_CONSUMER_SECRET)
        auth.set_access_token(TW_ACCESS_TOKEN, TW_ACCESS_SECRET)
        self.__api = tweepy.API(auth)

    def getResults(self):
        results = []

        for r in self.__api.mentions_timeline(self.__latestId):
            if(r.id > self.__latestId):
                self.__latestId = r.id

            if(len(r.entities['hashtags']) > 0):
                t = TweetResult(r.id, r.author.screen_name, r.entities['hashtags'])
                results.append(t)

        return results

    def sendTweet(self, msg):
        self.__api.update_status(msg)