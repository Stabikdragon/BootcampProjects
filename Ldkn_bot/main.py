from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
options = webdriver.ChromeOptions()


options.add_argument(r'--user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data')
options.add_argument(r'--profile-directory=Default')

options.add_argument('window-size=1920x1080')
chrome_driver = "/Users/user/Desktop/Stuffs/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
login_URL = "https://www.linkedin.com/home"
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3606633648&distance=25&f_AL=true&f_E=1%2C2&geoId=104119503&keywords=python%20developer&sortBy=R         "
number = 0
new_url=f"https://www.linkedin.com/jobs/search/?currentJobId=3595721089&distance=25&f_AL=true&geoId=104119503&keywords=python%20developer&sortBy=R&start={number}"


is_true = True
time.sleep(5)
driver.get(URL)
time.sleep(5)
page = 0
jobs_applied = 0
# for number in pages:
#     try:
while is_true:
    pages = driver.find_elements(By.CLASS_NAME, "artdeco-pagination__indicator--number")
    job_listing = driver.find_elements(By.CLASS_NAME, "job-card-container--clickable")  # List all job on the page
    for x in job_listing:
        x.click()# Click first job listing
        time.sleep(2)
        try:
            easy_apply_button = driver.find_element(By.CLASS_NAME,"jobs-apply-button")
            easy_apply_button.click()
            time.sleep(4)
            next_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
            next_button.click()
            time.sleep(2)
            next_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
            if next_button.text == "Review":
                next_button.click()
                time.sleep(2)
                next_button = driver.find_element(By.CLASS_NAME, "artdeco-button--primary")
                next_button.click()
                time.sleep(2)
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-button__icon")
                close_button.click()
                jobs_applied += 1
                print(jobs_applied)
            else:
                close_button = driver.find_element(By.CLASS_NAME, "artdeco-button")
                close_button.click()
                time.sleep(2)
                discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[0]
                discard_button.click()
                print("nope")

        except:
            # print("one down")
            continue
    time.sleep(2)
    page += 1
    pages[page].click()
    time.sleep(2)


