from twython import Twython, TwythonError
import time
import random
from random import randint
from random import choice
from time import sleep

#Authorise
APP_KEY = 'hwtNGXTnCAjeUOgRveksZdESX'
APP_SECRET = '1YrUz3JLLD86AtwPorc4PVh1MZBUptrOnLEIeL4SWjjh1zMtma'
OAUTH_TOKEN = '20427648-Xx2mqMa0ANvyVheg8xagsrgh6sm3LtEuKUxuSylfR'
OAUTH_TOKEN_SECRET = 'KYoMPhcvq7iMOf0i9Y8p2TwDnyLbcCrPB78SNd9jRf51v'

#Prepare your twitter, you will need it for everything
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#The above should just be a single line, without the break

#simple retween keywords
naughty_words = [" -RT", "MAGA", "Brexit", "Trump", "xxx", "porn", "gay"]
good_words = ["climatechange", "bitcoin"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist

count = 0
while (count < 50):
	print 'The count is:', count
	count = count + 1
	try:
		search_results = twitter.search(q=keywords, count=1)
		for tweet in search_results["statuses"]:
			try:
				twitter.retweet(id = tweet["id_str"])
				count = count -1
				sleep(randint(3000,50000))
			except TwythonError as e:
				print e
	except TwythonError as e:
		print e