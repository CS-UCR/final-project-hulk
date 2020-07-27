# Team Hulk

## Project Description

Team Hulk set out to create a project that focused on current social media discussions around 45th President of the United States of America Donald J. Trump. This project is not aimed to be political or lean in favor of a political ideology. Instead, Team Hulk is focused on collecting data pertaining to the President in an unbiased way in an attempt to understand what people within social media are discussing about the President.

The idea to focus Team Hulk's project around the President was conceived due to social media responses both defending and attacking the President that has never been seen before. While we will not be able to analyze all social media posts or tweets relating to the President, we feel taking a sliver of this information will allow us to analyze the trends around the President's name.

As a test run, we collected a small sample of Twitter data through the Tweepy library in order to better understand the dataset we were going to be working with that the Twitter API provides us. This dataset contains bulk, detailed information of a number of gathered tweets that have been posted pertaining to the President. Since the actual dataset is too large, we will not be uploading it here. However, a sample dataset can be found under "sample_data.json".

As for the purpose of this project, we will be answering 2 questions relating to tweets mentioning the keyword "Donald Trump". First, we would like to know whether or not different types of hashtags trend throughout the day depending on real world events relating to Trump. Secondly, we would like to know if tweeters who mention Donald Trump in their tweets differ or are similar types of people. To answer these intriguing questions, we created the "DataCleaning.ipynb" to conduct our analysis. In depth descriptions and answers can be found inside or under the Data Analysis section down below.

### Twitter Api

We used the Tweepy library to access Twitter's API to livestream tweets. We were interested in tweet data pertaining to President Donald J. Trump. We only streamed tweets mentioning the keyword "Donald Trump". Because we are livestreaming in realtime, the amount of data collected can vary based on the day and time the collection took place. The data collected from the program is stored in the "data.json" file and key variables can be found within the jupyter notebook. Due to Twitter's API security measures, they will time you out exponentially when someone overuses their allocated time limit to use the API. Fortunately, our program will exit on its own if it encounters that specific error. If that error is encountered, please wait between 15-60 minutes until you try to use it again. The keyword can be modified at any time if there is interest in using this code outside the project's scope.

### Data Cleaning

The Twitter API collects extensive amounts of information on a single tweet. This includes the number of favorites, retweets, person's name, time sent, and many more. After we json normalized our data, we discovered over 400 columns for a single tweet. However, most of it contained NaN. This is due to the tweet not containing data that met that column's requirement. We removed all of the columns where more than half of the values were NaN and did not apply to the tweets we gathered. After that, we also noticed that there were a couple of columns that did not pertain to the scope of our work, such as the number of favorites, retweets, and likes. This data is outside of the project's scope because livestreaming tweets only allows for seeing tweets in real time, so they will always be zero or close to zero and will not provide any useful information. Strings were also refined for better readability and to ease comparison between other variables. More in depth data cleaning in the notebook.

### Prerequisites

* [Twitter Developer Account](https://developer.twitter.com/en/docs) (consumer key, consumer secret key, access token, access token secret)
* [pip installer](https://pip.pypa.io/en/stable/) (Python installer to install Tweepy)
* [Tweepy](http://docs.tweepy.org/en/latest/index.html) (Python library to access Twitter API)

### Install
The easiest and most efficient way to install this is through the Windows Subsystem for Linux (WSL). This system is available on Windows 10. To get started with WSL, [click here.](https://docs.microsoft.com/en-us/windows/wsl/install-win10)

Once WSL is installed, open Powershell in Admin mode, run WSL, and run the following command to install the proper library:
`pip install tweepy`

### How to Run Code

In order to run the TwitterStreamer program you need a set of the following: a consumer key, consumer secret key, access token, and access token secret. However, Twitter does not allow us to share our keys/tokens, so we replaced them with placeholders. If you want to run the program yourself, you have to apply for a [Twitter Developer Account](https://developer.twitter.com/en/docs), create your own app, and generate your own keys/tokens there. 

*Note:* This program will livestream tweets into a file named "data.json" until the user ends the program (CTRL + C).

	git clone https://github.com/CS-UCR/final-project-hulk.git
	cd final-project-hulk
	python TwitterStreamer.py

## Authors

<a href="https://github.com/ksand012"><img src="https://avatars0.githubusercontent.com/u/35273571?s=400&u=78662d345e71ce7f5b3aaa6a14d79ada4f4296e1&v=4" align="left" height="30px"></a> **Kramer Sanders**: project logistics, document analyzer, tweeter statistic analysis.

<a href="https://github.com/jtang073"><img src="https://avatars2.githubusercontent.com/u/49227768?s=400&u=4f70a5b1d0525a13d219ac57c2750a1f9be340ce&v=4" align="left" height="30px"></a> **Jason Tang**: created TwitterStreamer.py to use Twitter API, data cleaning, collected tweets, trending hashtag analysis, part of tweeter statistic analysis, conclusion.

## License

Released under the [MIT](/LICENSE) license.
