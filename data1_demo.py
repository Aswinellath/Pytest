import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def browser_handle():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture(scope="function")
def page_handle(browser_handle):
    page = browser_handle.new_page()
    yield page
    page.close()

@pytest.mark.parametrize('invalid_number', ['admin','1234wrfgd','1234567890','0000000000'])
def test_invalid_login(page_handle, invalid_number):
    page_handle.goto('https://woocommerce-973242-5202660.cloudwaysapps.com/dashboard/')
    page_handle.wait_for_selector('//input[@id="user_login"]').type('xidala1772@arinuse.com')
    page_handle.wait_for_selector('//input[@id="user_pass"]').type('Xidala1772@arinuse.com')
    page_handle.wait_for_timeout(3000)
    page_handle.wait_for_selector('//input[@id="wp-submit"]').click()
    page_handle.wait_for_timeout(2000)
    page_handle.wait_for_selector('//a[@href="/dashboard/profile/"]').click()
    page_handle.wait_for_timeout(2000)
    page_handle.wait_for_selector('//button[@id="edit-button"]').click()
    page_handle.wait_for_timeout(2000)
    page_handle.wait_for_selector('//input[@type="tel"]').type(invalid_number)
    page_handle.wait_for_selector('//button[@id="save-button"]').click()
    # page_handle.wait_for_selector('//input[@id="user_login"]').type(invalid_username)
    # page_handle.wait_for_selector('//input[@id="user_pass"]').type(invalid_password)
    # page_handle.wait_for_selector('//input[@id="wp-submit"]').click()
    page_handle.wait_for_timeout(3000)
    error_message = page_handle.query_selector('//span[@id="phone-required"]').text_content()
    assert error_message == 'Phone Number Required'
    page_handle.wait_for_timeout(3000)



