from behave import *
from src.sample.fizzBuzz import FizzBuzz
from assertpy import *

use_step_matcher("re")

@given('Fizzbuzz app is run')
def step_impl(context):
    context.fizzbuzz = FizzBuzz


@when('I input (?P<number>.+)')
def step_impl(context, number):
    print(number)
    context.result = context.fizzbuzz.game(number)


@then('I get result (?P<result>.+)')
def step_impl(context, result):
    print(result)
    assert_that(context.result).is_equal_to(result)