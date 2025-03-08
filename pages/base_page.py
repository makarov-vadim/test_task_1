from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BasePage:
    """Класс, описывающий базовую страницу"""

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def go_to_site(self):
        """Метод, который открывает и разворачивает страниц"""
        self.driver.maximize_window()
        return self.driver.get(self.url)

    def find_element(self, locator, timeout=10):
        """Метод поиска элемента на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def find_elements(self, locator, timeout=10):
        """Метод поиска группы элементов на странице"""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}",
        )

    def scroll(self, value=500, timeout=2):
        """Метод, прокручивающий страниц. По умолчанию прокручивает на 500px"""
        time.sleep(timeout)
        scroll_result = self.driver.execute_script(f"window.scrollBy(0, {value})")
        time.sleep(timeout)
        return scroll_result
