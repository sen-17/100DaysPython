from bs4 import BeautifulSoup
# import lxml

file_path = r"day-45\bs4-start\bs4-start\website.html"

with open(file_path , mode="r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.a)

all_anchor = soup.find_all(name="a")

for tag in all_anchor:
    # print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id = "name")
print(heading)

section_heading = soup.find(name="h3", class_ = "heading")
print(section_heading.getText())

company_url = soup.select_one(selector="p a") # '#idName' for id selector and '.className' for class selector
print(company_url)