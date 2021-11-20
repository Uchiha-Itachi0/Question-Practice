def power_of_2():
    number = int(input('Enter a number : '))
    if number == 0:
        return False
    number_of_one = 0
    while number != 0:
        if number & 1 == 1:
            number_of_one += 1
            if number_of_one > 1:
                return False
        number = number >> 1
    return True


def power_of_2_2():
    number = int(input('Enter a number : '))
    if number == 0:
        return False
    return number & (number - 1) == 0


print(power_of_2())
