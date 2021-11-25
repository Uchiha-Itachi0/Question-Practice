def palindrome(string, low, high):
    if low >= high:
        return True
    else:

        # The idea is simple if at any point value is False then the answer will definitely will be false
        # because we are using and operator. On the other hand if the value is always true then the answer
        # will definitely be true
        value = string[low] == string[high]
        return value and palindrome(string, low + 1, high - 1)


print(palindrome('1', 0, 0))
