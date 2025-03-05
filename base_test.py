from selenium import webdriver
from pages.main_page import SearchHelper, Locators

# Мои методы
def get_count_elements(iterable):
    return len(iterable)

def get_len_max_elem(iterable):
    return len(max(iterable, key=len))



def test(browser):
    main_page = SearchHelper(browser)
    main_page.go_to_site()

    main_page.enter_word(Locators.LOCATOR_NAME, "Ivan")
    main_page.enter_word(Locators.LOCATOR_PASSWORD, "123")

    main_page.scroll()
    main_page.click_on(Locators.LOCATOR_DRINK_1)
    main_page.click_on(Locators.LOCATOR_DRINK_2)
    main_page.click_on(Locators.LOCATOR_COLOR)

    main_page.scroll()
    main_page.click_on(Locators.LOCATOR_AUTOMATION)
    main_page.click_on(Locators.LOCATOR_AUTOMATION_ELEM)
    main_page.enter_word(Locators.LOCATOR_EMAIL, "Ivan@example.com")

    automation_list = main_page.check_bar(Locators.LOCATOR_TOOLS)
    count_elems = get_count_elements(automation_list)
    max_len = get_len_max_elem(automation_list)
    main_page.enter_word(Locators.LOCATOR_MESSAGE, f"{count_elems}\n{max_len}")

    main_page.click_on(Locators.LOCATOR_BUTTON)


if __name__ == "__main__":
    test(webdriver.Chrome())
    input("Press Enter to finish")
