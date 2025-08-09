# Doesn't Work Due Linkedin Security Check

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4261677278&f_AL=true&geoId=102478259&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&spellCorrectionEnabled=true")

wait = WebDriverWait(driver, 10)

sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH , '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')))
sign_in_button.click()

email_input = wait.until(EC.element_to_be_clickable((By.XPATH , '//*[@id="base-sign-in-modal_session_key"]')))
email_input.send_keys("jassonn.176@gmail.com")

password_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-sign-in-modal_session_password"]')))
password_input.send_keys(",X)iGN-t82%tH7u")

button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="base-sign-in-modal"]/div/section/div/div/form/div[2]/button')))
button.click()

jobs_listing = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR , '.fIPvHriRZGzoNhZfdzYSlfTgbEvyrECFataA span strong')))

for title in jobs_listing:
    try:
        driver.execute_script('arguments[0].scrollIntoView(true);', title)
        time.sleep(1)
        title.click()
        time.sleep(2)

        save_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'jobs-save-button')))
        driver.execute_script("arguments[0].scrollIntoView(true);", save_button)
        time.sleep(1)
        save_button.click()

        toast_dismiss = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.artdeco-toast-item__dismiss')))
        toast_dismiss.click()

        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, 'artdeco-toast-item')))
        time.sleep(1)
    except Exception as e:
        print(e)
        continue