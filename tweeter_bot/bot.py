from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER = "/Users/user/Desktop/Stuffs/Development/chromedriver.exe"
PROMISED_DOWN = 500
PROMISED_UP = 10
speedtest_url = "https://www.speedtest.net/"
twitter_url = "https://twitter.com/home"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER)
        self.down_speed = 0
        self.up_speed = 0


    def get_internet_speed(self):
        self.driver.get(speedtest_url)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()
        time.sleep(60)
        down_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        up_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        self.down_speed = float(down_speed)
        self.up_speed = float(up_speed)


    def tweet_at_provider(self, up, down):
        print(f"My up speeds are:{up} and my down speeds are:{down}.")

