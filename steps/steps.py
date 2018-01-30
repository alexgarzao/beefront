# encoding: utf-8
from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from pwa_driver import PwaDriver
from android_driver import AndroidDriver

import platform


# TODO: o driver abaixo teria mais recursos do que o do selenium???
# from appium import webdriver


@given(u'que quero efetuar o login')
def step_impl(context):
    pass


@given(u'que quero testar um app PWA')
def step_impl(context):
    context.config.driver = PwaDriver()
    os = platform.system().lower()
    context.config.driver.chrome_driver_path = ("./chromedriver/%s/chromedriver" % os)


@given(u'o app a ser testado está em {app}')
def step_impl(context, app):
    context.config.server_address = app


@given(u'quero rodar os testes no modo {mode}')
def step_impl(context, mode):
    context.config.headless = True


@given(u'estou na tela {screen}')
def step_impl(context, screen):
    # import pdb; pdb.set_trace()

    context.config.driver.screen_assert_equal(screen)


# @given(u'preencho o campo de id {campo} com o valor {valor}')
# def step_impl(context, campo, valor):
#     # driver.find_element_by_id('loginForm')
#     context.config.driver.find_element_by_xpath('//*[@id="' + campo + '"]').send_keys(valor)

# @given(u'clico no xpath {campo}')
# def step_impl(context, campo):
#     # driver.find_element_by_id('loginForm')
#     context.config.driver.find_element_by_xpath(campo).click()
#     # time.sleep(1)

@given(u'seleciono a select {name} com o texto {texto}')
def step_impl(context, name, texto):
    # import pdb; pdb.set_trace()

    if not texto == "<ignora>":
        select = Select(context.config.driver.find_element_by_name(name))
        select.select_by_visible_text(texto)
        selected_option = select.first_selected_option
        set_value = selected_option.text
        assert set_value == texto
    else:
        pass

# @given(u'preencho o campo de nome {campo} com o valor {valor} valor esperado {valor_esperado}')
# def step_impl(context, campo, valor, valor_esperado):
#     # driver.find_element_by_id('loginForm')
#     if not valor == "<ignora>":
#         context.config.driver.find_element_by_name(campo).send_keys(valor)
#         set_value = context.config.driver.find_element_by_name(campo).get_attribute('value')
#         # print (set_value)
#         # time.sleep(5)
#         assert set_value == valor_esperado
#     else:
#         pass


# @when('clico no elemento pelo texto {valor}')
# @given('clico no elemento pelo texto {valor}')
# def step(context, valor):
#     time.sleep(1)
#     valor = '//*[text()='+ valor +']'
#     # import pdb; pdb.set_trace()
#
#     context.config.driver.find_element_by_xpath(valor).click()

# @given('clico no elemento pelo id {valor}')
# def step(context, valor):
#     context.config.driver.find_element_by_id(valor).click()

@when('clico em {valor}')
def step(context, valor):
    # import pdb; pdb.set_trace()

    context.config.driver.find_element_by_xpath('//*[@id="' + valor + '"]').click()

@given('estou na url {url}')
@then('sou direcionado para a url {url}')
def step(context, url):

    context.config.driver.url_assert_equal(url)

# @given(u'que quero cadastrar um contato')
# def step_impl(context):
#     pass


@given(u'que quero testar um app android')
def step_impl(context):
    context.config.driver = AndroidDriver()

    context.config.driver.platform_name = 'Android'


@given(u'a versão da plataforma é {platform_version}')
def step_impl(context, platform_version):
    context.config.driver.platform_version = platform_version


@given(u'o nome do device é {device_name}')
def step_impl(context, device_name):
    context.config.driver.device_name = device_name


@given(u'o app a ser testado é {app}')
def step_impl(context, app):
    context.config.driver.app = '/root/tmp/' + app


@given(u'o servidor está em {remote}')
def step_impl(context, remote):
    context.config.driver.remote = remote


@when(u'tento inicializar o teste')
def step_impl(context):
    # import pdb; pdb.set_trace()

    context.config.driver.app = context.config.server_address
    context.config.driver.open(context.config.headless)


@then(u'recebo um status ok')
def step_impl(context):
    pass


@then(u'finalizo o teste')
def step_impl(context):
    pass
    # context.driver.quit()



# @given(u'que estou na tela de login')
# def step_impl(context):
#     pass

# @when(u'clico no xpath {campo}')
# @given(u'clico no xpath {campo}')
# def step_impl(context, campo):
#     # import pdb; pdb.set_trace()
#
#     context.config.driver.find_element_by_xpath(campo).click()


# @when(u'clico no textview de xpath {campo}')
# @given(u'clico no textview de xpath {campo}')
# def step_impl(context, campo):
#     # import pdb; pdb.set_trace()
#
#     context.config.driver.find_element_by_xpath(campo).click()


@then('sou direcionado para a tela de {screen}')
def step(context, screen):
    context.config.driver.screen_assert_equal(screen)


@given(u'que quero cadastrar um contato')
def step_impl(context):
    pass


# @given(u'preencho o campo de nome {campo} com o valor {valor}')
# def step_impl(context, campo, valor):
#     if valor == "<ignora>":
#         return
#
#     context.config.driver.fill_value_by_name(campo, valor)
#
#
# @given(u'preencho o campo xpath {xpath} com o valor {valor}')
# def step_impl(context, xpath, valor):
#     if valor == "<ignora>":
#         return
#
#     context.config.driver.fill_value_by_xpath(xpath, valor)

# def __find_element_by_xpath(context, field):
#     for retries in xrange(0, 30):
#         try:
#             el = context.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/' + field)
#             return el
#         except:
#             time.sleep(1)
#
#     return None
