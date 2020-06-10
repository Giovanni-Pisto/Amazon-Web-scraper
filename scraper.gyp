#installare python3 e beautifulsoup4 
#per far funzionare serve sudo pip3 install lxml
"""
Scaper AI v 0.0.1 
@author Pisto Giovanni
"""
import requests
from bs4 import BeautifulSoup
import smtplib

def check_price():
    url = "https://www.amazon.it/NZXT-CA-H700W-WB-Case-Gaming-Bianco/dp/B076JG8Z6N"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0 Chrome/83.0.4103.97 Safari/537.36'}
    soup = BeautifulSoup(requests.get(url,headers=headers).content,'lxml')
    title = soup.find(id='productTitle').get_text(strip=True)
    price = soup.find(id="priceblock_ourprice").get_text()
    fix_string=price.replace(",",".")
    converted_price=float(fix_string[0:5])
    print(title)
    print(converted_price)
    if (converted_price >170.9):
        send_mail()
      

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('turfhdturfhd@gmail.com','myvtjweaxbyaomru')
    subject="prezzo sceso"
    body="controlla il link\nhttps://www.amazon.it/NZXT-CA-H700W-WB-Case-Gaming-Bianco/dp/B076JG8Z6N"
    msg=f"Subject:{subject}\n\n{body}"
    server.sendmail(
        'turfhdturfhd@gmail.com',
        'pistogiovannii@gmail.com',
        msg
    )
    print("email inviata")
    server.quit

check_price()