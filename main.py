from urllib.request import urlopen
from bs4 import BeautifulSoup
from time import sleep

quote_page = "https://markets.businessinsider.com/stocks/aapl-stock"

page = urlopen(quote_page)

soup = BeautifulSoup(page, 'html.parser')

name_box = soup.find('h1').get_text()
print(name_box)

while True:
  page = urlopen(quote_page)
  soup = BeautifulSoup(page, 'html.parser')
  price_box = soup.find('span',{'class': 'push-data aktien-big-font text-nowrap'}).get_text()
  print (price_box)
  sleep(1)
