import requests
from bs4 import BeautifulSoup
import json
import os

def fetch_learn_earn_projects():
    url = "https://www.binance.com/en/learn-and-earn"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = [tag.text.strip() for tag in soup.find_all("h6")]
    return list(set(titles))

def check_new_projects():
    current_projects = fetch_learn_earn_projects()

    if not os.path.exists("data.json"):
        with open("data.json", "w") as f:
            json.dump([], f)

    with open("data.json", "r") as f:
        old_projects = json.load(f)

    new_projects = [p for p in current_projects if p not in old_projects]

    if new_projects:
        with open("data.json", "w") as f:
            json.dump(current_projects, f)

    return new_projects
