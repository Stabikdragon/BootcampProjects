import requests

from bs4 import BeautifulSoup

URL = "https://www.billboard.com/charts/hot-100/"
# question = input("Which year do you want to travel to? Type the dat in this format YYYY-MM-DD:\n")
question = "2021-12-12"
SPOTIPY_CLIENT_ID = "76561ba749d341a2b277429deb20ac68"
SPOTIPY_CLIENT_SECRET ="9230efdb4c9d4c7ab72296220c106758"
CLIENT_REDIRECT = "http://example.com"
USER_ID = "22njsbpycmqptcxpbux7y2kka"
response = requests.get(url=URL + question)
content = response.text
soup = BeautifulSoup(content,'html.parser')
song_list = [x.getText().strip() for x in soup.select("li ul li h3")]
artist_list = [x.getText().strip() for x in soup.find_all(name="span", class_="u-max-width-330")]
print(artist_list[0])
print(song_list[0])


import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = SpotifyOAuth(client_id="76561ba749d341a2b277429deb20ac68", client_secret="9230efdb4c9d4c7ab72296220c106758", redirect_uri="http://example.com", scope="playlist-modify")
spotify = spotipy.Spotify(auth_manager=sp)


for x in song_list:
    try:
        position = song_list.index(x)
        song = spotify.search(q=f"track:{x} year:2021 artist: {artist_list[position]}", type="track")
        song_id = song["tracks"]["items"][0]["uri"]
        spotify.playlist_add_items(playlist_id="7s0iAzw4fYgFWgy7zrO697", items=[song_id], position=None)

    except:
        print('pass')

