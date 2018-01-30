# encoding: utf-8

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from appium import webdriver
import time
from test_driver import TestDriver


class AndroidDriver(TestDriver):
    base_xpath = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"

    def __init__(self):
        TestDriver.__init__(self)
        self.platform_name = None
        self.platform_version = None
        self.device_name = None
        self.app = None
        self.remote = None

    def open(self):
        TestDriver.open(self)
        desired_caps = {}
        desired_caps['platformName'] = self.platform_name
        desired_caps['platformVersion'] = self.platform_version
        desired_caps['deviceName'] = self.device_name
        desired_caps['app'] = self.app
        self.driver = webdriver.Remote(self.remote, desired_caps)

    def fill_value_by_xpath(self, xpath, value):
        el = context.config.driver.find_element_by_xpath(AndroidDriver.base_xpath + xpath)
        self.__fill_value(el, value)

    def __hide_keyboard(self):
        # TestDriver.hide_keyboard(self)
        self.driver.hide_keyboard()

    def __fill_value(self, el, value):
        el.click()
        el.set_text(value)
        # el.send_keys(valor)

        try:
            context.config.driver.__hide_keyboard()
            time.sleep(2)
        except:
            print ('hide falhou')
            pass

    def screen_assert_equal(self, screen):
        TestDriver.screen_assert_equal(self, screen)
        # TODO
        # assert False

    def find_element_by_xpath(self, xpath):
        return TestDriver.find_element_by_xpath(self, AndroidDriver.base_xpath + xpath)
