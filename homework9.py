import requests
from bs4 import BeautifulSoup

url = "https://minfin.com.ua/ua/currency/usd/"
responce = requests.get(url)
html = responce.text

soup = BeautifulSoup(html, "html.parser")
dollar_rate_element = soup.find("div", class_="sc-1x32wa2-8 tWvco")
dollar_rate_element = dollar_rate_element.text