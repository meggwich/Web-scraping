# Scraper вакансий

Этот проект предназначен для сбора данных о вакансиях с веб-сайта и их очистки. Проект состоит из нескольких модулей, каждый из которых выполняет свою задачу.

## Структура проекта

- main.py: Главный файл, который запускает процесс сбора и очистки данных.
- browser.py: Модуль для работы с браузером с использованием Selenium.
- scraper.py: Модуль для парсинга веб-страниц и сбора данных о вакансиях.
- data_cleaner.py: Модуль для очистки собранных данных.
- variables.py: Модуль, содержащий переменные, используемые в проекте(при желании можно изменить значения переменных, парсер работает со сбором вакансий с сайта https://spb.hh.ru. Чтобы изменить параметры поиска вакансий, воспользуйтесь возможностями веб-сайта и вставьте скопированную ссылку из браузера в этот файл. Парсер умеет лисать страницы, и при желании возможно достать все объявления о вакансии).
- requirements.txt: Файл, содержащий все необходимые библиотеки для проекта.

## Установка

1. Клонируйте репозиторий:
   
    git clone https://github.com/yourusername/vacancies-scraper.git
    cd vacancies-scraper
    
2. Установите необходимые библиотеки:
   
    pip install -r requirements.txt
    
## Использование

1. Откройте файл variables.py и настройте переменные:
    - url: URL страницы с вакансиями.
    - waiting_time: Время ожидания элементов на странице.
    - number_of_vacancies: Количество вакансий для сбора.
    - pattern: Регулярное выражение для очистки данных.

2. Запустите скрипт:
   
    python main.py
    
3. После завершения работы скрипта, данные будут сохранены в файл vacancies_data.json.

## Пример использования

```python
from browser import Browser
import scraper
from config.variables import url, waiting_time, number_of_vacancies, pattern
from cleaner.data_cleaner import DataCleaner
import json


def main():
   browser = Browser()
   browser.init(waiting_time, url)
   vacancies_data = scraper.run(browser, url, number_of_vacancies, waiting_time)
   cleaner = DataCleaner()
   cleaner.init(pattern)
   cleaned_data = cleaner.clean_data(vacancies_data)

   with open('vacancies_data.json', 'w', encoding='utf-8') as json_file:
      json.dump(cleaned_data, json_file, ensure_ascii=False, indent=4)

   print("Данные успешно записаны в vacancies_data.json")


if name == "main":
   main()
```

## Требования

Все необходимые библиотеки перечислены в файле `requirements.txt`. Убедитесь, что у вас установлены все зависимости перед запуском проекта.

## Контакты

Если у вас есть вопросы или предложения, пожалуйста, свяжитесь с нами по адресу [dixtry3826@gmail.com](mailto:dixtry3826@gmail.com).
