# Team Hulk

## Project Description

**TODO**

(identifies and describes the datasets that were used) 

also mention that sampledata.json is just a sample not our actual data.

also datacleaning jupyter notebook only has code rn but it needs more code/descriptions

### Twitter Api

We used the Tweepy library to access Twitter's API to livestream tweets. We were interested in tweet data pertaining to President Donald J. Trump. We only streamed tweets mentioning the keyword "Donald Trump". Because we are livestreaming in realtime, the amount of data collected can vary based on the day and time the collection took place. The data collected from the program is stored in the "data.json" file and key variables can be found within the jupyter notebook. Due to Twitter's API security measures, they will time you out exponentially when someone overuses their allocated time limit to use the API. Fortunately, our program will exit on its own if it encounters that specific error. If that error is encountered, please wait between 15-60 minutes until you try to use it again. The keyword can be modified at any time if there is interest in using this code outside the project's scope.

### Data Cleaning

The Twitter API collects extensive amounts of information on a single tweet. This includes the number of favorites, retweets, person's name, time sent, and more. After we json normalized our data, we discovered over 345 columns for a single tweet. However, most of it contained NaN. This is due to the tweet not containing data that met that column's requirement. We removed all of the columns where more than half of the values were NaN and did not apply to the tweets we gathered. After that, we also noticed that there were a couple of columns that did not pertain to the scope of our work, such as the number of favorites, retweets, and likes. This data is outside of the project's scope because livestreaming tweets only allows for seeing tweets in real time, so they will always be zero or close to zero and will not provide any useful information.

As a test run, we collected a small sample of Tweet data through the Tweepy library in order to better understand the dataset the Twitter API provides us. Because this is was just a test, the amount of time tweets were collected was rather short to quickly get a sense of the information we were receiving.


### Prerequisites

* [Twitter Developer Account](https://developer.twitter.com/en/docs) (consumer key, consumer secret key, access token, access token secret)
* [pip installer](https://pip.pypa.io/en/stable/) (Python installer to install Tweepy)
* [Tweepy](http://docs.tweepy.org/en/latest/index.html) (Python library to access Twitter API)

### Install

`pip install tweepy`

### How to Run Code

In order to run the TwitterStreamer program you need a set of consumer key, consumer secret key, access token, and access token secret. However, Twitter does not allow us to share our keys/tokens, so we replaced them with placeholders. If you want to run the program yourself, you have to apply for a [Twitter Developer Account](https://developer.twitter.com/en/docs), create your own app, and generate your own keys/tokens there. *Note:* Program will livestream tweets into a file named "data.json" until the user ends the program (CTRL + C).

	git clone https://github.com/CS-UCR/final-project-hulk.git
	cd final-project-hulk
	python TwitterStreamer.py

## Authors

<a href="https://github.com/ksand012"><img src="https://avatars0.githubusercontent.com/u/35273571?s=400&u=78662d345e71ce7f5b3aaa6a14d79ada4f4296e1&v=4" align="left" height="30px"></a> **Kramer Sanders**: project logistics, part of data cleaning, **TODO (contributions)**

<a href="https://github.com/jtang073"><img src="https://avatars2.githubusercontent.com/u/49227768?s=400&u=4f70a5b1d0525a13d219ac57c2750a1f9be340ce&v=4" align="left" height="30px"></a> **Jason Tang**: created TwitterStreamer.py to use Twitter API, part of data cleaning, collected tweets

## License

Released under the [MIT](/LICENSE) license.
