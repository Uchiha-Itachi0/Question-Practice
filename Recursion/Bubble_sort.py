def bubble_sort(arr, first, last):
    if last == 0:
        return

    # because last element is always going to be sorted
    elif first < last - 1:
        if arr[first] > arr[first + 1]:
            arr[first], arr[first + 1] = arr[first + 1], arr[first]
        bubble_sort(arr, first + 1, last)
    else:
        bubble_sort(arr, 0, last - 1)


arr = [5, 4, 3, 2, 1]
bubble_sort(arr, 0, len(arr))
print(arr)
