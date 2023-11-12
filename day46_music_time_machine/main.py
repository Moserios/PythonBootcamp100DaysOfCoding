import requests
from bs4 import BeautifulSoup
from spotifyxx import *

URL = "https://www.billboard.com/charts/hot-100/"

custom_date = input("What date do you wanna travel (YYYY-MM-DD):")
user_url = f"{URL}{custom_date}/"
response = requests.get(user_url).text
soup = BeautifulSoup(response, "lxml")
top100_titles = soup.select(selector="li h3")
song_list = [title.getText().strip() for title in top100_titles]

spotify_part(song_list, custom_date)





