# Web-scraper with Python

Questo progetto invia automaticamente una mail con il link per l'acquisto del prodotto interessato quando il prezzo dell'articolo arriva al prezzo desiderato.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purpose. See deployments for notes on how to deploy the project on a live system.

### Prerequisites 

What things you need to install the software and how to install them
```
Python 3.8.x

BeautifulSoup4

lxml

enable two-factor authentication google email
```
## Running the tests

Puoi scegliere due modi diversi per testare il codice. Il primo è inserire singolarmente i link e i prezzi, l'altro modo (più veloce e consigliato) è quello di creare due files chiamati rispettivamemte ```urls.txt``` e ```prices.txt``` dove contengono i link e i prezzi.
```
def read_data():
    with open('path/urls.txt') as fh:
        text = fh.read()
        urls = text.split('\n')

    with open('path/prices.txt') as fh:
        text = fh.read()
        prices = text.split('\n')

    return urls, prices
```
path= where is your file


