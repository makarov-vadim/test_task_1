import time
from .base_page import BasePage

from selenium.webdriver.common.by import By


class Locators:
    LCTR_NAME = (By.ID, "name-input")
    LCTR_PASSWORD = (By.CSS_SELECTOR, "[type='password']")
    LCTR_MILK = (By.ID, "drink2")
    LCTR_COFFEE = (By.ID, "drink3")
    LCTR_YELLOW = (By.ID, "color3")
    LCTR_AUTOMATION = (By.ID, "automation")
    LCTR_AUTOMATION_YES = (By.CSS_SELECTOR, "[value='yes']")
    LCTR_EMAIL = (By.ID, "email")
    LCTR_TOOLS = (By.XPATH, "//*[@id='feedbackForm']/ul/li")
    LCTR_MESSAGE = (By.ID, "message")
    LCTR_BUTTON = (By.ID, "submit-btn")


class MainPage(BasePage):
    def __init__(self, driver):
        url = "https://practice-automation.com/form-fields/"
        super().__init__(driver, url)

    def enter_word(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on(self, locator):
        clickable_element = self.find_element(locator)
        clickable_element.click()
        return clickable_element

    def check_bar(self, locator):
        all_list = self.find_elements(locator)
        nav_bar_menu = [x.text for x in all_list if len(x.text) > 0]
        return nav_bar_menu