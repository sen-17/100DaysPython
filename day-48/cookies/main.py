from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

wait = WebDriverWait(driver, 10)
pick_language = wait.until(EC.presence_of_element_located((By.ID, "langSelect-EN")))
pick_language.click()

click_cookies = wait.until(EC.presence_of_element_located((By.ID, "bigCookie")))
amount_cookies = wait.until(EC.presence_of_element_located((By.ID, "cookies")))
button_1 = wait.until(EC.presence_of_element_located((By.ID, "product0")))
button_2 = wait.until(EC.presence_of_element_located((By.ID, "product1")))

# prices = [int(price.text) for price in upgrade_price[:2]]

while True:
    click_cookies.click()

    text = amount_cookies.text
    lines = text.split("\n")
    count = 0
    for line in lines:
        if "cookies" in line:
            count = int(line.split(" ")[0].replace(",", ""))
    
    upgrade_price = driver.find_elements(By.CLASS_NAME, "price")

    price_1 = int(upgrade_price[0].text.replace(",", ""))
    price_2 = int(upgrade_price[1].text.replace(",", ""))
    
    if count >= price_2:
        button_2.click()
    elif count >= price_1:
        button_1.click()
    