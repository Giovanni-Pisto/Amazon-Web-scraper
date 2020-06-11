import requests
from bs4 import BeautifulSoup
import smtplib
import time
#    "https://www.amazon.it/Corsair-Vengeance-Memorie-Desktop-Prestazioni/dp/B0143UM4TC",
#    "https://www.amazon.it/AMD-Ryzen-5-3600-Processori/dp/B07STGGQ18",
#    "https://www.amazon.it/Apple-iPhone-Grigio-Siderale-Ricondizionato/dp/B07985C44N"

urls = []
prices=[]
all_product = []
n = int(input("Inserisci il numero di prodotti: "))

#agginge il link da controllare
print("\nInserisci i link:")
for i in range(0, n): 
    link = str(input()) 
    urls.append(link)    

#aggiunge il realtivi prezzi ai link
print("\nInserisci i prezzi:")
for i in range(0, n): 
    money = int(input()) 
    prices.append(money) 

#headers per i diversi motori di ricerca
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0 Chrome/83.0.4103.97 Safari/537.36'}

def check_price():
    for url, price in zip(urls, prices):
        soup  = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')
        title = soup.find(id='productTitle').get_text(strip=True)    
        try:
            products = soup.find(id='priceblock_ourprice').get_text()
            fix_string = products.replace(",", ".")      
            converted_price = float(fix_string[0:5])
            all_product.append(converted_price)
            money_saved=converted_price-price
            if (converted_price>=price): #capire come controllare ogni elemento della lista con un  float/int
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login('web.scraper.python@gmail.com','oqmbxwqhcoaerskg') #pass 2 fattori
                subject="PREZZO SCESO"
                object_="NOME PROTTO: "+title   #titolo del prodotto
                body="RISPARMIO CALCOLATO: "+str(money_saved)+" EURO"
                link="LINK: "+url               #link del relativo prodotto
                msg=f"Subject:{subject}\n\n{object_}\n\n{body}\n\n{link}"
                server.sendmail(
                    'web.scraper.python@gmail.com',
                    'pistogiovannii@gmail.com',
                    msg
                )
                print("E-MAIL INVIATA")
                server.quit
        except AttributeError:
            print ("Prezzo non trovato, controlla se il prodotto ha un prezzo esposto")
    print(all_product)

while(True):
    check_price()
    time.sleep(21600)#controlla ogni 6 ore il tempo va messo in secondi