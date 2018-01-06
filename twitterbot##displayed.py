from twython import Twython, TwythonError
import time
import random
from random import randint
from random import choice
from time import sleep
#from papirus import Papirus
#from papirus import PapirusText
#from papirus import PapirusTextPos

#configure papirus screen
#text = PapirusTextPos(rotation = 0)
#text.AddText("hello world", 0, 25, Id="Start" )

#Authorise
APP_KEY = 'hwtNGXTnCAjeUOgRveksZdESX'
APP_SECRET = '1YrUz3JLLD86AtwPorc4PVh1MZBUptrOnLEIeL4SWjjh1zMtma'
OAUTH_TOKEN = '20427648-Xx2mqMa0ANvyVheg8xagsrgh6sm3LtEuKUxuSylfR'
OAUTH_TOKEN_SECRET = 'KYoMPhcvq7iMOf0i9Y8p2TwDnyLbcCrPB78SNd9jRf51v'

#Prepare your twitter, you will need it for everything
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#The above should just be a single line, without the break

#keywords for search query q
naughty_words = [" -RT", "MAGA", "Brexit", "Trump", "xxx", "porn", "gay", "tory", "labour", "conservative", "brexit", "russia"]
good_words = ["mountaineering", "solarpv", "biomass", "windpower", "climatechange" "#antarctica", "#fission", "#tate"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

#sets total tweets number to automate
TWEETNUM = 10

#creates empty list for twitter IDs
list = []

#retreives tweet data from API then adds the id strings (a unique id number) to the list
search_results = twitter.search(q=keywords, count=TWEETNUM)
for tweet in search_results["statuses"]:
    try:
        list.append(tweet["id_str"])
        print list
    except TwythonError as e:
        print e

print 'now my code continues'

#this section tweets by randomly selecting id strings from the list, cleaning them update
#(for somwe reason they are added to the list with some extra character) and retweets them
#then removes them from the list

countdown = TWEETNUM
while (countdown <> 0):
    print 'The count is:', countdown
#    text.AddText("the count is", 0, 25, Id="Start" )
    try:
        toTweet = list[random.randint(0,len(list))-1]
        list.remove(toTweet)
        toTweet[2:19]
        print toTweet
        twitter.retweet(id = toTweet)
        countdown = countdown -1
        sleep(randint(3,6)
    except: TwythonError as e
#        print e
#print 'all done'