import requests
import bs4
import lxml
PRODUCT_URL = "https://www.amazon.com/dp/B006R76WK2?ref=nb_sb_ss_w_as-proactive-reorder-desktop_proactive-reorder_nk_11_0&amp=&crid=36X8SB9C19C9N&sprefix=&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
data = response.text
soup = bs4.BeautifulSoup(data, 'lxml')
price = float(soup.find(name="span", class_="a-offscreen").getText()[1::])
target_price = 30

if price <= target_price:
    print("Hazaa!")
else:
    print("nah")