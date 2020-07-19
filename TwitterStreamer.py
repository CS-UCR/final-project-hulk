from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = #Enter Consumer Key here
csecret = #Enter Consumer Secret Key here
atoken = #Enter Access Token here
asecret = #Enter Access Token Secret here

class streamerSetUp():
    def streamTweets(self, json_file, keywords):
        listener = TwitterListener(json_file)
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener)
        twitterStream.filter(track=keywords)

class TwitterListener(StreamListener):
    def __init__(self, json_file):
        self.json_file = json_file 

    def on_data(self, data):
        try:
            print data  #Not needed; Only used to check to see if program is still running.
            with open(self.json_file, 'a') as dataFile: #Appends data into specified file. (Does NOT overwrite)
                dataFile.write(data)
            return True
        except BaseException as error:
            print("Error: %s" % str(error))
        return True

    def on_error(self, errorCode):  #Avoid using API for a while if error code is 420, Twitter will time you out if you keep going.
        if errorCode == 420:
            print("Using Twitter API too much... Wait a while before using again.")
            return False
        print errorCode

keywords = ["donald trump"]
json_file = "data.json"
twitterStreamer = streamerSetUp()
twitterStreamer.streamTweets(json_file, keywords)
