import requests
from bs4 import BeautifulSoup as bs


usd = int(input('Enter usd: '))
r = requests.get("https://privatbank.ua/rates-archive")
html = bs(r.text, "html.parser")
data = html.find_all('div', class_='sale')
cur = []
for i in data:
    cur.append(float(i.span.text))

print(f'GRN: {usd * cur[1]}')

