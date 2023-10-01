import requests
import json
import pandas
from datetime import *



ALPHA_API_KEY = "9J3GH26FRNO416LX"
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "d23d92d02ccf4afd9f46d88eb1a92c55"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

now = datetime.now().date()
yesterday = now - timedelta(days=1)
stock_parameters = {
    "apikey": ALPHA_API_KEY,
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK_NAME,
    "outputsize":"compact"
    # "datatype":"json"

}
response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
data = response.json()["Time Series (Daily)"]

# close_price = data[f"{yesterday}"]["4. close"]

new_list = [value for (key, value) in data.items()]
yesterday_closing_price = float(new_list[0]["4. close"])
day_before_yesterday_closing_price = float(new_list[1]["4. close"])

difference = abs(yesterday_closing_price - day_before_yesterday_closing_price)

percent_diff = (yesterday_closing_price - day_before_yesterday_closing_price)/((yesterday_closing_price + day_before_yesterday_closing_price)/2)*100
positive_diff = (difference)/((difference)/2)*100

news_param = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    # "pageSize": 3,
    # "sortBy": "relevancy",
}

news_response = requests.get(NEWS_ENDPOINT, params=news_param)
news_data = news_response.json()
new_list_first_3 = [value for (key,value) in news_data.items()][2][:3]
if abs(percent_diff) > 5:
    print("Get News")
    print(news_response)
    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles.
# Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number.
# for x in new_list_first_3:
#     title = x["title"]
#     description = x["description"]
#     print(f"Title: {title}\nDescription: {description}")
#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
title_description_list = [f'Title:{x["title"]}.\nDescription:{x["description"]}' for x in new_list_first_3]




#TODO 9. - Send each article as a separate message via Twilio.
[print(i) for i in title_description_list]


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
