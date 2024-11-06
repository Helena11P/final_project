import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from API.Search_API_page import Search
from API.values_api import base_url

param = pytest.mark.parametrize


@pytest.fixture
def driver():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    browser.maximize_window()
    yield browser

    browser.quit()


@pytest.fixture
def api() -> Search:
    return Search(base_url)
