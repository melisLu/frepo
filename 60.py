import requests
from bs4 import BeautifulSoup as bs
import sqlite3

class DB:
    def creat_table(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS url(id INTEGER PRIMARY, link VARCHAR NOT NULL, name VARCHAR);""")
        connection.commit()
        connection.close()

    def add_data(self, link, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO url(link, name) VALUES(?, ?);""", (link, name))
        connection.commit()
        connection.close()




class Parcing:
    def parc(self, link):
        r = requests.request("https://privatbank.ua/rates-archive")


class Currency:
    def curr(self,link,r):
            uah = int(input('Enter uah: '))
            html = bs(r.text, "html.parser")
            data = html.find_all('div', class_='sale')
            cur = ['EUR', 'USD', 'PLN']
            if cur == 'EUR':
                print(f'EUR: {uah * cur[0]}')
            if cur == 'USD':
                print(f'USD: {uah * cur[1]}')
            if cur == 'PLN':
                print(f'PLN: {uah * cur[2]}')








