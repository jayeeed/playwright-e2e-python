from playwright.sync_api import Page


class ChatboxPage:
    def __init__(self, page: Page):
        self.page = page

        self.chatbox_nav = (
            '//*[@id="root"]/div[1]/div/div/div[2]/nav/div[2]/div/button[3]'
        )
        self.chatbox_textarea = '[id="reply-input"]'
        self.chatbox_send = '//*[@id="root"]/div[1]/div/div/div[2]/main/div/div/div/div[1]/div[2]/div[2]/div[3]/div[2]/div/div[2]/div[2]/button'

    def goto_chatbox(self):
        self.page.click(self.chatbox_nav)

    def type_chatbox(self, message: str):
        self.page.fill(self.chatbox_textarea, message)

    def send_chatbox(self):
        self.page.click(self.chatbox_send)
