from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json

def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        EC.presence_of_element_located((by, value))
    )

path = ChromeDriverManager().install()
browser_service = Service(executable_path=path)
service = Service(executable_path=path)
browser = Chrome(service=service)

url = "https://spb.hh.ru/search/vacancy?L_save_area=true&text=python+django+flask&search_field=description&excluded_text=&area=2&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
browser.get("https://spb.hh.ru")
browser.get(url)

main_tag = wait_element(browser, 5, By.CLASS_NAME, "vacancy-serp-content")

html_data = browser.page_source
soup = BeautifulSoup(html_data, "lxml")

vacancies_tags = main_tag.find_elements(By.CLASS_NAME, "vacancy-search-item__card serp-item_link vacancy-card-container--OwxCdOj5QlSlCBZvSggS")
vacancies_data = []
for vacancy_tag in vacancies_tags:
    try:
        span_tag = vacancy_tag.find("span", {"class": "serp-item__title-link-wrapper"})
        a_tag = span_tag.find("a")
        link = a["href"]
        h2_tag = vacancy_tag.find("h2", {"class": "bloko-header-section-2"})
        salary_range = h2_tag.text
        # company_name = vacancy_tag.find("a", {"data_qa": "vacancy-serp__vacancy-employer"}).text
        div_tag = vacancy_tag.find("div", {"class": "info-section--N695JG77kqwzxWAnSePt"})
        company_name = div_tag.find("span", {"class": "company-info-text--vgvZouLtf8jwBmaD1xgp"}).text
        city_name = div_tag.find("span", {"class": "fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni"}).text
        vacancies_data.append({
            "link": link,
            "salary_range": salary_range,
            "company_name": company_name,
            "city_name": city_name
        })
    except Exception as e:
        print(f"Ошибка при обработке вакансии: {e}")

# Запись данных в файл JSON
with open('vacancies_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(vacancies_data, json_file, ensure_ascii=False, indent=4)

print("Данные успешно записаны в vacancies_data.json")



# html_data = response.text
# soup = bs4.BeautifulSoup(html_data, "lxml")
# div_tag = soup.find("div", {"data-qa": "vacancy-serp__results"})
# vacancies_tags = div_tag.findall("div", {"class": "vacancy-card--z_UXteNo7bRGzxWVcL7y font-inter"})
#
# vacancies_data = []
# for vacancy_tag in vacancies_tags:
#     h2_tag = vacancy_tag.find("h2", {"data_qa": "bloko-header-2"})
#     a_tag = h2_tag.find("a")
#     link = a["href"]
#     span_tag = vacancy_tag.find("span", {"class": "fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh"})
#     salary_range = span_tag.text
#     # company_name = vacancy_tag.find("a", {"data_qa": "vacancy-serp__vacancy-employer"}).text
#     company_name = vacancy_tag.find("span", {"class": "separate - line - on - xs - -mtby5gO4J0ixtqzW38wh"}).text
#     city_name = vacancy_tag.find("span", {"data_qa": "vacancy-serp__vacancy-address_narrow"}).text
#     vacancies_data.append({
#         "link": link,
#         "salary_range": salary_range,
#         "company_name": company_name,
#         "city_name": city_name
#     })