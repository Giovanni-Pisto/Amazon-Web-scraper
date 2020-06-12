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
print("\nInserisci i link:") 
for i in range(0, n): 
    link = str(input()) 
    urls.append(link)    

#aggiunge il realtivi prezzi ai link
print("\nInserisci i prezzi:")
for i in range(0, n): 
    money = float(input()) 
    prices.append(money) 

#headers per i diversi motori di ricerca
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0 Chrome/83.0.4103.97 Safari/537.36'} 

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
            money_saved=converted_price-price
            if (converted_price<=price): 
                server = smtplib.SMTP('smtp.gmail.com',587)
                server.ehlo()
                server.starttls()
                server.ehlo()
                server.login('web.scraper.python@gmail.com','oqmbxwqhcoaerskg') 
                subject="PREZZO SCESO"
                object_="NOME PROTTO: "+product_title+title  
                body="PREZZO INIZIALE: "+str(converted_price)+" EURO\n"+"RISPARMIO CALCOLATO DI CIRCA: "+str(money_saved)+" EURO"
                link="LINK: "+url               
                msg=f"Subject:{subject}\n\n{object_}\n\n{body}\n\n{link}"
                server.sendmail(
                    'web.scraper.python@gmail.com',
                    'pistogiovannii@gmail.com',
                    msg
                )
                print("E-MAIL INVIATA")
                server.quit
                remove_link=str(url)
                remove_price=price
                if(urls.index(remove_link)&prices.index(remove_price)):
                    urls.pop((urls.index(remove_link)))
                    prices.pop(prices.index(remove_price))
                    #all_product.pop(prices.index(remove_price))
        except AttributeError:
            print ("Prezzo non trovato, controlla se il prodotto ha un prezzo esposto")
    print("lista aggiornata"+str(urls))
    print("prezzi aggiornati"+str(prices))
    print("Prezzi attuali prodotti"+str(all_product))

while(True):
    check_price()
    time.sleep(20)#controlla ogni 3 ore il tempo va messo in secondi

#   https://www.amazon.it/Corsair-Vengeance-Memorie-Desktop-Prestazioni/dp/B0143UM4TC
#   https://www.amazon.it/AMD-Ryzen-5-3600-Processori/dp/B07STGGQ18
#   https://www.amazon.it/Apple-iPhone-Grigio-Siderale-Ricondizionato/dp/B07985C44N
