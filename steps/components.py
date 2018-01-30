# encoding: utf-8

from behave import given, when, then

import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from common import value_with_mask



@given(u'que quero definir os componentes da tela')
def step_impl(context):
    context.config.components.clear()


@given(u'que o componente {name} tem o id {internal_id}')
def step_impl(context, name, internal_id):
    context.config.components.new_id_component(name, internal_id)


@given(u'que o componente {name} tem o nome {internal_id}')
def step_impl(context, name, internal_id):
    context.config.components.new_name_component(name, internal_id)


@given(u'que o componente {name} tem o texto {internal_id}')
def step_impl(context, name, internal_id):
    context.config.components.new_text_component(name, internal_id)


@given(u'que o componente {name} tem o xpath {internal_id}')
def step_impl(context, name, internal_id):
    context.config.components.new_xpath_component(name, internal_id)


@given(u'que o componente {name} tem o automation id {internal_id}')
def step_impl(context, name, internal_id):
    context.config.components.new_automation_id_component(name, internal_id)


@when(u'tento definir os componentes')
def step_impl(context):
    pass


@then(u'recebo um ok')
def step_impl(context):
    pass

@given(u'vejo o {name} com o valor {expected_value}')
@then(u'vejo o {name} com o valor {expected_value}')
def step_impl(context, name, expected_value):

    component = context.config.components.get_component(name)
    element = context.config.driver.find_element(component)
    value = context.config.driver.search_text(element)
    assert value == expected_value

@given(u'preencho o {name} com o valor {value}')
def step_impl(context, name, value):
    if value == "<ignora>":
        return
    if value == "<espaço>":
        value = ' '
    component = context.config.components.get_component(name)
    context.config.driver.find_element(component).clear()
    context.config.driver.find_element(component).send_keys(value)


@given(u'preencho e valido o {name} com o valor {value} e valor esperado {expected_value}')
def step_impl(context, name, value, expected_value):
    if value == "<ignora>":
        return
    component = context.config.components.get_component(name)
    context.config.driver.find_element(component).clear()
    context.config.driver.find_element(component).send_keys(value)
    set_value = context.config.driver.find_element(component).get_attribute('value')
    assert set_value == expected_value


@given(u'preencho e valido o {name} com o valor {value} e máscara {mask}')
def step_impl(context, name, value, mask):
    if value == "<ignora>":
        return

    component = context.config.components.get_component(name)
    context.config.driver.find_element(component).clear()
    context.config.driver.find_element(component).send_keys(value)
    set_value = context.config.driver.find_element(component).get_attribute('value')
    expected_value = value_with_mask(value, mask)
    assert set_value == expected_value


@then(u'clico no {name}')
@given(u'clico no {name}')
@when(u'clico no {name}')
def step_impl(context, name):
    time.sleep(1)

    component = context.config.components.get_component(name)
    #TODO: Ver se o componente pode estar visivel mas nao clicavel
    #TODO: Precisa validar se esta habilitado?!
    for i in xrange(0, 10):
        try:
            context.config.driver.find_element(component).click()
            return
        except:
            time.sleep(1)

@when(u'aguardo {seconds:Number} segundos')
@given(u'aguardo {seconds:Number} segundos')
def step_impl(context, seconds):
    time.sleep(seconds)


@given(u'seleciono em {name} o valor {value}')
def step_impl(context, name, value):
    if value == "<ignora>":
        return
    component = context.config.components.get_component(name)
    select = Select(context.config.driver.find_element(component))
    select.select_by_visible_text(value)
    selected_option = select.first_selected_option
    set_value = selected_option.text
    assert set_value == value