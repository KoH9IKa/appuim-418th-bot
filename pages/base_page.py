from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.windows import WindowsOptions
from appium.webdriver.common.appiumby import AppiumBy
from packaging.tags import android_platforms
import re

from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator, timeout=10):
        return Wait(self.driver, timeout, poll_frequency=1).until(expected_conditions.element_to_be_clickable(locator)).click()

    def element_is_visible(self, locator, timeout=10.0):
        return Wait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=10.0):
        return Wait(self.driver, timeout).until(expected_conditions.visibility_of_all_elements_located(locator))

    @staticmethod
    def formate_locator_kwargs(locator, **kwargs):
        """После локатора обязательно передать ключ=значение всех заменяемых элементов строки что бы превратить
        /admin/clients?date[start]={start}&date[end]={end} => /admin/clients?date[start]=1234&date[end]=5678"""
        loc = locator[1]
        for key, value in kwargs.items():
            item = f'{{{key}}}'
            if item in loc:
                loc = re.sub(item, str(value), loc)
        return locator[0], loc

    def fill_text(self, locator, text=None, clear='default', click=True, by_script=False):  # pylint: disable=too-many-arguments
        """Если не работает удаление текста по дефолту - попробуй с clear='keys'"""
        element = self.element_is_visible(locator)
        if click is True:
            element.click()
        if clear == 'default':
            element.clear()
        if clear == 'keys':
            element.send_keys(Keys.CONTROL + "a")  # Выделение всего текста
            element.send_keys(Keys.BACKSPACE)  # Удаление выделенного текста
        if text != '' or text is not None:
            element.send_keys(text)
        if by_script is True:
            self.driver.execute_script(f"arguments[0].value = '{text}';", element)
            element.send_keys(Keys.ENTER)

    def get_text(self, elem, timeout=5):
        return Wait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(elem)).text
