from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None, help='Select lang: rus | eng ... ')


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")
    print("\nChrome is starting ...")
    if lang:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': lang})
        browser = webdriver.Chrome(options=options)
    else:
        browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
