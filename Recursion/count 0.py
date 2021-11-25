def count_0(number, count):
    if number == 0:
        return count
    number, r = divmod(number, 10)
    if r == 0:
        count += 1
    return count_0(number, count)


print(count_0(10020000, 0))
