import re

class DataCleaner:
    def init(self, pattern):
        self.pattern = pattern

    def clean_data(self, vacancies_data):
        pattern_object = re.compile(self.pattern)
        for vacancy in vacancies_data:
            company_name = vacancy['company_name']
            cleaned_company_name = re.sub(r'\u202f|\xa0|–', ' ', company_name)
            vacancy['company_name'] = cleaned_company_name

            salary = vacancy['salary_range']
            match = pattern_object.search(salary)
            if match:
                if match.group(1):
                    vacancy['salary_range'] = f"от {match.group(1).replace('\u202f', '')} {match.group(2)}"
                elif match.group(3):
                    vacancy['salary_range'] = f"до {match.group(3).replace('\u202f', '')} {match.group(4)}"
                elif match.group(5):
                    vacancy['salary_range'] = f"от {match.group(5).replace('\u202f', '')} до {match.group(6).replace('\u202f', '')} {match.group(7)}"
        return vacancies_data