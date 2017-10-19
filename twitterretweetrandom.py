from twython import Twython, TwythonError
import time
import random

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
good_words = ["energy", "climatechange", "bitcoin", "dog", "carbon"]
filter = " OR ".join(good_words)
blacklist = " -".join(naughty_words)
keywords = filter + blacklist



#search_results = twitter.search(q=keywords, count=count)

list = [
    "test 1",
    "test 2",
	"test 3",
	"test 4",
    ]




	
	
	
	
count = 0
while (count < 2):
	print 'The count is:', count
	count = count + 1
	try:
		if len(list) > 0:
			toTweet = list[random.randint(0,len(list))-1]
			twitter.update_status(status=toTweet)
			list.remove(toTweet)
			time.sleep(3)
	
		else:
			twitter.update_status(status="Oh dear... I'm afraid I'm rather empty =(")
		
	except TwythonError as e:
			print e
	
print "Good bye!"		
#while True (count <> 0):
#	try:
#		for tweet in search_results["statuses"]:
#			try:
#				twitter.retweet(id = tweet["id_str"])
#				count = count -1
#				time.sleep(randint(10,60))
#	except TwythonError as e:
#       print e
		
#print count " retweets delivered"
#print "programme finished"