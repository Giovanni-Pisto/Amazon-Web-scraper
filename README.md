# Amazon Web Scraper 

This project automatically sends an email with the link for the purchase of the product concerned when the price of the item reaches the desired price.  When an email is sent, the ulr with the price is automatically eliminated in order to avoid spam of the same email.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purpose. See deployments for notes on how to deploy the project on a live system.

### Prerequisites 

What things you need to install the software and how to install them

* Python 3.8.x

* BeautifulSoup4

* lxml

* enable two-factor authentication google email

### Installing

If you have all the prerequisites installed without any type of error, just run the code like any python file.
In this case, I suggest you create a folder where it should contain the file.gyp and the two files.txt. 
Then run ```python3.8 file.gyp``` command

## Running the tests

You can choose two different ways to test the code. The first is to insert the links and the prices individually, the other way (faster and recommended) is to create two files called respectively ``` urls.txt``` and ``` prices.txt``` where they contain the links and prices. When an email is sent, the ulr with the price is automatically eliminated in order to avoid spam of the same email.

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
The price scan runs every x seconds, set by changing the value of ```time.sleep(60)```

## Authors
* Pisto Giovanni



