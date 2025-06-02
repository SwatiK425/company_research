import requests
from bs4 import BeautifulSoup

def fetch_html_text(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.extract()
    lines = [line.strip() for line in soup.get_text(separator="\n").splitlines()]
    return "\n".join([line for line in lines if line])

def clean_earnings_text(text):
    start_keywords = ["Mark Zuckerberg", "Susan Li", "Operator:"]
    for keyword in start_keywords:
        idx = text.find(keyword)
        if idx != -1:
            return text[idx:]
    return text
