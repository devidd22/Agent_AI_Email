import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
rows = []
def parsare_articole():
    # with open("links.csv", "r") as f:
    #     csvreader = csv.reader(f)
    #     fields = next(csvreader)
    #     for row in csvreader:
    #         rows.append(row)
    #     for row in rows[:5]:
    #         url = ''.join
            
    print("Parsare Articole...")
    url = 'https://www.artificialintelligence-news.com/'
    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
    except Exception as e:
        raise Exception("Nu se poate citi din acest URL: " + str(e))

    soup = BeautifulSoup(response.text, 'html.parser')
    links_from_page = []

    #pt h1
    for h1 in soup.find_all('h1'):
        a_tag = h1.find('a')
        if a_tag and a_tag.get('href'):
            links_from_page.append(a_tag.get('href'))
    #pt h2
    for h2 in soup.find_all('h2'):
        a_tag = h2.find('a')
        if a_tag and a_tag.get('href'):
            links_from_page.append(a_tag.get('href'))
            
    #pt h3
    for h3 in soup.find_all('h3'):
        a_tag = h3.find('a')
        if a_tag and a_tag.get('href'):
            links_from_page.append(a_tag.get('href'))

    links_from_page = list(set(links_from_page))

    #salvare csv
    df = pd.DataFrame(links_from_page, columns=['link'])
    df.to_csv("links.csv", index=False)

    print(f"Am găsit {len(links_from_page)} linkuri și le-am salvat în links.csv")