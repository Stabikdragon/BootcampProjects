from bs4 import BeautifulSoup
import requests
from selenium import webdriver


FORM_URL = "https://forms.gle/b8sYCWJW5wSiDHpm7"
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.960053872807215%2C%22east%22%3A-121.10949873124873%2C%22south%22%3A36.9917413571668%2C%22west%22%3A-122.93940900956905%7D%2C%22mapZoom%22%3A11%2C%22customRegionId%22%3A%220ce0664686X1-CR1dm4kgyp6qkzp_1cunh8%22%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A374931%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A1900%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22sort%22%3A%7B%22value%22%3A%22paymenta%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

contents = requests.get(url=ZILLOW_URL, headers=headers).text

soup = BeautifulSoup( contents,'html.parser')
# # list_of_rentals = soup.find_all(class_="photo-cards")
# # print(list_of_rentals)
#
address = soup.find_all(class_ ='property-card-data')
adress_single = [item.text for item in address]

print(len(adress_single))
# print(soup)

# price=
# link=