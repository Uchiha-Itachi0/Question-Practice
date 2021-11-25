def sum_of_digit(number):
    number = str(number)
    if len(number) == 0:
        return 0
    else:
        return int(number[0]) + sum_of_digit(number[1:])


def sum_of_digit_2(number):
    if number == 0:
        return 0
    else:
        number, r = divmod(number, 10)
        return r + sum_of_digit_2(number)


print(sum_of_digit_2(123456789))
