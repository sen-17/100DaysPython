import requests
from bs4 import BeautifulSoup
import html

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
FILE_PATH = r"day-45\Starting+Code+-+100+movies+to+watch+start\movies.txt"

response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents , "html.parser")

article_title = soup.find_all(name= "h3", class_ = "title")
title = [title.getText() for title in article_title]
reversed_title = list(reversed(title))

with open(FILE_PATH, mode="w", encoding="utf-8") as file:
    for titles in reversed_title:
        encoded_title = html.escape(titles)
        file.write(f"{encoded_title}\n")



