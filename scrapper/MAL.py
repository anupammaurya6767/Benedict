import requests
from bs4 import BeautifulSoup

def fetch_anime_details(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    episode_list = soup.find_all('tr', class_='episode-list-data')
    anime_name = get_anime_name(soup)
    
    return len(episode_list), anime_name

def get_anime_name(soup):
    for elem in soup.find_all('div', class_='spaceit_pad'):
        if 'Japanese' in elem.text:
            return elem.text.replace('Japanese: ', '').replace('\n', '').strip()

# Debugger
if __name__ == '__main__':
    anime_url = 'https://myanimelist.net/anime/47917/Bocchi_the_Rock/episode'
    print(fetch_anime_details(anime_url))
