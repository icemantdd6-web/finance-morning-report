import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = "https://www.cnbc.com/markets/"
    r = requests.get(url, timeout=10)
    soup = BeautifulSoup(r.text, "html.parser")

    headlines = [h.get_text() for h in soup.select("h3")][:10]

    return headlines
