# Web Scraping Using Beautiful Soup
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

articles = soup.find_all(name="span", class_="titleline")

article_text = [article_tag.a.getText() for article_tag in articles]
article_link = [article_tag.a.get("href") for article_tag in articles]

upvotes = soup.find_all(name="span" , class_="score")
articles_upvotes = [int(score.getText().split(" ")[0]) for score in upvotes]

highest_upvotes_index = articles_upvotes.index(max(articles_upvotes))
print(article_text[highest_upvotes_index])
print(article_link[highest_upvotes_index])
print(articles_upvotes[highest_upvotes_index])


