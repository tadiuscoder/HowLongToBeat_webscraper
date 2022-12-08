import csv
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(chrome_options=options)

game_nr = 635

while game_nr <= 150000:
    url='https://www.howlongtobeat.com/game/'+str(game_nr)
    time.sleep(5)
    driver.get(url)
    print("Test driver.get OK")
    page = driver.page_source
    print("Test driver.page_source OK")
    soup = BeautifulSoup(page,'lxml')  
    
    print("Found page for game nr",game_nr)

    if soup.find('div',class_='GameHeader_profile_header__g1fEv shadow_text') == None:
        game_nr += 1
        print("Did not find game nr",game_nr,". Continuing to next game...")
        continue

    game_title = soup.find('div',class_='GameHeader_profile_header__g1fEv shadow_text').text
    print(game_title)
    game_stats = soup.find( 'div',class_='GameHeader_profile_details__QMxb9')
    game_stats_list = game_stats.find_all("li")
    game_rating = "NA"
    game_rating = game_stats_list[4].text
    print(game_rating)
    
    game_lengths = soup.find_all("h5")

    game_length_mainstory = "NA"
    game_length_mainsides = "NA"
    game_length_completionist = "NA"

    for i in range(0,len(game_lengths)):
        if i == 0:
            game_length_mainstory = game_lengths[i].text
        if i == 1:
            game_length_mainsides = game_lengths[i].text
        if i == 2:
            game_length_completionist = game_lengths[i].text
    print(game_length_mainstory," ",game_length_mainsides," ",game_length_completionist)
    data_to_append = [
        [game_title, game_rating, game_length_mainstory, game_length_mainsides, game_length_completionist]
    ]

    file = open('Game_rating_and_lengths.csv','a', newline='')
    writer = csv.writer(file)
    writer.writerows(data_to_append)
    file.close()
    print("Done with game",game_nr,". Going to next game")
    game_nr += 1
    

print("Web scraping of HLTB complete")
driver.quit()