import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


def test_goto_google(page):
    page.goto("https://google.com")
    assert page.title() == "Google"


def test_goto_redbus(page):
    page.goto("https://redbus.com")
    assert page.title() == "Bus Ticket Booking Online at Cheapest Price with Top Bus Operators- redBus"

