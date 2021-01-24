Feature: ISBN-13 Test
    Test for ISBN-13 check sum algorithm

    Scenario Outline: Returns Control Sum
        Given ISBN-13 app is run
        When Input:  <isbn>
        Then Result: <res>

    Examples:
        | isbn |  res |
        | 978-3-16-148410-0 | 0 |
        | 978-1-56619-909-4 | 4 |
        | 978-1-4028-9462-6 | 6 |
        | 978-1-86197-876-9 | 9 |

    Scenario Outline: Returns False
        Given ISBN-13 app is run
        When Wrong input: <isbn>
        Then Returns False

    Examples:
        | isbn |
        | 978-3-16-148410-4 |
        | 978-1-56619-909-2 |
        | 978-1-4028-9462-8 |
        | 978-1-86197-876-1 |

    Scenario Outline: Returns Error
        Given ISBN-13 app is run
        When Input is not ISBN-13 <isbn>
        Then Returns error

    Examples:
        | isbn |
        | 978-3-16-148-5 |
        | 12345 |
        | dasdasdasda |
        | -=+;'[/.;'\*&^%!@#$ |