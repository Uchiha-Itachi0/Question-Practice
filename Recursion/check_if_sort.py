def check_if_sort(array):
    # if length is 1 that means there is only 1 element left and since
    # we already compare it with previous value Therefore the answer will
    # definitely will be true.
    if len(array) == 1:
        return True
    boolean = array[0] <= array[1]

    # If at any point the boolean is False then the whole thing will false.
    # since we are using and operator
    return boolean and check_if_sort(array[1:])


def check_if_sorted_2(arr):
    # This logic is same as above
    if len(arr) == 1:
        return True

    # if at any point array is not sorted then we don't need to travel all the way
    # to end we can simply return false
    if arr[0] > arr[1]:
        return False

    # If the array is actually sorted then it will travel up to the end and finally return
    # True
    return check_if_sorted_2(arr[1:])


print(check_if_sorted_2([1, 2, 3, 6, 8]))
