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

#twitter.update_status(status='hello world from twython')

result = twitter.show_user(screen_name='network_vis')
print result
print result['status']["id"]
#status = result['status']
#print status['id']
tweet_id = result['status']["id"]
print tweet_id