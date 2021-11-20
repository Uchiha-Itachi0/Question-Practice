import math

"""
Formula for finding the number of digit in any base is : 
int(log(number, base)) + 1
"""


def number_of_digit():
    number = int(input('Enter a number : '))
    base = int(input('Enter base : '))
    return int(math.log(number, base)) + 1


print(number_of_digit())
