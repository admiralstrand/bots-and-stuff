from twython import Twython
twitter = Twython()

#Authorise
APP_KEY = 'hwtNGXTnCAjeUOgRveksZdESX'
APP_SECRET = '1YrUz3JLLD86AtwPorc4PVh1MZBUptrOnLEIeL4SWjjh1zMtma'
OAUTH_TOKEN = '20427648-Xx2mqMa0ANvyVheg8xagsrgh6sm3LtEuKUxuSylfR'
OAUTH_TOKEN_SECRET = 'KYoMPhcvq7iMOf0i9Y8p2TwDnyLbcCrPB78SNd9jRf51v'

#Prepare your twitter, you will need it for everything
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
#The above should just be a single line, without the break

#The obligatory first status update to test
twitter.update_status(status="baby twitter #bot test message#1 #python")