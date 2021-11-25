"""
* * * *
* * *
* *
*
"""


# Recursion using one for loop

def pattern1(rows):
    if rows > 0:
        for i in range(rows):
            print('*', end=' ')
        print()
        return pattern1(rows - 1)


# Pure recursion
def pattern_1(row, col):
    # base case
    if row < 0:
        return

    # When this condition failed that means we have printed all the required column now we have to change
    # the row
    if col <= row:
        print('*', end=' ')
        pattern_1(row, col + 1)
    else:
        print()
        pattern_1(row - 1, 0)


# opposite of above using one for loop
def pattern2(rows):
    if rows > 0:
        pattern2(rows - 1)
        for i in range(rows):
            print('*', end=' ')
        print()


# opposite of above using pure recursion
def pattern_2(rows, row=0, col=0):
    if row >= rows:
        return
    elif col <= row:
        print('*', end=' ')
        pattern_2(rows, row, col + 1)
    else:
        print()
        pattern_2(rows, row + 1, 0)


pattern_2(4)
