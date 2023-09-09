import requests
from bs4 import BeautifulSoup
import sqlite3

class WeatherScraper:
    def __init__(self, url):
        self.url = url

    def scrape_weather(self):
        r = requests.request("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2")

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        connection = sqlite3.connect('weather.db')
        cursor = connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS url(id INTEGER PRIMARY, link VARCHAR NOT NULL, name VARCHAR);""")
        connection.commit()
        connection.close()

    def insert_data(self, data):
        connection = sqlite3.connect('weather.db')
        cursor = connection.cursor()
        cursor.execute("""INSERT INTO url(link, name) VALUES(?, ?);""", (link, name))
        connection.commit()
        connection.close()


class WeatherApp:
    def __init__(self):
        self.db_manager = DatabaseManager('weather.db')
        self.scraper = WeatherScraper('https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2')

    def run(self):
        # Код для виконання програми

if name == '__main__':
    app = WeatherApp()
    app.run()
