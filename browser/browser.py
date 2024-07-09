from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_headers import Headers

class Browser:
    def init(self, waiting_time, url):
        self.waiting_time = waiting_time
        self.path = ChromeDriverManager().install()
        self.service = Service(executable_path=self.path)
        self.browser = Chrome(service=self.service)
        headers = Headers(os="win", browser="chrome", headers=True)
        gen_headers = headers.generate()
        self.options = ChromeOptions()
        for key, value in gen_headers.items():
            self.options.add_argument(f'{key}={value}')
        self.browser = Chrome(options=self.options)
        self.browser.get(url)

    def get(self, url):
        return self.browser.get(url)

    def quit(self):
        self.browser.quit()

    def get_page_source(self):
        return self.browser.page_source

    def wait_element(self, delay_seconds, by, value):
        return WebDriverWait(self.browser, delay_seconds).until(
            EC.presence_of_element_located((by, value))
        )

    def find_element(self, by, value):
        return self.browser.find_element(by, value)

    def execute_script(self, script, element):
        self.browser.execute_script(script, element)