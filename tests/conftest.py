import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument('--no-first-run')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-default-browser-check')
chrome_options.add_argument('--disable-default-apps')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-search-engine-choice-screen')
chrome_options.add_argument('--disable-extensions')


sys.path.append('C:/Users/Ana/PycharmProjects/python_ui_tests')


@pytest.fixture()
def driver():
    driver_service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service, options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()