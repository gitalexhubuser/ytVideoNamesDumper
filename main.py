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

        if source is not None:
            soup = BeautifulSoup(source, "lxml")
            # print(f"soup: {soup}")

            # Имя
            videos = soup.find_all(class_="style-scope ytd-rich-grid-media")  # Замените "your-class-name" на класс, который вы ищете

            for video in videos:
                print(video)
                # print(video.text)



if __name__ == "__main__":
    # downloadSiteToFile(url)
    findAllVideosInFile("./Assets/index.html")
