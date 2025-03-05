import time
from selenium.webdriver.common.by import By

from .base_page import BasePage

class Locators:
    LOCATOR_NAME = (By.ID, "name-input")
    LOCATOR_PASSWORD = (By.CSS_SELECTOR, "[type='password']")
    LOCATOR_DRINK_1 = (By.CSS_SELECTOR, "[value='Milk']")
    LOCATOR_DRINK_2 = (By.CSS_SELECTOR, "[value='Coffee']")
    LOCATOR_COLOR = (By.CSS_SELECTOR, "[value='Yellow']")
    LOCATOR_AUTOMATION = (By.XPATH, "//select[@id='automation']")
    LOCATOR_AUTOMATION_ELEM = (By.CSS_SELECTOR, "option:nth-child(2)")
    LOCATOR_EMAIL = (By.ID, "email")
    LOCATOR_TOOLS = (By.CSS_SELECTOR, "#feedbackForm ul li")
    LOCATOR_MESSAGE = (By.ID, "message")
    LOCATOR_BUTTON = (By.ID, "submit-btn")


class SearchHelper(BasePage):

    def enter_word(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on(self, locator):
        return self.find_element(locator).click()

    def check_bar(self, locator):
        all_list = self.find_elements(locator)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu

    def scroll(self, t=2):
        scroll_result = self.driver.execute_script("window.scrollBy(0, 500)")
        time.sleep(t)
        return scroll_result
