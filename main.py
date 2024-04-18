import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/catalogue/page-1.html"

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

print(soup.title.text)