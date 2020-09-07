import requests
from bs4 import BeautifulSoup
import soupsieve as sv
import re
import sys

if len(sys.argv) == 4:
    artist = sys.argv[1]
    artist_id = sys.argv[2]
    search_term = sys.argv[3]
else:
    artist = 'Spice-Girls'
    artist_id = 199833
    search_term = 'good sheep'
                          
print(str(artist_id) + ' : ' + artist)
print('Search for : ' + search_term)

url = 'https://www.lyrics.com/artist.php?name=' + artist + '&aid=' + str(artist_id) + '&o=1'
page_source = requests.get(url).text
beautiful_soap_content = BeautifulSoup(page_source, "lxml")

for song in sv.select('tr', sv.select_one('tbody', beautiful_soap_content)):
    song_element = sv.select_one('a', song)
    print('\n\nSong Title : ' + song_element.text)
    song_url = 'https://www.lyrics.com' + song_element.get('href')
    print('Song URL : ' + song_url + '\n')
    song_page_source = requests.get(song_url).text
    song_page_content = BeautifulSoup(song_page_source, "lxml")
    # print('Song Lyrics')
    song_lyrics = sv.select_one('pre', song_page_content).text
    print(song_lyrics)

    # if search_term in song_lyrics :
    #     break

    if re.search(search_term, song_lyrics, re.IGNORECASE):
        print(search_term + ' Found On ' + song_element.text)
        print('URL : ' + song_url)
        break
