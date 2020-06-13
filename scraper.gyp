import requests
from bs4 import BeautifulSoup
import smtplib
import time

#   https://www.amazon.it/Corsair-Vengeance-Memorie-Desktop-Prestazioni/dp/B0143UM4TC
#   https://www.amazon.it/AMD-Ryzen-5-3600-Processori/dp/B07STGGQ18
#   https://www.amazon.it/Apple-iPhone-Grigio-Siderale-Ricondizionato/dp/B07985C44N

urls = []
prices=[]
all_product = []
n = int(input("Inserisci il numero di prodotti: "))

#agginge il link da controllare
def insert_your_links():
    print("\nInserisci prodotto:") 
    for i in range(0, n): 
        link = str(input()) 
        urls.append(link)    

#aggiunge il realtivi prezzi ai link
def insert_your_price():
    print("\nInserisci prezzo:")
    for i in range(0, n): 
        money = float(input()) 
        prices.append(money)

#headers per i diversi motori di ricerca
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0 Chrome/83.0.4103.97 Safari/537.36'} 
insert_your_links()
insert_your_price()
def check_price():
    for url, price in zip(urls, prices):
        soup  = BeautifulSoup(requests.get(url, headers=headers).content, 'lxml')
        product_title = soup.find(id='productTitle').get_text(strip=True)
        title = soup.find(id='title').get_text(strip=True) 
        try:
            products = soup.find(id='priceblock_ourprice').get_text()
            fix_string = products.replace(",", ".")      
            converted_price = float(fix_string[0:6])
            all_product.append(converted_price)
            money_saved=price-converted_price
            initial_price=converted_price+money_saved
            if (converted_price<=price): 
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login('web.scraper.python@gmail.com','oqmbxwqhcoaerskg') 
                subject="PREZZO SCESO"
                object_="NOME PROTTO: "+product_title+title  
                body="PREZZO INIZIALE: "+str(initial_price)+" EURO\n"+"RISPARMIO CALCOLATO DI CIRCA: "+str(money_saved)+" EURO"
                link="LINK: "+url               
                msg=f"Subject:{subject}\n\n{object_}\n\n{body}\n\n{link}"
                server.sendmail(
                    'web.scraper.python@gmail.com',
                    'pistogiovannii@gmail.com',
                    msg
                )
                print("E-MAIL INVIATA\n")
                server.quit
                remove_link=str(url)
                remove_price=price
                #se manda la mail rimuove link e prezzo dalle liste relative
                if(urls.index(remove_link)&prices.index(remove_price)):
                    urls.pop((urls.index(remove_link)))
                    prices.pop(prices.index(remove_price))
        except AttributeError:
            print ("Prezzo non trovato, controlla se il prodotto ha un prezzo esposto")
    print("\nLink in attesa:\n"+str(urls))
    print("\nLa tua offerta:\n"+str(prices))
    print("\nPrezzi attuali:\n"+str(all_product))
    all_product.clear()

while(True):
    check_price()
    time.sleep(1800)#secondi

#   https://www.amazon.it/Corsair-Vengeance-Memorie-Desktop-Prestazioni/dp/B0143UM4TC
#   https://www.amazon.it/AMD-Ryzen-5-3600-Processori/dp/B07STGGQ18
#   https://www.amazon.it/Apple-iPhone-Grigio-Siderale-Ricondizionato/dp/B07985C44N
 