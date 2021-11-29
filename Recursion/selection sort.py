# For finding the maximum index in an array
def getMax(arr, first, last):
    maximum_index = first
    first += 1
    while first <= last:
        if arr[first] > arr[maximum_index]:
            maximum_index = first
        first += 1
    return maximum_index


def selection_sort(arr, first, last):
    if first == last:
        return
    else:
        # finding the Maximum element index
        maximum_index = getMax(arr, first, last)
        arr[last], arr[maximum_index] = arr[maximum_index], arr[last]
        selection_sort(arr, first, last - 1)


arr = [5, 4, 3, 2, 1]
selection_sort(arr, 0, len(arr) - 1)
print(arr)
