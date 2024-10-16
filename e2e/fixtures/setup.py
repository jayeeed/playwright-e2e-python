import pytest
from playwright.sync_api import Browser, BrowserContext, Page
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as playwright:
        browser: Browser = playwright.chromium.launch(headless=False)
        context: BrowserContext = browser.new_context(viewport=None)

        page: Page = context.new_page()
        yield page

        # page.evaluate("window.moveTo(0, 0); window.resizeTo(screen.width, screen.height);")

        context.close()
        browser.close()
