url = "https://spb.hh.ru/search/vacancy?L_save_area=true&text=python+django+flask&search_field=description&excluded_text=&area=2&area=1&salary=&currency_code=RUR&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&hhtmFrom=vacancy_search_filter"
number_of_vacancies = 20
waiting_time = 10
pattern = r'от\s*(\d+[\u202f\s]*\d*)\s*([₽$])|до\s*(\d+[\u202f\s]*\d*)\s*([₽$])|(\d+[\u202f\s]*\d*)\s*–\s*(\d+[\u202f\s]*\d*)\s*([₽$])'
