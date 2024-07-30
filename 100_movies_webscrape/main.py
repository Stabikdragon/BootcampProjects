import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


response = requests.get(url=URL)
contents = response.text
soup = BeautifulSoup(contents, 'html.parser').find_all(name="h3")

with open ("movies.txt",encoding='utf-8-sig', mode="w") as file:
    for x in soup[::-1]:
        movie= x.getText()
        file.writelines(movie+"\n")
