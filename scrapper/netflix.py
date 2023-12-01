import requests
from bs4 import BeautifulSoup
import logging
import logging.handlers

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Setup file handler for logging
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

def fetch_latest_episode(url, episode_class):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        logger.info(soup)
        episode_titles = soup.find_all('h3', class_=episode_class)
        latest_episode = len(episode_titles)
        return latest_episode
    except Exception as e:
        logger.error(f"Error fetching data from {url}: {str(e)}")
        return 0

def netflix(url):
    return fetch_latest_episode(url, 'episode-title')

# Debugger
if __name__ == '__main__':
    netflix_url = "https://www.netflix.com/th/title/81499847"
    print(netflix(netflix_url))
