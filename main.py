import requests
from bs4 import BeautifulSoup
import json

# url = 'https://www.youtube.com/@alex.dubovyck.videos/videos'
url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCjDdSdLJbbV0UBtzKpClmig'

def downloadSiteToFile(url):

    response = requests.get(url)

    if response.status_code == 200:
        print("Ответ 200!")

        source = response.text
        # print("source:", source)

        soup = BeautifulSoup(source, "xml") # html.parser lxml

        # Поиск тега media:title и извлечение текста после него
        media_title_tag = soup.find('media:title')
        text_after_title = media_title_tag.get_text(strip=True)

        print(text_after_title)



if __name__ == "__main__":
    downloadSiteToFile(url)
    # findAllVideosInFile("./Assets/index.html")
    # findAllVideosInFile(r"E:\PythonProjects\ytVideoNamesDumper\Assets\index.html")
