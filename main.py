import requests
from bs4 import BeautifulSoup
import json

# URL сайта, с которого нужно собрать информацию
url = 'https://www.youtube.com/@alex.dubovyck.videos/videos'

def downloadSiteToFile(url):

    response = requests.get(url)

    if response.status_code == 200:
        print("Ответ 200!")

        source = response.text
        print("source:", source)

        # Запись содержимого в файл
        with open("./Assets/index.html", "w", encoding="utf-8") as file:
            file.write(source)

        print("Сайт успешно сохранен в файле index.html")


def findAllVideosInFile(filePath):
    with open(filePath, encoding="utf8", errors='ignore') as file:
        source = file.read()
        # print(f"source: {source}")


        # soup = BeautifulSoup(source, "lxml")
        soup = BeautifulSoup(source, 'html.parser')
        # print(f"soup: {soup}")

        # Нахождение элемента <a> с id="video-title-link"
        a_tag = soup.find('a', id='video-title-link')

        # Получение значения атрибута "title"
        title = a_tag['title']

        print(title)



if __name__ == "__main__":
    # downloadSiteToFile(url)
    # findAllVideosInFile("./Assets/index.html")
    findAllVideosInFile(r"E:\PythonProjects\ytVideoNamesDumper\Assets\index.html")
