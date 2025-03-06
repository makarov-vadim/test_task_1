import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")

    browser = webdriver.Chrome()
    yield browser
    alert_obj = browser.switch_to.alert
    assert alert_obj.text == 'Message received!'

    print("\nquit browser..")
    browser.quit()