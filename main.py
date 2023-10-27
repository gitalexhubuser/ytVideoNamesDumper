import requests
from bs4 import BeautifulSoup
import json

# URL сайта, с которого нужно собрать информацию
url = 'https://www.youtube.com/@alex.dubovyck.videos/videos'

# Отправка GET-запроса к сайту
response = requests.get(url)

# Создание объекта BeautifulSoup для парсинга HTML
# soup = BeautifulSoup(response.text, 'html.parser')
soup = BeautifulSoup(response.text, "lxml")

print("soup", type(soup)) # soup <class 'bs4.BeautifulSoup'>
