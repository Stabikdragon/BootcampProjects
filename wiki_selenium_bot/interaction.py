import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import keys_to_typing

# keys = Keys()

# enter = keys.ENTER()
chrome_driver = "/Users/user/Desktop/Stuffs/Development/chromedriver.exe"
URL = "https://en.wikipedia.org/wiki/Main_Page"

driver = webdriver.Chrome(executable_path=chrome_driver)

driver.get(URL)
number= driver.find_element(By.CSS_SELECTOR, "#articlecount a")
search = driver.find_element(By.NAME, "search")
search.send_keys("python")
search.send_keys(Keys.ENTER)
# search.send_keys(Keys.ENTER)