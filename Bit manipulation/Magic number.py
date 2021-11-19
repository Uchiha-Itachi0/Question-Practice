# A simple calculation no bit manipulation is required
def magic_number():
    number = int(input('Enter a number : '))
    bit = []
    while number != 1:
        number, remainder = divmod(number, 2)
        bit.append(remainder)
    bit.append(1)
    ans = 0
    power = 1
    for byte in bit:
        ans = ans + (byte * (5 ** power))
        power += 1
    return ans


"""
In this example we don't need to convert the number in binary to find the answer.
& operator do that internally, we only have to focus on logic.
Logic : 
We have to multiply 5 with each bits now how can we do that,
Since,
N & 1 = N   where N can be 0, 1
Therefore if we & the give number we can find the bit to multiply with 5, but now the question arises how
can we find the next bit because if we keep & the number with 1 it will give same result but we have to 
move forward means we have to ignore the last digit in each iteration, and that can be done using right
shift.
"""
def magic_number_bit():
    number = int(input('Enter a number : '))
    base = 5
    ans = 0
    while number != 0:
        ans += (number & 1) * base
        base *= 5
        number = number >> 1
    return ans


print(magic_number_bit())
