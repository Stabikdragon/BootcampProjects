from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import datetime
chrome_driver = "/Users/user/Desktop/Stuffs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)



URL = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(URL)
cookie = driver.find_element(By.ID, "cookie")
white = "rgba(238, 238, 238, 1)"
grey= "rgba(102, 102, 102, 1)"
store = driver.find_elements(By.CSS_SELECTOR, "#store div")
store_specific = [item.find_element(By.CSS_SELECTOR, "b") for item in store]

highest_value = 0
is_true = True
while is_true:
    amount_of_cookies = int(driver.find_element(By.ID, "money").text)
    cookie.click()
    for x in store_specific:
        position = store_specific.index(x)
        if store[position].value_of_css_property("background-color") == white:
            # print(store[position])
            test = store[position].get_property("id")
            driver.find_element(By.ID, test).click()
            cookie.click()
            driver.implicitly_wait(1)
            time.sleep(3)
            # item_value = "".join(x.text.split(" ")[len(x.text.split(" ")) - 1].split(","))
            # if item_value != "":
            #     item_value = int(item_value)
            #     if item_value > highest_value:
            #         highest_value = item_value
            #         print(item_value)


    # time.sleep(5)
    # else:
    #     is_true = False
    #     # print(amount_of_cookies)
    #     # print(highest_value)








# purchase_amount = int(x.text.split(" ")[2])
# .value_of_css_property("background-color")
# .find_element(By.CSS_SELECTOR, "b").text