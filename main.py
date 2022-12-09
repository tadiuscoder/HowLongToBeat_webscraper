import csv
from bs4 import BeautifulSoup
import requests

game_nr = 1

while game_nr < 10:
    html_text = requests.get('https://howlongtobeat.com/game/{game_nr}')
    soup = BeautifulSoup(html_text, 'lxml')
    game_stats = soup.find_all('div',class_='GameHeader_profile_details__QMxb9')
    print(game_stats)
    game_nr += 1

