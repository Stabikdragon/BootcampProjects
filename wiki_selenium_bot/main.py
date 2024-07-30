from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_driver = "/Users/user/Desktop/Stuffs/Development/chromedriver.exe"


driver = webdriver.Chrome(executable_path= chrome_driver)

driver.get("https://www.python.org/")

date = [item.text for item in (driver.find_elements(By.CSS_SELECTOR, "div.event-widget ul time"))]
test = [item.text for item in driver.find_elements(By.CSS_SELECTOR,"div.event-widget ul a")]
new_dict={}
# print(date)
for item in  range(len(date)):
    new_dict[item]= {date[item]:test[item]}



print(new_dict)
driver.close()
