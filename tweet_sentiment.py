# -*- coding: utf-8 -*-

import tweet_scraping_engOnly
from auth_file import AuthCredentials
import tweepy
from textblob import TextBlob as tb
import pandas as pd



class AnalyzeTweet(object):
    
    def __init__(self, tweet):
        self.tweet = tweet(str)
    
    def __str__(self):
        at = AnalyzeTweet(self)
        print(at)
    
    def calculate(self):
        
        ### calulate tweet polarity and write to csv file
        def pol(self):
            
            #### initialize polarity variable and calculate polarity of tweet
            polarity = tb(self.tweet).sentiment.polarity
            
            
            with tweet_scraping_engOnly.scrape_output:
            
                for tweet in tweet_scraping_engOnly.public_tweets:
                    
                    ###### write polarity number into th Polarity collumn of csv file
                    tweet_scraping_engOnly.csv_writer.writerow({'Polarity': polarity})
        
        ### calculate tweet subjectivity and write to csv file
        def subj(self):
            
            #### initialize polarity variable and calculate polarity of tweet
            subjectivity = tb(self.tweet).sentiment.subjectivity
            
            
            with tweet_scraping_engOnly.scrape_output:
            
                for tweet in tweet_scraping_engOnly.public_tweets:
                    
                    ###### write polarity number into th Polarity collumn of csv file
                    tweet_scraping_engOnly.csv_writer.writerow({'Subjectivity': subjectivity})
                    
                    
    
    ## analyze tweet sentiment and write to csv file
    def analyze_sentiment(self):
        
        ### open csv file to complete the dataset initiated for the search
        with tweet_scraping_engOnly.scrape_output:
            
            for tweet in tweet_scraping_engOnly.public_tweets:
                
                ##### initialize sentiment analysis variable
                analysis = tb(tweet.text)
                
                ##### initialize sentiment analysis classification criteria
                pos = analysis.sentiment[0]>0
                neut = analysis.sentiment[0]==0
                neg = analysis.sentiment[0]<0
                
                if tweet == pos:
                    tweet_scraping_engOnly.csv_writer.writerow({'Sentiment Analysis': 'Positive'})
                    
                elif tweet == neut:
                    tweet_scraping_engOnly.csv_writer.writerow({'Sentiment Analysis': 'Neutral'})
                
                else:
                    tweet_scraping_engOnly.csv_writer.writerow({'Sentiment Analysis': 'Negative'})
            
            
