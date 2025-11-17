from gemini_prompt import aplicare_gemini
from parsare_text_linkuri import parsare_text_linkuri
from parser import parsare_articole
from trimitere_email import send_email
from datetime import datetime
from verif import stergere_fisier
parsare_articole()
parsare_text_linkuri()
aplicare_gemini()
with open('afisare_prompt.html', "r", encoding='utf-8') as f:
    data = f.read()
subject = f"Informatii Articole AI pt: {datetime.today().strftime('%Y-%m-%d')}"
html_body = data
sender = "devid.mihail@gmail.com"
recipients = ["seful2168@gmail.com"]
password = "hjcm muvo jizw leuc "

send_email(subject, html_body, sender, recipients, password)
stergere_fisier()