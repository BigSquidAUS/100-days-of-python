import ast
import os
from itertools import islice
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"
AV_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_parameters = {
    "apikey" : AV_API_KEY,
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_parameters = {
    "apiKey" : NEWS_API_KEY,
    "q" : COMPANY_NAME,
    "totalResults" : 3,
    "sortBy" : "popularity",
}

use_static_data = True
#Quickly used up free API call allocation so had to implement static data to continue testing code.
#use_static_data flag switches between using the API and the static data.

if use_static_data:
    with open("static_data.txt", "r") as file:
        text = file.read()
    data = ast.literal_eval(text) # Converts 'text' into a dictionary.
    data = data['Time Series (Daily)']
else:
    request = requests.get(STOCK_ENDPOINT, params=stock_parameters)
    request.raise_for_status()
    data = request.json()
    data = data['Time Series (Daily)']

closing_prices = [[key, value['4. close']] for key,value in islice(data.items(), 2)]
#islice takes first two items instead of a list of the entire dictionary.
yesterday_close = float(closing_prices[0][1])
two_day_close = float(closing_prices[1][1])

# Calculate percentage change.
close_percentage = ((yesterday_close - two_day_close) / two_day_close) * 100

up_down = "🔺" if close_percentage > 0 else "🔻" if close_percentage < 0 else "▫️"

print(f"{STOCK_NAME}: {up_down}{close_percentage:.2f}%\n")

if abs(close_percentage) >= 5 :
    #If the stock price increased or decreased by 5 or more percent then get the news headlines for that company.
    request = requests.get(NEWS_ENDPOINT,params=news_parameters)
    request.raise_for_status()
    data = request.json()
    data = data['articles']

    articles = []
    for item in data:
        articles.append([item['title'],item['description']])

    articles = articles[:3]
    #Slice list to only include first 3 items.

    for article in articles:
        print(f"{article[0]}\n{article[1]}\n")

#TODO 9. - Send each article as a separate message via Twilio.

#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""