import time, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

webdriver_path = r'E:\PythonProjects\ytVideoNamesDumper\Assets\geckodriver.exe' ## https://github.com/mozilla/geckodriver/releases

while True:
    print('\r\nEnter channel name:')
    print('Example: https://www.youtube.com/@alex.dubovyck.videos/videos')
    m = input()

    if m:
        # Загрузка страницы
        driver = webdriver.Firefox(service=Service(executable_path=webdriver_path)) # Создание экземпляра драйвера
        driver.get(m)
        # driver.get('https://www.youtube.com/@alex.dubovyck.videos/videos')

        channel_name = driver.current_url.split('.youtube.com/')[1].replace('/videos', '') # Получаем название канала из URL
        # print("channel_name", channel_name) # @AccLeiTo/videos

        # Создаем папку для сохранения результатов, если она не существует
        if not os.path.exists('results'):
            os.mkdir('results')
            print("Создал папку - results")

        file_name = f'results/{channel_name}.txt' # Создаем имя файла на основе названия канала





        # Ждем, пока все заголовки полностью загрузятся (вы можете настроить это время в зависимости от сайта)
        driver.implicitly_wait(3)
        time.sleep(3)




        # Пролистываем страницу вниз
        start_time = time.time()
        duration = 20  # Длительность в секундах
        while time.time() - start_time < duration:
            element = driver.find_element(By.TAG_NAME, 'body') # Находим любой элемент на странице и фокусируемся на нем
            element.send_keys(Keys.END) # Пролистываем страницу вниз
            time.sleep(0.1)
            element.send_keys(Keys.END) # Пролистываем страницу вниз
            time.sleep(1)
            

        media_title_elements = driver.find_elements(By.XPATH, '//*[@id="video-title"]') # (By.CSS_SELECTOR, '#video-title')
        # media_title_elements = driver.find_elements(By.CSS_SELECTOR, '#video-title') # (By.CSS_SELECTOR, '#video-title')
        # print(len(media_title_elements))
        strMediaTitleElements = str(len(media_title_elements)) # Кол-во видосов строкой

        # Открываем файл в режиме записи
        with open(file_name, 'w', encoding='utf-8') as file:
            # Выводим текст каждого заголовка
            for element in media_title_elements:
                text_after_title = element.text.strip()
                # print(text_after_title)
                file.write(text_after_title + '\n')
            print(strMediaTitleElements)
            file.write(strMediaTitleElements + '\n')

        time.sleep(5)

        # Закрытие драйвера
        driver.quit()
