# Bullwatch

A simple script that searches for recent tweets containing the names and symbols of the most popular cryptocurrencies and scans them for keywords to evaluate the overall sentiment towards the future value of one cryptocurrency. The result is presented as the ratio of bullish tweets to bearish tweets. The list of cryptocurrencies considered can be found (and altered) in cryptos.csv

## Instructions

Clone the repo, open config.json, and replace "Insert your bearer token here" with your bearer token. To get a bearer token, you must gain access to the twitter api at https://developer.twitter.com/en/docs.

## Sample results

Results can be graphed by date. It is recommended to scale the y-axis logarithmically, as to appriciate changes more easily in coins with fairly standard values.

![newplot](https://user-images.githubusercontent.com/39555324/134785005-07f30cf1-b7c2-4fe0-a92b-c16923b95fea.png)
