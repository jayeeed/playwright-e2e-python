from playwright.sync_api import Page


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.chatbox = (
            '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[3]/a/div'
        )
        self.chatbox_textarea = '[id="reply-input"]'
        self.chatbox_send = '[data-testid="button-element"]'

    def click_chatbox(self):
        self.page.click(self.chatbox)

    def goto_chatbox(self):
        self.click_chatbox()

    def type_chatbox(self, message: str):
        self.page.fill(self.chatbox_textarea, message)

    def send_chatbox(self):
        self.page.click(self.chatbox_send)
