from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") 
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_elements(By.CSS_SELECTOR, value="#articlecount a")

for count in article_count[1:2]:
    number = count

# number.click()
all_portals = driver.find_element(By.LINK_TEXT, value="Liz Truss")
# all_portals.click()

search = driver.find_element(By.ID, value="searchInput")
search.send_keys("Python", Keys.ENTER)
