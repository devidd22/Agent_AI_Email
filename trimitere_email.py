import smtplib
from email.mime.text import MIMEText
def send_email(subject, html_body, sender, recipients, password):
    print("Se trimite mail-ul...")
    msg = MIMEText(html_body,"html")
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("S-a trimis mail-ul...")

