""" Twitter miner that downloads the followers from the specified account """

import tweepy
import time
import json
import logging
import sys

# Twitter keys, place them in config folder
KEYFILE = "config/mykey.json"

__author__ = "Luis Natera"
__credits__ = "Miguel Salazar"
__license__ = "GPL"
__version__ = "0.5"
__maintainer__ = "Luis Natera"
__email__ = "nateraluis@gmail.com"
__status__ = "Prototype"

# Load the twitter keys
def get_key(keyfile):
	try:
		with open(keyfile) as fin:
			key = json.load(fin)
	except FileNotFoundError as e:
		print ("Key not found")
		sys.exit(1)
	return key

# Authenticate in twitter
def authenticate(key):
	api = authenticate(key)
	return auth

# Main code to run
def main():
	key = get_key(KEYFILE)
	auth = tweepy.OAuthHandler(key['consumer_key'], key['consumer_secret'])
	auth.set_access_token(key['access_token'], key['access_secret'])
	api = tweepy.API(auth)

	# Ask for the twitter account to analyse
	print("Twitter Followers Importer V0.5")
	accountvar = input ("Account name: ")

	# Generate a new file to save the data
	list = open (accountvar + "_Followers" + ".csv", 'w')
	list.write("Source,Target" +' \n')


	# Tell the API to look for the followers and the followers count
	users = tweepy.Cursor(api.followers, screen_name=accountvar).items()
	user_followers = api.get_user(screen_name=accountvar)
	no_followers = user_followers.followers_count
	count = 0
	
	print ("Downloading " + str(no_followers) + " Followers of " + accountvar)

	# Download and write the data in the file
	while True:
		try:
			user = next(users)
			list.write(user.screen_name + "," + accountvar + '\n')
			count = count + 1
			print("Downloading: " + str(count) + "/" + str(no_followers))
			time.sleep(3)
		except tweepy.TweepError:
			print ("Getting a time out, wait 15 minutes :)")
			time.sleep(60*15)
			print ("Startting again")
			user = next(users)
			list.write(user.screen_name + "," + accountvar + '\n')
			count = count+1
			print("Downloading: " + str(count) + "/" + str(no_followers))
			time.sleep (3)
		except StopIteration:
			break

# Execute the program
if __name__=="__main__":
	main()