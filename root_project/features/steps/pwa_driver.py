# encoding: utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from test_driver import TestDriver
import os

class PwaDriver(TestDriver):

    def __init__(self):
        TestDriver.__init__(self)
        self.app = None
        self.chrome_driver_path = None

    def open(self, headless):
        TestDriver.open(self)

        self.chrome_driver_options = webdriver.ChromeOptions()
        if headless:
            self.chrome_driver_options.add_argument('headless')
            self.chrome_driver_options.add_argument('no-sandbox')

        self.driver = webdriver.Chrome(self.chrome_driver_path, chrome_options=self.chrome_driver_options)
        self.driver.get(self.app)
        self.driver.implicitly_wait(30)

    def url_assert_equal(self, url):
        TestDriver.url_assert_equal(self, url)

        for i in xrange(0, 20):
            try:
                current_url = self.driver.current_url[-len(url):]
                assert current_url == url
                return
            except:
                time.sleep(1)
        assert False , 'Erro ao comparar URL\'s. \n URL do Browser: {} difere da esperada: {}'.format(current_url, url)

    def fill_value_by_name(self, field, value):
        el = self.driver.find_element_by_name(field)
        self.__fill_value(el, value)

    def __fill_value(self, el, value):
        el.send_keys(value + Keys.TAB)
        set_value = el.get_attribute('value')
        assert set_value == value

    def screen_assert_equal(self, screen):
        TestDriver.screen_assert_equal(self, screen)
        # TODO
        # assert False

    def search_text(self, elemento):
        value = elemento.get_attribute('value')
        if value == None:
            value = elemento.text
        return value
