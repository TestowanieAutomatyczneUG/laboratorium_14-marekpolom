from behave import *
from src.sample.isbn13 import Isbn13
from assertpy import *

use_step_matcher("re")

@given('ISBN-13 app is run')
def step_impl(context):
    context.isbn13 = Isbn13

@when('Input: (?P<isbn>.+)')
def step_impl(context, isbn):
    context.result = str(context.isbn13.csum(isbn))

@then('Result: (?P<res>.+)')
def step_impl(context, res):
    assert_that(context.result).is_equal_to(res)


@when('Wrong input: (?P<isbn>.+)')
def step_impl(context, isbn):
    context.result = context.isbn13.csum(isbn)

@then('Returns False')
def step_impl(context):
    assert context.result == False


@when('Input is not ISBN-13 (?P<isbn>.+)')
def step_impl(context, isbn):
    context.result = context.isbn13.csum(isbn)

@then('Returns error')
def step_impl(context):
    assert_that(context.result).is_equal_to('Input must contain 13 digits!')