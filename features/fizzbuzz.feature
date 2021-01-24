Feature: Fizzbuzz Test
    Scenario Outline: Returns Fizz
        Given Fizzbuzz app is run
        When I input <number>
        Then I get result <result>

    Examples:
        | number |  result |
        |      6 |    Fizz |
        |     10 |    Buzz |
        |     15 | FizzBuzz |
        |      2 |    None |
        |   fizz | ValueError |