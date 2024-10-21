from tests.login import login
from pages.chatbox_page import ChatboxPage
from utils.config_loader import load_config


def test_chatbox(browser_context):
    page = browser_context

    config = load_config()
    base_url = config["base_url"]

    chatbox_page = ChatboxPage(page)

    chatbox_page.goto_chatbox()
    page.wait_for_url(f"{base_url}/projects/1981/inbox")
    chatbox_page.type_chatbox("Hello, how are you?")
    chatbox_page.send_chatbox()
    assert chatbox_page.wait_for_message_to_appear("Hello, how are you?")
