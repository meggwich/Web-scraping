from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from browser.browser import Browser
import time

class Scraper:
    def run(self, browser, url, number_of_vacancies, waiting_time):
        self.url = url
        self.number_of_vacancies = number_of_vacancies
        self.waiting_time = waiting_time
        self.vacancies_data = []
        self.browser = browser
        self.browser.wait_element(waiting_time, By.CLASS_NAME, "vacancy-serp-content")
        while len(self.vacancies_data) < number_of_vacancies:
            html_data = self.browser.get_page_source()
            soup = BeautifulSoup(html_data, "lxml")
            div_tag = soup.find("div", {"id": "a11y-main-content"})
            vacancies_tags = div_tag.find_all("div", {"class": "vacancy-search-item__card serp-item_link vacancy-card-container--OwxCdOj5QlSlCBZvSggS"})

            for vacancy_tag in vacancies_tags:
                try:
                    if len(self.vacancies_data) >= number_of_vacancies:
                        break
                    link = vacancy_tag.find("span", {"class": "serp-item__title-link-wrapper"}).find("a")["href"]
                    div2_tag = (vacancy_tag.find_all("div", {"class": "narrow-container--lKMghVwoLUtnGdJIrpW4"}))[1]
                    span_tag = div2_tag.find("span", class_="fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh")
                    salary_range = span_tag.text if span_tag else "Отсутствие информации об зарплате"
                    div3_tag = vacancy_tag.find("div", {"class": "info-section--N695JG77kqwzxWAnSePt"})
                    company_name = div3_tag.find("span", {"class": "company-info-text--vgvZouLtf8jwBmaD1xgp"}).text
                    city_name = div_tag.find("span", {"class": "fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni"}).text

                    self.vacancies_data.append({
                        "link": link,
                        "salary_range": salary_range,
                        "company_name": company_name,
                        "city_name": city_name
                    })
                except Exception as e:
                    print(f"Произошла ошибка: {e}")

            if len(self.vacancies_data) % 50 == 0:
                next_button = self.browser.find_element(By.CSS_SELECTOR, "a[data-qa='pager-next']")
                self.browser.execute_script("arguments[0].scrollIntoView(true);", next_button)
                next_button.click()
                self.browser.wait_element(waiting_time, By.CLASS_NAME, "vacancy-serp-content")
                time.sleep(2)
            else:
                break

        self.browser.quit()
        return self.vacancies_data

