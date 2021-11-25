def reduce_to_0(number, step):
    if number == 0:
        return step
    if number % 2 == 0:
        return reduce_to_0(number // 2, step + 1)
    return reduce_to_0(number - 1, step + 1)


print(reduce_to_0(14, 0))
