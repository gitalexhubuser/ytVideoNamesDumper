# ytVideoNamesDumper

<p align="center">
    <img width="70%" src="https://i.imgur.com/88MIcf0.png">
    <img width="50%" src="https://i.imgur.com/FYQiKEv.png">
</p>

## Описание

Получаем название всех видеороликов с нужного канала.

Вручную это делал через [Web Scraper - Free Web Scraping](https://chrome.google.com/webstore/detail/web-scraper-free-web-scra/jnhgnonknehpejjnehehllkliplmbmhn)

<details>
<summary>Web Scraper</summary>

С использованием:

Selector `yt-formatted-string#video-title`

type `SelectorText`

Multiple `yes`

Parent selectors `_root`

</details>

Переделал в полноценный проект на Python, который при помощи Selenium - открывает сайт и дампит названия роликов в файл!

**Ps:** проект похож на [BogatovSirusCharDumper](https://github.com/gitalexhubuser/BogatovSirusCharDumper)

---

## Возможности

- [x] "RSS reader" последних 15 роликов [коммит](https://github.com/gitalexhubuser/ytVideoNamesDumper/tree/6f5691e7b3af995e50a0d2cabcc8bec9e0f3610d)
- [x] Дампер всех всех видео с вкладки /videos (Selenium)

---

## Использование

- Ввоидим название канала для дампа, в файл `main.py`, строка `driver.get(" ссылку сюда! ")`
- Запускаем `run.cmd`
- Забираем файл с всеми видеороликами в папке results

---

## Установка

TODO

---

# Ссылки
| Описание | Ссылка |
| ------ | ------ |
Репо: | [github.com/gitalexhubuser/ytVideoNamesDumper](https://github.com/gitalexhubuser/ytVideoNamesDumper)
