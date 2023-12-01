import requests
from bs4 import BeautifulSoup

def fetch_latest_episode(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    episode_links = soup.find_all('a', class_='ep-item')
    latest_episode = len(episode_links)

    # Exclude PV episodes from the count
    for link in episode_links:
        if 'PV' in link.text:
            latest_episode -= 1

    try:
        section_bar_items = soup.find_all('li', class_='section-bar__item')
        reversed_text = section_bar_items[-1].text[::-1]
        
        latest_digit_str = ""
        for char in reversed_text:
            if char.isdigit():
                latest_digit_str += char
            else:
                break
        
        latest_episode = max(latest_episode, int(latest_digit_str[::-1]))

    except Exception:
        pass

    return latest_episode

# Debugger
if __name__ == '__main__':
    bilibili_url = "https://www.bilibili.tv/th/play/2069747"
    print(fetch_latest_episode(bilibili_url))
