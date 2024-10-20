import json
from tests.login import login
from pages.dashboard_page import DashboardPage


def load_config():
    with open("e2e/config/config.json") as config_file:
        return json.load(config_file)


def test_chatbox(browser_context):
    page = browser_context
    config = load_config()
    base_url = config["base_url"]
    login(browser_context)

    dashboard_page = DashboardPage(page)

    dashboard_page.goto_chatbox()

    page.wait_for_timeout(5000)

    assert page.url == f"{base_url}/projects/1981/inbox"

    dashboard_page.type_chatbox("Hello, how are you?")

    page.wait_for_timeout(5000)

    dashboard_page.send_chatbox()
