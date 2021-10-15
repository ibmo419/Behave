from behave import given, when, then
from numpy.testing import assert_equal
from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains

@given(u'the user navigate to drag-drop home page')
def step_impl(context):
    context.dd.setup()
    # context.browser.get('https://qavbox.github.io/demo/dragndrop/')



@when(u'he drag the rectangle in his taget (green rectangle)')
def step_impl(context):
    context.dd.drag()
    time.sleep(2)


@then(u'"Droped!" message will be displayed in the target plce')
def step_impl(context):
    assert_equal(context.dd.result(), "Dropped!")

