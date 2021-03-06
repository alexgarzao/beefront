from test_config import TestConfig
from components import Components
from time import gmtime, strftime



def before_all(context):
    context.config = TestConfig()
    context.config.driver = None
    context.config.components = Components()

def after_scenario(context, scenario):
    if context.failed:
        log = 'LOG-EXECUCAO-{}.log'.format(strftime("%Y-%m-%d", gmtime()))
        name_screen = context.config.driver.screenshot()
        message = "\nFeature:{}\n   Linha em que falhou:{}\n   Screenshot:{}\n\n".format(scenario.filename, scenario.line, name_screen)
        print(message)

        with open(log, 'a') as arq:
            arq.write(message)

def after_all(context):
    if context.config.driver:
        context.config.driver.quit()


# ----------------------------------------------------------------------------
# USER-DEFINED TYPES:
# ----------------------------------------------------------------------------
from behave import register_type

import parse
import parse_type


# @parse.with_pattern(r"\d+")
def parse_number(text):
    """
    Convert parsed text into a number.
    :param text: Parsed text, called by :py:meth:`parse.Parser.parse()`.
    :return: Number instance (integer), created from parsed text.
    """
    return int(text)
register_type(Number=parse_number)


from bdd.beefront.steps import steps, common, components
