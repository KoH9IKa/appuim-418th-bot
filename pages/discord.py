import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class DiscordPages(BasePage):

    def __init__(self, driver, env_username=None, env_password=None):
        super().__init__(driver)
        self.env_username = env_username
        self.env_password = env_password

    BUTTON_GET_IN = AppiumBy.XPATH, '//android.widget.TextView[@text="Вход"]'
    DISCORD_USERNAME = AppiumBy.XPATH, '//android.widget.EditText[@resource-id="login_login_input"]'
    DISCORD_PASSWORD = AppiumBy.XPATH, '//android.widget.EditText[@resource-id="login_password_input"]'
    BUTTON_LOGIN = AppiumBy.XPATH, '//android.widget.Button[@content-desc="Вход"]'

    PERMISSION_DENY = AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.permissioncontroller:id/permission_deny_button"]'
    GROUP_NAME = AppiumBy.XPATH, '//android.widget.Button[contains(@content-desc,"{group_name}")]/android.view.ViewGroup/android.widget.ImageView'
    CHANNEL_NAME = AppiumBy.XPATH, '//android.widget.TextView[@text="{channel_name}"]'
    MESSAGE_BLOCK = AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout'
    MESSAGE_TEXT = AppiumBy.XPATH, './/androidx.recyclerview.widget.RecyclerView/android.widget.TextView'
    BUTTON_GO_TO_LAST_MESSAGE = AppiumBy.XPATH, '//android.widget.Button[@content-desc="Перейти к последним сообщениям"]/android.view.ViewGroup/android.widget.ImageView'

    AUTHOR_LOCATOR = (AppiumBy.ID, 'com.discord:id/author_name')
    NAME_LOCATOR = (AppiumBy.XPATH, '//android.widget.RelativeLayout[@text]')
    MESSAGE_LOCATOR = (AppiumBy.XPATH, './/android.widget.TextView[@text]')

    MESSAGE_INPUT = (AppiumBy.XPATH, '//android.widget.EditText[@resource-id="com.discord:id/chat_input_edit_text"]')
    SEND_MESSAGE = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Отправить"]')

    def login_in(self, username=None, password=None):
        name = username if username is not None else self.env_username
        pswrd = password if password is not None else self.env_password
        self.click(self.BUTTON_GET_IN)
        self.fill_text(self.DISCORD_USERNAME, name)
        self.fill_text(self.DISCORD_PASSWORD, pswrd)
        self.click(self.BUTTON_LOGIN)


    def press_permission_button(self, action='deny'):
        button = None
        if action == 'deny':
            try:
                button = self.element_is_visible(self.PERMISSION_DENY)
            except:
                pass
        if button:
            button.click()

    def select_discord_group(self, group_name):
        locator = self.formate_locator_kwargs(self.GROUP_NAME, group_name=group_name)
        group = self.element_is_visible(locator)
        group.click()

    def select_group_channel(self, channel_name):
        locator = self.formate_locator_kwargs(self.CHANNEL_NAME, channel_name=channel_name)
        channel = self.element_is_visible(locator)
        channel.click()

    def go_to_last_message(self):
        try:
            while True:
                self.click(self.BUTTON_GO_TO_LAST_MESSAGE, timeout=1)
        except:
            pass

    def get_message_list(self, start:int|None, end:int|None=None):
        message_log = []
        before_slice_blocks = self.elements_are_visible(self.MESSAGE_BLOCK)
        blocks = before_slice_blocks[start:end]
        for block in blocks:
            # print(blocks.index(block))
            try:
                name = block.find_element(*self.AUTHOR_LOCATOR).text
                message = block.find_element(*self.MESSAGE_TEXT).text
                message_log.append(f'{name}: {message}')
                # print(f'{name}: {message}')
            except:
                try:
                    name = block.find_element(*self.NAME_LOCATOR).text
                    message = block.find_element(*self.MESSAGE_LOCATOR).text
                    message_log.append(f'{name}: {message}')
                    # print(f'{name}: {message}')
                except:
                    message_log.append('-------------------------')
                    pass
        return message_log

    def get_last_two_messages(self):
        message_log = {}
        blocks = self.elements_are_visible(self.MESSAGE_BLOCK)
        for block in blocks[-2:]:
            name = block.find_element(*self.AUTHOR_LOCATOR).text
            message = block.find_element(*self.MESSAGE_TEXT).text
            message_log[name] = message
        return message_log

    def click_on_message_input(self):
        self.click(self.MESSAGE_INPUT)

    def enter_message(self, message):
        self.fill_text(self.MESSAGE_INPUT, message)
        time.sleep(3)

    def click_on_send_message(self):
        self.click(self.SEND_MESSAGE)
