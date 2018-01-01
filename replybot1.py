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

#set target user

target = "network_vis"
at = "@"
attarget = at + target
print attarget

#sets total tweets to search
TWEETNUM = 1

#sets URL or message to reply
#message = 'https://www.metoffice.gov.uk/public/weather/forecast/ucftnugpr'
message = " replybot test2"

#sets timing between replies (seconds)
pace = 1500

#finds user id and tweet id
#result = twitter.show_user(screen_name=target)
#print result['status']
#status = result['status']
#print status['id']
#tweet_id = status['id']
#print tweet_id



#this section tweets @ the original targetted user with the message to reply

countdown = 0
while (countdown == 0):
	try:
		#finds user id and tweet id
		result = twitter.show_user(screen_name=target)
		print result['status']
		status = result['status']
		print status['id']
		tweet_id = status['id']
		print tweet_id
		toTweet = message + attarget
		twitter.update_status(status="WELL DONE BRO! @network_vis", in_reply_to_status_id=tweet_id)
		sleep(pace)
	except TwythonError as e:
		print e
#	try:
#		toTweet = target + message
#		print toTweet
#		twitter.update_status(status=toTweet)
#		sleep(pace)
		
#	except TwythonError as e:
#		print e


print "all done"

