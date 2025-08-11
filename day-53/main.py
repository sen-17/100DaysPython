from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

URL = 'https://appbrewery.github.io/Zillow-Clone/'
FORM_URL = 'https://forms.gle/AGSkLfUW5tWDZfaz9'
# 1. Take all of the data using beautifulsoup

response = requests.get(URL)
contents = response.text

soup = BeautifulSoup(contents , 'html.parser')

property_links = soup.find_all(name='div', class_='StyledPropertyCardPhotoBody')
links = [link.a.get('href') for link in property_links]

property_price = soup.find_all(name='span', class_='PropertyCardWrapper__StyledPriceLine')

prices = []
for price in property_price:
    full_text = price.getText()
    base_price = full_text.split('+')[0].strip().replace('/mo','')
    prices.append(base_price)

property_addr = soup.find_all(name='div', class_='StyledPropertyCardDataWrapper')
addresses = [addr.address.getText().strip() for addr in property_addr]

# 2. Fill in the forms using selenium
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM_URL)

wait = WebDriverWait(driver, 10)

for i in range (len(links)):
    address_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input = wait.until(EC.element_to_be_clickable((By.XPATH , '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))

    address_input.send_keys(addresses[i])
    price_input.send_keys(prices[i])
    link_input.send_keys(links[i])

    submit_btn = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_btn.click()

    time.sleep(2)
    driver.get(FORM_URL)







