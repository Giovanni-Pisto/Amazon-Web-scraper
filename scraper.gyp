import requests
from bs4 import BeautifulSoup
import smtplib
import time

# --- functions ---
"""
def ask_for_data():
    urls = []
    prices = []

    n = int(input("Number of products: "))

    #agginge il link da controllare
    print("\nInsert link:")

    for i in range(n): 
        link = input()
        urls.append(link)    

    #aggiunge il realtivi prezzi ai link
    print("\nInsert prices:")

    for i in range(n): 
        money = input()
        prices.append(money) 

    return urls, prices
"""
def read_data():
    with open('path/urls.txt') as fh:
        text = fh.read()
        urls = text.split('\n')

    with open('path/prices.txt') as fh:
        text = fh.read()
        prices = text.split('\n')

    return urls, prices

def write_data(urls, prices):
    with open('urls.txt', 'w') as fh:
        text = "\n".join(urls)
        fh.write(text)

    with open('prices.txt', 'w') as fh:
        text = "\n".join(prices)
        fh.write(text)

def send_email(url, price, converted_price):
    money_saved = converted_price-float(price)
    print('E-MAIL INVIATA: ', url, price, converted_price)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('from@gmail.com','2-auth google pass') 
    subject="PREZZO SCESO"
    email_title="NOME PROTTO: "+product_title+title
    body="PREZZO INIZIALE: "+str(price)+" EURO\n"+"RISPARMIO CALCOLATO DI CIRCA: "+str(money_saved)+" EURO\n\n"+url              
    msg=f"Subject:{subject}\n\n{email_title}\n\n{body}"
    server.sendmail(
        'from@gmail.com',
        'to@gmail.com',
        msg
    )
    server.quit

def check(prodotti):
    fix_string = prodotti.replace(",", ".")      
    converted_price = float(fix_string[0:6])

    all_products.append(converted_price)

    if (converted_price <= float(price)): 
        send_email(url, price, converted_price)
    else:
        keep_urls.append(url)
        keep_prices.append(price)
# --- main ---

# - start -
#urls, prices = ask_for_data()
urls, prices = read_data()

#headers per i diversi motori di ricerca
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0 Chrome/83.0.4103.97 Safari/537.36'
}

while True:

    # - before loop -
    keep_urls = []
    keep_prices = []
    all_products = []

    # - loop -
    for url, price in zip(urls, prices):
        r = requests.get(url, headers=headers)
        #print(r.status_code)
        soup  = BeautifulSoup(r.content, 'lxml')
        product_title = soup.find(id='productTitle').get_text(strip=True)
        title = soup.find(id='title').get_text(strip=True)
        try:
            products = soup.find(id='price_inside_buybox').get_text()
            if(products!= ""):
                check(products)
            else:
                products1 = soup.find(id='priceblock_ourprice').get_text()
                if(products1 != ""):
                    check(products1)
                else:
                    products2 = soup.find(id='priceblock_saleprice').get_text()
                    if(products2!= ""):
                        check(products2) 
                    else:
                        products3 = soup.find(id='priceblock_dealprice').get_text()
                        if(products3!= ""):
                            check(products3)
        except AttributeError as ex:
            print("",ex)
        
    # - loop -
    urls = keep_urls
    prices = keep_prices
    #print(urls)
    print(prices)
    print(all_products)
    time.sleep(1800)

# - end -
write_data(urls, prices)
