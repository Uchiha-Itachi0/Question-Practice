def duplicate():
    numbers = list(map(int, input().split()))
    ans = 0
    for number in numbers:
        ans = ans ^ number
    return ans


print(duplicate())
