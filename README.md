# Team Hulk

## Project Description

Team Hulk set out to create a project that focused on current social media discussions around 45th President of the United States of America Donald J. Trump. This project is not aimed to be political or lean in favor of a political ideology. Instead, Team Hulk is focused on collecting data pertaining to the President in an unbiased way in an attempt to understand what people within social media are discussing about the President.

The idea to focus Team Hulk's project around the President was conceived due to social media responses both defending and attacking the President that has never been seen before. While we will not be able to analyze all social media posts or tweets relating to the President, we feel taking a sliver of this information will allow us to analyze the trends around the President's name.

As a test run, we collected a small sample of Twitter data through the Tweepy library in order to better understand the dataset we were going to be working with that the Twitter API provides us. This dataset contains bulk, detailed information of a number of gathered tweets that have been posted pertaining to the President. Because this is was just a test, the amount of time tweets were collected in was rather short. This short amount of time collecting tweet data will not occur for the actual final project.

In addition to this, our jupyter notebook requires more data cleaning before it is ready as a final project, and we plan to have it ready by the deadline. This will include organizing the data much better, and providing more in-depth descriptions and more code to analyze the data even further.

### Twitter Api

We used the Tweepy library to access Twitter's API to livestream tweets. We were interested in tweet data pertaining to President Donald J. Trump. We only streamed tweets mentioning the keyword "Donald Trump". Because we are livestreaming in realtime, the amount of data collected can vary based on the day and time the collection took place. The data collected from the program is stored in the "data.json" file and key variables can be found within the jupyter notebook. Due to Twitter's API security measures, they will time you out exponentially when someone overuses their allocated time limit to use the API. Fortunately, our program will exit on its own if it encounters that specific error. If that error is encountered, please wait between 15-60 minutes until you try to use it again. The keyword can be modified at any time if there is interest in using this code outside the project's scope.

### Data Cleaning

The Twitter API collects extensive amounts of information on a single tweet. This includes the number of favorites, retweets, person's name, time sent, and more. After we json normalized our data, we discovered over 345 columns for a single tweet. However, most of it contained NaN. This is due to the tweet not containing data that met that column's requirement. We removed all of the columns where more than half of the values were NaN and did not apply to the tweets we gathered. After that, we also noticed that there were a couple of columns that did not pertain to the scope of our work, such as the number of favorites, retweets, and likes. This data is outside of the project's scope because livestreaming tweets only allows for seeing tweets in real time, so they will always be zero or close to zero and will not provide any useful information.

### Data Analysis

In this project, we tried to learn more about the statistics of tweets that mention Trump. From the results in our notebook, we have decided our answer on the question about "Trending Tweets About President Trump Throughout the Day": Do different types of hashtags trend throughout the day depending on real world events relating to Trump? The answer was simply, yes... but no.. sorta. To further evaluate, our data does suggest that different types of hashtags trend throughout the day and is not overly dominated by one single hashtag. However, we did see some similar trending hashtags throughout the day which suggests that another factor, such as real world events relating to Trump, plays a huge factor in trending tweets about Trump. Despite this observation, we also noticed that during a worldwide pandemic (COVID-19), the hashtag #COVID19 was only ranked 23 which was lower than #LinkinPark, which ranked 19, even though President Trump was at the center of attention for poorly managing the COVID19 outbreak. This happened mainly because of the fact that we gathered data on the same day LinkinPark decided to sue President Trump from using their songs in one of Trump's campaign ad. Overall, trending hashtags that mention Donald Trump are influenced by real world events but are also drastically changing throughout the day depending on the time.

For the question about "Trump Tweeter Statistics": Are tweeters who mention Donald Trump in their tweets different or similar types of people? We believe that a vast majority of tweeters mentioning Donald Trump are somewhat similar to each other because of their public information on Twitter. Statistics like the tweeter's follow count tend to be towards the low end, with an exception of a couple of outliers being in the high follow count range. We also noted that about 99% of the people mentioning Donald Trump are not verified users. This only goes to show that many people who tweet about Trump are not known users around the world. On top of all that, we noticed a trend that many people create new Twitter accounts just to tweet at/about Donald Trump.

This project has widened our eyes on how Twitter really works, especially about tweets that mention Donald Trump. Despite our discoveries, we realize that we only just scratched the surface of what Twitter statistics can say about the way mainstream media works. There are many more interesting questions to ask and compelling answers to find, such as the reliability of retweeted status or even the categorization of positive/negative tweets about President Donald J. Trump. But on that note, we are at an end to our project for CS105.

### Prerequisites

* [Twitter Developer Account](https://developer.twitter.com/en/docs) (consumer key, consumer secret key, access token, access token secret)
* [pip installer](https://pip.pypa.io/en/stable/) (Python installer to install Tweepy)
* [Tweepy](http://docs.tweepy.org/en/latest/index.html) (Python library to access Twitter API)

### Install
The easiest and most efficient way to install this is through the Windows Subsystem for Linux (WSL). This system is available on Windows 10. To get started with WSL, [click here.](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

Once WSL is installed, open Powershell in Admin mode, run WSL, and run the following command to install the proper library:
`pip install tweepy`

### How to Run Code

In order to run the TwitterStreamer program you need a set of the following: a consumer key, consumer secret key, access token, and access token secret. However, Twitter does not allow us to share our keys/tokens, so we replaced them with placeholders. If you want to run the program yourself, you have to apply for a [Twitter Developer Account](https://developer.twitter.com/en/docs), create your own app, and generate your own keys/tokens there. *Note:* This program will livestream tweets into a file named "data.json" until the user ends the program (CTRL + C).

	git clone https://github.com/CS-UCR/final-project-hulk.git
	cd final-project-hulk
	python TwitterStreamer.py

## Authors

<a href="https://github.com/ksand012"><img src="https://avatars0.githubusercontent.com/u/35273571?s=400&u=78662d345e71ce7f5b3aaa6a14d79ada4f4296e1&v=4" align="left" height="30px"></a> **Kramer Sanders**: project logistics, part of data cleaning, document analyzer.

<a href="https://github.com/jtang073"><img src="https://avatars2.githubusercontent.com/u/49227768?s=400&u=4f70a5b1d0525a13d219ac57c2750a1f9be340ce&v=4" align="left" height="30px"></a> **Jason Tang**: created TwitterStreamer.py to use Twitter API, part of data cleaning, collected tweets.

## License

Released under the [MIT](/LICENSE) license.
