def calculate_sq_sum(number):
    if number <= 0:
        return 0
    else:
        number, r = divmod(number, 10)
        return (r ** 2) + calculate_sq_sum(number)


def happy_number(number: int) -> bool:
    number = calculate_sq_sum(number)
    slow = number
    fast = number
    while True:
        slow = calculate_sq_sum(slow)
        fast = calculate_sq_sum(calculate_sq_sum(fast))
        if fast == 1:
            return True
        if fast == slow:
            return False


print(happy_number(13))
