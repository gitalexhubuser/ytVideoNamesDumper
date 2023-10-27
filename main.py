import requests
from bs4 import BeautifulSoup
import json

# url = 'https://www.youtube.com/@alex.dubovyck.videos/videos'
# url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCjDdSdLJbbV0UBtzKpClmig' # me
url = 'https://www.youtube.com/feeds/videos.xml?channel_id=UCVws9TRZN49QxiIk4Q3VOgg' # atom

def downloadSiteToFile(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("Ответ 200!")

        source = response.text
        # print("source:", source)

        soup = BeautifulSoup(source, "xml")  # html.parser lxml
        
        media_title_tags = soup.find_all('media:title')
        for media_title_tag in media_title_tags:
            text_after_title = media_title_tag.get_text(strip=True)
            print(text_after_title)



if __name__ == "__main__":
    downloadSiteToFile(url)
    # findAllVideosInFile("./Assets/index.html")
    # findAllVideosInFile(r"E:\PythonProjects\ytVideoNamesDumper\Assets\index.html")
