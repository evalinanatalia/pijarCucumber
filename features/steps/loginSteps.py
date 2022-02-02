from selenium import webdriver
from behave import *
import time


@given(u'launch the browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when(u'open the Pijar website')
def step_impl(context):
    context.driver.get("https://pijarmahir.id/")


@then(u'the website has been opened')
def step_impl(context):
    assert context.driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button').is_displayed()


@then(u'click menu login')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[1]/div/header/div/div[4]/div[2]/a[1]/button').click()


@then(u'input the username "{username}" and password "{password}"')
def step_impl(context, username, password):
    context.driver.find_element_by_id('email').send_keys(username)
    context.driver.find_element_by_id('password').send_keys(password)


@then(u'click th login button')
def step_impl(context):
    context.driver.find_element_by_xpath('/html/body/div[1]/main/div[1]/div[2]/div[2]/form/button').click()


