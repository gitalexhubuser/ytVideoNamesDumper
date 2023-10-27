from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# Путь к исполняемому файлу драйвера Selenium WebDriver
# webdriver_path = r'E:\PythonProjects\ytVideoNamesDumper\Assets\webdriver.exe' ## https://chromedriver.storage.googleapis.com/index.html?path=114.0.5735.90/
webdriver_path = r'E:\PythonProjects\ytVideoNamesDumper\Assets\geckodriver.exe' ## https://github.com/mozilla/geckodriver/releases

# Опции драйвера
# options = Options()
# options.add_argument('--headless')  # Запуск в безголовом режиме (без отображения браузера)

# Создание экземпляра драйвера
driver = webdriver.Firefox(service=Service(executable_path=webdriver_path))

# Загрузка страницы
# driver.get('https://www.youtube.com/@alex.dubovyck.videos/videos')
driver.get('https://www.youtube.com/@LuaNaZakaz/videos')

# Ждем, пока все заголовки полностью загрузятся (вы можете настроить это время в зависимости от сайта)
driver.implicitly_wait(60)

# Получаем все заголовки с помощью XPath
# media_title_elements = driver.find_elements(By.ID, 'video-title')
# media_title_elements = driver.find_elements(By.CLASS_NAME, 'style-scope ytd-rich-grid-media')
media_title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')

# Выводим текст каждого заголовка
for element in media_title_elements:
    text_after_title = element.text.strip()
    print(text_after_title)

# Закрытие драйвера
# driver.quit()
