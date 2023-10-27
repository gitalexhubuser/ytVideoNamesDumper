import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

webdriver_path = r'E:\PythonProjects\ytVideoNamesDumper\Assets\geckodriver.exe' ## https://github.com/mozilla/geckodriver/releases


# Создание экземпляра драйвера
driver = webdriver.Firefox(service=Service(executable_path=webdriver_path))

# Загрузка страницы
# driver.get('https://www.youtube.com/@alex.dubovyck.videos/videos')
# driver.get('https://www.youtube.com/@LuaNaZakaz/videos')
# driver.get('https://www.youtube.com/@DarhangeR_Official/videos')
driver.get('https://www.youtube.com/@AccLeiTo/videos')



# Ждем, пока все заголовки полностью загрузятся (вы можете настроить это время в зависимости от сайта)
driver.implicitly_wait(2)
time.sleep(2)



# Пролистываем страницу вниз
start_time = time.time()
duration = 6  # Длительность в секундах
while time.time() - start_time < duration:
    # Пролистываем страницу вниз
    element = driver.find_element(By.TAG_NAME, 'body') # Находим любой элемент на странице и фокусируемся на нем
    element.send_keys(Keys.END) # Пролистываем страницу вниз
    
    # Ждем небольшую паузу перед следующей итерацией
    time.sleep(0.5)  # Настройте паузу по вашему усмотрению
    

media_title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# print(len(media_title_elements))

# Выводим текст каждого заголовка
for element in media_title_elements:
    text_after_title = element.text.strip()
    print(text_after_title)

print(len(media_title_elements))

# Получаем все заголовки с помощью XPath
# media_title_elements = driver.find_elements(By.CSS_SELECTOR, '#video-title')
# media_title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
# print(len(media_title_elements))

# Выводим текст каждого заголовка
# for element in media_title_elements:
#     text_after_title = element.get_attribute('aria-label')
#     print(text_after_title)
