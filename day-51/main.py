# Complaining Twitter Bot
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PROMISED_DOWN = 50
PROMISDED_UP = 20
OOKLA_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://x.com"


class InternetSpeedTwitterBot():
    def __init__(self, url):
        self.url = url
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.url)   
        self.wait = WebDriverWait(self.driver, 10)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        time.sleep(5)
        go_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".start-button a")))
        go_button.click()

        time.sleep(40)
        down_speed = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'download-speed'))).text
        up_speed = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'upload-speed'))).text

        self.down = float(down_speed)
        self.up = float(up_speed)

        if self.down < PROMISED_DOWN or self.up < PROMISDED_UP:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        # I aint posting
        pass

internet_speed = InternetSpeedTwitterBot(OOKLA_URL)
internet_speed.get_internet_speed()
# complaint = InternetSpeedTwitterBot(TWITTER_URL)  
        
