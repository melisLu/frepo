import urllib.request
import requests
from bs4 import BeautifulSoup as bs
#opener = urllib.request.build_opener()
#responce = opener.open("https://uk.wikipedia.org/wiki/%D0%9A%D0%B8%D1%97%D0%B2")
#print(responce.read())

#r = requests.get("https://uk.wikipedia.org/wiki/%D0%9A%D0%B8%D1%97%D0%B2")
#html = bs(r.text, "html.parser")
#data = html.find_all('div', class_ = 'noprint')
#for i in data:
    #print(i.text)

uah = int(input('Enter uah: '))
r = requests.get("https://privatbank.ua/rates-archive")
html = bs(r.text, "html.parser")
data = html.find_all('div', class_ = 'purchase')
cur = []
for i in data:
   cur.append(float(i.span.text))
print(uah)
print(cur)
print(f'EUR: {uah / cur[0]}\nUSD: {uah / cur[1]}\nPLN: {uah / cur[2]}')

