import requests
from newsapi import NewsApiClient
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY")
NEWS_KEY = os.getenv("NEWS_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
NUMBER = os.getenv("NUMBER")
url = "https://www.alphavantage.co/query"

params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : ALPHA_VANTAGE_KEY
}

response = requests.get(url , params=params)
response.raise_for_status()
data = response.json()

def get_price():
    daily_data = data["Time Series (Daily)"]
    dates = list(daily_data.keys())
    dates.sort(reverse=True)

    yesterday = dates[0]
    before_yesterday = dates[1]

    yesterday_close_value = float(daily_data[yesterday]["4. close"])
    before_yesterday_close_value = float(daily_data[before_yesterday]["4. close"])

    difference = ((yesterday_close_value - before_yesterday_close_value) / before_yesterday_close_value) * 100
    
    if abs(difference) > 5:
        header , desc = get_news()
        news_messages = ""

        for i in range(len(header)):
            news_messages += f"\nHeadline {i + 1}: {header[i]}\nBrief: {desc[i]}\n"

        if difference > 0:
            return f"TSLA:🔺{difference:.2f}%{news_messages}"
        else:
            return f"TSLA:🔻{difference:.2f}%{news_messages}"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news():
    newsapi = NewsApiClient(api_key=NEWS_KEY)
    all_articles = newsapi.get_everything(q=COMPANY_NAME, page_size=3)

    header = [article["title"] for article in all_articles["articles"]]
    desc = [article["description"] for article in all_articles["articles"]]

    return header , desc


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_notif():
    message_body = get_price()
    if message_body:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body = message_body,
            from_ = 'whatsapp:+14155238886',
            to= f'whatsapp:{NUMBER}'
        )
        print("Notification sent")
    else:
        print("No significant price change. No notification sent.")

def main():
    send_notif()

if __name__ == "__main__":
    main()
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

