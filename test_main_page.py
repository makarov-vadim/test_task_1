from selenium import webdriver
from pages.main_page import MainPage, Locators


def get_expected_result():
    '''Функция, возвращающая ожидаемый результат теста'''
    return ("Message received!", 5, "Katalon Studio")


def get_count_elements(iterable):
    return len(iterable)


def get_max_elem(iterable):
    return max(iterable, key=len)


def test_page(browser):
    '''Тест главной страницы'''
    page = MainPage(browser)
    page.go_to_site()

    page.enter_word(Locators.LCTR_NAME, "Vadim")
    page.enter_word(Locators.LCTR_PASSWORD, "super_puper_vadim_12345")

    page.scroll()

    page.click_on(Locators.LCTR_MILK)
    page.click_on(Locators.LCTR_COFFEE)
    page.click_on(Locators.LCTR_YELLOW)

    page.scroll()

    page.click_on(Locators.LCTR_AUTOMATION)
    page.click_on(Locators.LCTR_AUTOMATION_YES)
    page.enter_word(Locators.LCTR_EMAIL, "vadim@example.com")

    automation_list = page.get_ul_list(Locators.LCTR_TOOLS)
    count_elems = get_count_elements(automation_list)
    max_elem = get_max_elem(automation_list)
    page.enter_word(Locators.LCTR_MESSAGE, f"{count_elems}\n{max_elem}")

    page.click_on(Locators.LCTR_BUTTON)
    alert_obj = browser.switch_to.alert

    assert (alert_obj.text, count_elems, max_elem) == get_expected_result()


# Прогон без использования pytest
if __name__ == "__main__":
    test_page(webdriver.Chrome())
    input("Press key to finish\n")
