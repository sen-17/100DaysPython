from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")


input_first_name = driver.find_element(By.NAME, value="fName")
input_last_name = driver.find_element(By.NAME, value="lName")
input_email = driver.find_element(By.NAME, value="email")
click_button = driver.find_element(By.CLASS_NAME, value="btn")

input_first_name.send_keys("josua")
input_last_name.send_keys("babi")
input_email.send_keys("josuapler@gmail.com")
click_button.click()