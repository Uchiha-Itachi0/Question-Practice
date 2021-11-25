import math


def reverse(number):
    if number > 0:
        number, r = divmod(number, 10)
        print(r, end='')
        return reverse(number)


def reverse_2(number, power):
    if number == 0:
        return 0
    else:
        if number > 0:
            number, r = divmod(number, 10)
            result = r * (10 ** power)
            return result + reverse_2(number, power - 1)


# How to calculate number of digit in some number of any base
# Formula for that : (int(log(number, base) + 1)
number = 12345678901

# we don't need +1 because we are raising 10 to power 0
number_of_digit = int(math.log(number, 10))
print(reverse_2(number, number_of_digit))
