import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
MY_EMAIL = os.getenv("MY_EMAIL")
PASSWORD = os.getenv("PASSWORD")

headers = { 
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-67b141da-1ce46c484d879603238213fb"
}

response = requests.get(URL, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")
price = soup.find(name="span", class_="a-price-whole").getText()
cents = soup.find(name="span", class_="a-price-fraction").getText()
combine_price = f"{price}{cents}"
final_price = float(combine_price)

if final_price < 100.00:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="jassonjasson17@gmail.com", msg="Subject: PRICE ALERT!!\n\nYOUR ITEM HAS DROPPED TO BELOW 100 DOLLARS! BUY NOW!!!!!!")

print(soup.prettify())
