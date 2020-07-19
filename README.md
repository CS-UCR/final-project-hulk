# Team Hulk

## Project Description

**TODO**

(identifies and describes the datasets that were used) 

also mention that sampledata.json is just a sample not our actual data.

also datacleaning jupyter notebook only has code rn but it needs more code/descriptions

### Twitter Api

We used the Tweepy library to access Twitter's API to livestream tweets. We were interested in the data around President Trump, so we only streamed tweets mentioning keywords like "Donald Trump". Since we livestream tweets in real time, the amount of data collected depends on the day and time the collection took place. The data collected from the program is stored in the "data.json" file and key variables can be found in the jupyter notebook. Twitter does not allow users to abuse their API, so they will time you out exponentially when you overuse your limit. However, our program will exit on its own if it encounters that specific error. In case you encounter that error, please wait a while until you use it again. If you wish to reuse this program for your own personal reasons, you can change the keywords variable to whatever you want.

### Data Cleaning

The Twitter API collects a lot of information on a single tweet such as the number of favorites, retweets, person's name, time and much more. After we json normalized our data, we discovered over 345 columns for a single tweet. However, most of it contained NaN so we removed all of the columns where more than half of the values were NaN. After that, we also noticed that there were a couple of columns that did not pertain to our scope of work, such as the number of favorites, retweets, and likes. These were not of interest for us because we livestreamed tweets in real time, so they will always be zero or close to zero and will not provide any useful information.

**TODO**

**... what else did we do for cleaning and EDA part here**


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
