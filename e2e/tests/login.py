import pytest
import json
from pages.login_page import LoginPage


def load_config():
    with open("e2e/config/config.json") as config_file:
        return json.load(config_file)


def load_login_data():
    with open("e2e/config/login_data.json") as login_file:
        return json.load(login_file)["user_credentials"]


def login(browser_context):
    page = browser_context

    config = load_config()
    login_data = load_login_data()

    base_url = config["base_url"]
    email = login_data["email"]
    password = login_data["password"]

    login_page = LoginPage(page)

    page.goto(f"{base_url}")

    login_page.login(email, password)

    page.wait_for_url(f"{base_url}/dashboard")

    assert page.url == f"{base_url}/dashboard"
    assert page.is_visible("text='Home'")
