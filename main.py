from browser.browser import Browser
from scraper.scraper import Scraper
from config.variables import url, waiting_time, number_of_vacancies, pattern
from cleaner.data_cleaner import DataCleaner
import json

def main():
    browser = Browser()
    browser.init(waiting_time, url)
    scraper = Scraper()
    vacancies_data = scraper.run(browser, url, number_of_vacancies, waiting_time)
    cleaner = DataCleaner()
    cleaner.init(pattern)
    cleaned_data = cleaner.clean_data(vacancies_data)

    with open('vacancies_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(cleaned_data, json_file, ensure_ascii=False, indent=4)

    print("Данные успешно записаны в vacancies_data.json")

if __name__ == "__main__":
    main()