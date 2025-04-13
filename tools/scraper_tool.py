import requests
from bs4 import BeautifulSoup

def scrape_url(url: str) -> str:
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        return soup.get_text()[:2000]
    except Exception as e:
        return f"Failed to scrape: {e}"
