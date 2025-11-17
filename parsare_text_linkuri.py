import csv
import requests
from bs4 import BeautifulSoup
import csv
from google import genai
from dotenv import load_dotenv
from datetime import datetime
from htmldate import find_date
def parsare_text_linkuri():
    load_dotenv()
    print("Parsare text linkuri...")
    with open('links.csv', newline='') as f:
        reader = csv.reader(f)
        for (i,row) in enumerate(reader):
            if i == 0:
                continue
            if i >= 1:
                link = ''.join(row)
                # print(find_date(link))
                # print(link)
                url = link
                # print(datetime.today().strftime('%Y-%m-%d'))
                if datetime.today().strftime('%Y-%m-%d') == find_date(link):
                    print(find_date(link))
                    print(url)
                    try:
                        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
                        response.raise_for_status()
                    except Exception as e:
                        raise Exception("Nu se poate citi din acest URL: " + str(e))
                    soup = BeautifulSoup(response.text, 'html.parser')
                    plain_text = soup.get_text(separator='\n', strip = True)
                    # client = genai.Client()
                    # print("Se verifica daca articolul este pentru data de astazi")
                    # response = client.models.generate_content(
                    #     model = 'gemini-2.5-pro',
                    #     contents=f"""
                    #     Verifica daca articolul acesta este pentru data de {datetime.today().strftime('%Y-%m-%d')} spunand doar da sau nu si afisand pe linia urmatoare link-ul daca este pentru data de {datetime.today().strftime('%Y-%m-%d')}:
                    #     {plain_text}
                    #     """
                    # )
                    # print(response.text)
                    with open("plain_text.txt", "a") as ff:
                        ff.write("New Article\n")
                        ff.write(plain_text)