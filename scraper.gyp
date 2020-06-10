"""
@author Pisto Giovanni
"""
import requests
from bs4 import BeautifulSoup
import smtplib
import time

def check_price():
    url = "https://www.amazon.it/NZXT-CA-H700W-WB-Case-Gaming-Bianco/dp/B076JG8Z6N"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0 Chrome/83.0.4103.97 Safari/537.36'}
    soup = BeautifulSoup(requests.get(url,headers=headers).content,'lxml')
    title = soup.find(id='productTitle').get_text(strip=True)
    price = soup.find(id="priceblock_ourprice").get_text()
    fix_string=price.replace(",",".")         #sostituisco la virgola con il punto altrimenti non posso converitre str to float
    converted_price=float(fix_string[0:5])    #fix_string[0:5] prende solo le prime 5 cifre
    if (converted_price >170.9):
        send_mail()
      

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('web.scraper.python@gmail.com','oqmbxwqhcoaerskg') #pass 2 fattori
    subject="PREZZO SCESO"
    body="CONTROLLA IL LINK\nhttps://www.amazon.it/NZXT-CA-H700W-WB-Case-Gaming-Bianco/dp/B076JG8Z6N"
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'web.scraper.python@gmail.com',
        'pistogiovannii@gmail.com',
        msg
    )
    print("E-MAIL INVIATA")
    server.quit

while(True):
    check_price()
    time.sleep(21600)#controlla ogni 6 ore il tempo va messo in secondi