import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as chrome_options


service = Service("/usr/lib/chromium-browser/chromedriver")



@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')#  Use headless if you dont need a browser UI
    options.add_argument('--start-maximazed')
    options.add_argument('--windows-size=2650,900')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(service=service,options=options)
    return driver


@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.yourexamplesayt/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    driver.delete_all_cookies()
    yield driver
    driver.quit()