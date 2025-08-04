from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

events = driver.find_elements(By.CSS_SELECTOR, ".event-widget li")

events_dict = {}

for index, event in enumerate(events, start=1):
    date = event.find_element(By.TAG_NAME, "time").text
    title = event.find_element(By.TAG_NAME, "a").text
    events_dict[index] = {
        "date": date,
        "title": title
    }

print(events_dict)


driver.quit()