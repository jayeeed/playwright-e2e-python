from playwright.sync_api import Playwright, sync_playwright

def main(playwright: Playwright):
    config = {
        "timeout": 60000,
        "expect_timeout": 20000
    }
    return config
