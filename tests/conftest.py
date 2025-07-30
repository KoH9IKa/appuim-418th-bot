from appium import webdriver
from appium.options.android import UiAutomator2Options
import os
from dotenv import load_dotenv
import pytest
from pages.discord import DiscordPages


@pytest.fixture()
def app(request):
    application = Application()
    yield application
    if application:
        def fin():
            application.driver.quit()

        request.addfinalizer(fin)



class Application:
    load_dotenv()
    DISCORD_USERNAME = os.getenv('DISCORD_USERNAME')
    DISCORD_PASSWORD = os.getenv('DISCORD_PASSWORD')
    APPIUM_SERVER_URL = os.getenv('APPIUM_SERVER_URL', default='http://localhost:4723/wd/hub')

    def __init__(self):
        capabilities = {"platformName":"Android",
                        "automationName": "uiautomator2",  # плагин для автоматизации
                        "appPackage": "com.discord",  # имя приложения в системе, что бы узнать пишем adb shell pm list package в командной строке при подключенном устройстве/эмуляторе
                        "noReset": True,  # флаг сбрасывающий текущее положение
                        'newCommandTimeout': 40,  # таймаут между командами, не должен быть меньше самого длинного ожидания
                        "udid": "emulator-5554"}  # эмулятор в Андроид Студио
                        # "udid": "RZ8M840C60F"  # реальное устройство
        self.driver = webdriver.Remote(self.APPIUM_SERVER_URL,
                                          options=UiAutomator2Options().load_capabilities(capabilities))

        self.dis = DiscordPages(self.driver, self.DISC_USERNAME, self.DISC_PASSWORD)