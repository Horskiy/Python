def sum1(a, b, c=3):
    return a + b + c


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def subtraction(a, b):
    return a - b


def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
