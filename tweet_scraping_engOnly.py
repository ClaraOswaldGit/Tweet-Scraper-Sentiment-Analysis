# -*- coding: utf-8 -*-  

import tweepy
from auth_file import AuthCredentials
import csv
import re

        
class PrintTweets(object):
    
    # fetch authentication information from auth_file module
    auth = tweepy.OAuthHandler(AuthCredentials.consumer_key, AuthCredentials.consumer_key_secret)
    auth.set_access_token(AuthCredentials.access_token, AuthCredentials.access_token_secret)
    api = tweepy.API(auth)
    
    def __init__(self, keyword):
        self.keyword = keyword(str)
    
    def __str__(self):
        pt = PrintTweets(self)
        print(pt)
    
    
    # perform tweet search and print output to csv file
    def print_search(self):
        
        ## initialize variable for public tweets mentionning keyword fetched from tweepy API
        ## search function set to filter retweets (inspired by: https://twittercommunity.com/t/exclude-retweets-in-api-v2/156357)
        ## filter function set to 'en' to limit search to tweets in English
        public_tweets = self.api.search(f"{ScrapeTweets.enter_keyword.keyword} -filter:retweets").filter(languages='en')
        
        ## ask user to input name of output file to be created
        filename = input('Please enter a name for the output file.')
        
        ## create/open csv file to store scraped tweets
        ## writing to file set on append mode to allow multiple tweets to be printed one after the other
        with open(f'{filename}.csv', 'a+') as scrape_output:
            
            ### initialize field names for csv file
            fieldnames = ['Tweet Text', 'Subjectivity', 'Polarity', 'Sentiment']
            csv_writer = csv.DictWriter(scrape_output, fieldnames=fieldnames)
            
            ### write field names in csv file
            csv_writer.writeheader()
                     
            for tweet in public_tweets:
                
                #### search for tweets with keyword
                s = str(tweet.text)
                
                #### write tweets in 'Tweet Text' field of csv file
                csv_writer.writerow({'Tweet Text': s, 'Subjectivity': '', 'Polarity': '', 'Sentiment Analysis': ''})
                

class CleanTweets(object):
    
    def __init__(self, s):
        self.s = PrintTweets.print_search.s
        
    def __str__(self):
        ct = CleanTweets(self.s)
        print(ct)
       
    def remove_hashtag(self, s):
        clean_tweet = re.sub("#[A-Za-z0-9]+","",s)
        return clean_tweet
    
    def remove_arrowb(self, s):
        clean_tweet = re.sub("@[A-Za-z0-9]+","", s)
        return clean_tweet
    
    def remove_url(self, s):
        clean_tweet = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", s)
        return clean_tweet
    

    
