'''
This script gets all recent tweets containing the names of some of the most popular 
cryptocurrencies, and counts the ammount of them that contain the words bull or bullish
vs bear or bearish, and outputs, for each one, a ratio calculated as such:

    amount of bullish tweets / amount of bearish tweets

in an attempt to get a rough approximation of the overall sentiment towards the coin in twitter.

REMEMBER TO PUT YOUR BEARER TOKEN IN CONFIG.JSON
'''

import requests
import os
import json
import csv


# We get the bearer token for config.json
bearer_token = json.load(open('config.json','r'))['bearer_token']
if bearer_token == 'Insert your bearer token here':
    print('You must insert your bearer token from the Twitter API in the config.json file. You can get a bearer token at https://developer.twitter.com/en/docs')

# URL for recent twitters in the twitter API
search_url = "https://api.twitter.com/2/tweets/counts/recent"

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentTweetCountsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=bearer_oauth, params=params)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    with open('cryptos.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        # For every coin in the CSV file
        for coin in reader:

            # We get bullish tweets
            query_params = {'query': '("#{}" OR "#{}" OR "{}" OR "{}") (bull OR bullish)'.format(coin[0],coin[0],coin[1],coin[1])}
            positive = connect_to_endpoint(search_url, query_params)['meta']['total_tweet_count']

            # We get bearish tweets
            query_params = {'query': '("#{}" OR "#{}" OR "{}" OR "{}") (bear OR bearish)'.format(coin[0],coin[0],coin[1],coin[1])}
            negative = connect_to_endpoint(search_url, query_params)['meta']['total_tweet_count']

            print('Coin:',coin[0],'(',coin[1],')')
            if negative > 0:
                print('Ratio =',round(positive/negative,2))
            else:
                print('Ratio = ∞')
            print('Bullish posts =',positive)
            print('Bearish posts =',negative)
            print('-'*20)


if __name__ == "__main__":
    main()
