import requests
from bs4 import BeautifulSoup

def fetch_episode_count(url, class_name):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    episodes = soup.find_all(class_=class_name)
    return len(episodes)

def animekimi(url):
    return fetch_episode_count(url, 'episodiotitle')

def animemasters(url):
    return fetch_episode_count(url, 'text-center')

def animeshiro(url):
    return fetch_episode_count(url, 'widget-list-item')

def get_latest_episode(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    a = soup.find_all('a', class_='widget-list-item')
    b = soup.find_all('td', class_='text-center')
    c = soup.find_all('div', class_='episodiotitle')
    
    latest_episode = len(max((a, b, c), key=len))
    return latest_episode

# Debugger
if __name__ == '__main__':
    animekimi_url = "https://animekimi.com/anime/tokyo-revengers-seiya-kessen-hen/"
    print(get_latest_episode(animekimi_url))
