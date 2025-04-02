import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope='class')
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        request.cls.browser = browser
        yield browser
        browser.close()


@pytest.fixture(scope='function')
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture(scope='browser')
class Test_titleclass:
    def test_google(self, page):
        page.goto("https://google.com")
        assert page.url == "https://www.google.com/"

    def test_orange(self, page):
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        assert page.url == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"